from src.Ui_Files.DockWidgets.Py.dw_XPS import Ui_DockWidget
from src.gui_elements.RC_Fucntions import *
from src.gui_elements.plotting_functions import *
from src.gui_elements.general_functions import *
from lmfit import Model, Parameters
from scipy.linalg import norm
from lmfit.models import VoigtModel, GaussianModel, LorentzianModel, PseudoVoigtModel
from matplotlib.widgets import SpanSelector
import matplotlib.pyplot as plt

class XPS_view(QtWidgets.QDockWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.ui = Ui_DockWidget()
        self.ui.setupUi(self)
        self._init_vars()
        self._init_UI()

    def _init_vars(self):
        self.current_data_container = None
        self.data = None
        self.model = None
        self.x_data = None
        self.y_data = None
        self.model = QtWidgets.QFileSystemModel()
        self.tree_view = self.ui.XPS_treeView
        self.context_menu = QtWidgets.QMenu(self)
        self.fit_obj = {}

    def _init_UI(self):
        rc_browser_options(self)
        self.model.setRootPath('')
        self.tree_view.setModel(self.model)
        self.tree_view.setSortingEnabled(True)
        self.tree_view.sortByColumn(True)
        self.tree_view.setRootIndex(self.model.index(self.main_window.settings.value('XPS_PATH')))
        self.tree_view.setModel(self.model)
        self.tree_view.installEventFilter(self)
        self.tree_view.setColumnWidth(0, 200)

        self.ui.plot_pb.clicked.connect(lambda: self.plot())
        self.ui.fill_cols_pb.clicked.connect(lambda: self.fill_cols())
        self.ui.xpsrange_rb.toggled.connect(self.select_xps_range)
        self.ui.fit_range_cb.currentIndexChanged.connect(lambda: self.fit_range_changed())
        self.ui.fit_pb_2.clicked.connect(lambda: self.fit_fun())
        self.ui.initplot_pb.clicked.connect(lambda: self.initial_fit())
        self.ui.clear_fit_objects_pb.clicked.connect(lambda: self.clear_fit_objs())

    def eventFilter(self, object, event):
        # For right click events
        if event.type() == QtCore.QEvent.ContextMenu:
            self.context_menu.exec_(self.mapToGlobal(event.pos()))
        return False

    def fill_cols(self):
        self.ui.tw_x.clear()
        self.ui.tw_y.clear()
        path = self.model.filePath(self.tree_view.currentIndex())
        filename, extension = os.path.splitext(self.model.filePath(self.tree_view.currentIndex()))
        if extension == '.CSV' or extension == '.csv':
            self.data = pd.read_csv(path, delimiter=',', skiprows=self.ui.skip_rows_sb.value())
        elif extension == '.xls' or extension == '.xlxs':
            excelfile = pd.ExcelFile(path)
            self.data = pd.read_excel(excelfile, "Sheet1",skiprows=self.ui.skip_rows_sb.value())
        elif extension == '.X01':
            self.data = pd.read_csv(path, delimiter='   ', skiprows=self.ui.skip_rows_sb.value(), engine='python')
        elif extension =='.txt':
            self.data = pd.read_csv(path, sep='\t', skiprows=self.ui.skip_rows_sb.value())
        else:
            print(extension)
            self.data = pd.read_csv(path, sep='\t',skiprows=self.ui.skip_rows_sb.value())

        strings = [col for col in self.data.columns]
        column_list_x = []
        column_list_y = []
        for i in strings:
            column_list_x.append(QtWidgets.QTreeWidgetItem([i]))
            column_list_y.append(QtWidgets.QTreeWidgetItem([i]))
            self.ui.tw_x.addTopLevelItems(column_list_x)
            self.ui.tw_y.addTopLevelItems(column_list_y)

    def correct_to(self, x_data, y_data, correction):
        lims = [find_nearest(x_data, 295),find_nearest(x_data, 260)]
        # np.where(y_data[lims[0]:lims[1]] == np.amax(y_data[lims[0]:lims[1]]))
        idx = np.where(y_data == np.amax(y_data[lims[0]:lims[1]]))[0]
        return x_data + correction - x_data[idx]

    def plot(self):
        x = self.ui.tw_x.currentIndex().data()
        self.x_data = self.data[x].to_numpy()
        self.x_data = self.x_data[~np.isnan(self.x_data)]
        y = self.ui.tw_y.currentIndex().data()
        self.y_data = self.data[y].to_numpy()
        self.y_data = self.y_data[~np.isnan(self.y_data)]
        # self.x_data = self.x_data+float(self.ui.offset_LE.text())
        try:
            self.x_data = self.correct_to(self.x_data,self.y_data, 284.8)
        except ValueError:
            print('correct to didnt work, falling back to offset in c1s')
            self.x_data = np.asarray(self.x_data)
            self.x_data = self.x_data + self.ui.correctc1s_dsb.value()
        ApplicationSettings.ALL_DATA_PLOTTED[str(x)] = \
            self.main_window.ax.plot(self.x_data, self.y_data, label=x)
        self.xps_basic()

    def select_xps_range(self,enabled):
        if enabled:
            self.span = SpanSelector(self.main_window.ax, self.on_select, 'horizontal', useblit=False,
                                     rectprops=dict(alpha=0.2, facecolor='blue'))
        else:
            del self.span

    def on_select(self,minimum, maximum):
        self.fit_obj[str(np.round(minimum,1))+'+'+str(np.round(maximum,1))] = Fit_Object(self.x_data,self.y_data,minimum,maximum)
        ApplicationSettings.ALL_DATA_PLOTTED[str(np.round(minimum,1))+'+'+str(np.round(maximum,1))] = \
            self.main_window.ax.plot(self.fit_obj[str(np.round(minimum,1))+'+'+str(np.round(maximum,1))].shirley[0],
                                     self.fit_obj[str(np.round(minimum,1))+'+'+str(np.round(maximum,1))].shirley[1])
        self.ui.fit_range_cb.clear()
        self.ui.fit_range_cb.addItems([i for i in self.fit_obj.keys()])
        self.ui.xpsrange_rb.setChecked(False)
        self.main_window.canvas.draw()

    def fit_range_changed(self):
        try:
            temp = self.fit_obj[self.ui.fit_range_cb.currentText()].peak_constraints
            _, _, _, constraints = self.checked_cons()
            # constraints = [[self.ui.amp1_sb,self.ui.amp1l_sb,self.ui.amp1h_sb],
            #         [self.ui.cen1_sb,self.ui.cen1l_sb,self.ui.cen1h_sb],
            #         [self.ui.sigma1_sb,self.ui.sigma1l_sb,self.ui.sigma1h_sb]],\
            #               [[self.ui.amp2_sb, self.ui.amp2l_sb, self.ui.amp2h_sb],
            #       [self.ui.cen2_sb, self.ui.cen2l_sb, self.ui.cen2h_sb],
            #       [self.ui.sigma2_sb, self.ui.sigma2l_sb, self.ui.sigma2h_sb]],\
            #               [[self.ui.amp3_sb, self.ui.amp3l_sb, self.ui.amp3h_sb],
            #       [self.ui.cen3_sb, self.ui.cen3l_sb, self.ui.cen3h_sb],
            #       [self.ui.sigma3_sb, self.ui.sigma3l_sb, self.ui.sigma3h_sb]],\
            #               [[self.ui.amp4_sb, self.ui.amp4l_sb, self.ui.amp4h_sb],
            #       [self.ui.cen4_sb, self.ui.cen4l_sb, self.ui.cen4h_sb],
            #       [self.ui.sigma4_sb, self.ui.sigma4l_sb, self.ui.sigma4h_sb]],\
            #               [[self.ui.amp5_sb, self.ui.amp5l_sb, self.ui.amp5h_sb],
            #       [self.ui.cen5_sb, self.ui.cen5l_sb, self.ui.cen5h_sb],
            #       [self.ui.sigma5_sb, self.ui.sigma5l_sb, self.ui.sigma5h_sb]], \
            #               [[self.ui.amp6_sb, self.ui.amp6l_sb, self.ui.amp6h_sb],
            #                [self.ui.cen6_sb, self.ui.cen6l_sb, self.ui.cen6h_sb],
            #                [self.ui.sigma6_sb, self.ui.sigma6l_sb, self.ui.sigma6h_sb]], \
            #               [[self.ui.amp7_sb, self.ui.amp7l_sb, self.ui.amp7h_sb],
            #                [self.ui.cen7_sb, self.ui.cen7l_sb, self.ui.cen7h_sb],
            #                [self.ui.sigma7_sb, self.ui.sigma7l_sb, self.ui.sigma7h_sb]], \
            #               [[self.ui.amp8_sb, self.ui.amp8l_sb, self.ui.amp8h_sb],
            #                [self.ui.cen8_sb, self.ui.cen8l_sb, self.ui.cen8h_sb],
            #                [self.ui.sigma8_sb, self.ui.sigma8l_sb, self.ui.sigma8h_sb]]
            for i in range(8):
                for j in range(3):
                    for k in range(3):
                        constraints[i][j][k].setValue(temp[i][j][k])
            self.ui.fitreport_te.setText(self.fit_obj[self.ui.fit_range_cb.currentText()].fit_result)
        except KeyError:
            pass

    def checked_cons(self):
        checked = [self.ui.peak1_box.isChecked(), self.ui.peak2_box.isChecked(), self.ui.peak3_box.isChecked(),
                   self.ui.peak4_box.isChecked(), self.ui.peak5_box.isChecked(), self.ui.peak6_box.isChecked(),
                   self.ui.peak7_box.isChecked(), self.ui.peak8_box.isChecked()]
        cons = [[self.ui.amp1_sb.value(), self.ui.amp1l_sb.value(), self.ui.amp1h_sb.value()],
                [self.ui.cen1_sb.value(), self.ui.cen1l_sb.value(), self.ui.cen1h_sb.value()],
                [self.ui.sigma1_sb.value(), self.ui.sigma1l_sb.value(), self.ui.sigma1h_sb.value()]], [[self.ui.amp2_sb.value(), self.ui.amp2l_sb.value(), self.ui.amp2h_sb.value()],[self.ui.cen2_sb.value(), self.ui.cen2l_sb.value(), self.ui.cen2h_sb.value()],[self.ui.sigma2_sb.value(), self.ui.sigma2l_sb.value(), self.ui.sigma2h_sb.value()]], [[self.ui.amp3_sb.value(), self.ui.amp3l_sb.value(), self.ui.amp3h_sb.value()],
                   [self.ui.cen3_sb.value(), self.ui.cen3l_sb.value(), self.ui.cen3h_sb.value()],
                   [self.ui.sigma3_sb.value(), self.ui.sigma3l_sb.value(), self.ui.sigma3h_sb.value()]], [
                   [self.ui.amp4_sb.value(), self.ui.amp4l_sb.value(), self.ui.amp4h_sb.value()],
                   [self.ui.cen4_sb.value(), self.ui.cen4l_sb.value(), self.ui.cen4h_sb.value()],
                   [self.ui.sigma4_sb.value(), self.ui.sigma4l_sb.value(), self.ui.sigma4h_sb.value()]], [
                   [self.ui.amp5_sb.value(), self.ui.amp5l_sb.value(), self.ui.amp5h_sb.value()],
                   [self.ui.cen5_sb.value(), self.ui.cen5l_sb.value(), self.ui.cen5h_sb.value()],
                   [self.ui.sigma5_sb.value(), self.ui.sigma5l_sb.value(), self.ui.sigma5h_sb.value()]], [
                   [self.ui.amp6_sb.value(), self.ui.amp6l_sb.value(), self.ui.amp6h_sb.value()],
                   [self.ui.cen6_sb.value(), self.ui.cen6l_sb.value(), self.ui.cen6h_sb.value()],
                   [self.ui.sigma6_sb.value(), self.ui.sigma6l_sb.value(), self.ui.sigma6h_sb.value()]], [
                   [self.ui.amp7_sb.value(), self.ui.amp7l_sb.value(), self.ui.amp7h_sb.value()],
                   [self.ui.cen7_sb.value(), self.ui.cen7l_sb.value(), self.ui.cen7h_sb.value()],
                   [self.ui.sigma7_sb.value(), self.ui.sigma7l_sb.value(), self.ui.sigma7h_sb.value()]], [
                   [self.ui.amp8_sb.value(), self.ui.amp8l_sb.value(), self.ui.amp8h_sb.value()],
                   [self.ui.cen8_sb.value(), self.ui.cen8l_sb.value(), self.ui.cen8h_sb.value()],
                   [self.ui.sigma8_sb.value(), self.ui.sigma8l_sb.value(), self.ui.sigma8h_sb.value()]]
        nums_checked = []
        for i in range(len(checked)):
            if checked[i]:
                nums_checked.append(i)
        constraints = [[self.ui.amp1_sb, self.ui.amp1l_sb, self.ui.amp1h_sb],
                       [self.ui.cen1_sb, self.ui.cen1l_sb, self.ui.cen1h_sb],
                       [self.ui.sigma1_sb, self.ui.sigma1l_sb, self.ui.sigma1h_sb]], [
                          [self.ui.amp2_sb, self.ui.amp2l_sb, self.ui.amp2h_sb],
                          [self.ui.cen2_sb, self.ui.cen2l_sb, self.ui.cen2h_sb],
                          [self.ui.sigma2_sb, self.ui.sigma2l_sb, self.ui.sigma2h_sb]], [
                          [self.ui.amp3_sb, self.ui.amp3l_sb, self.ui.amp3h_sb],
                          [self.ui.cen3_sb, self.ui.cen3l_sb, self.ui.cen3h_sb],
                          [self.ui.sigma3_sb, self.ui.sigma3l_sb, self.ui.sigma3h_sb]], [
                          [self.ui.amp4_sb, self.ui.amp4l_sb, self.ui.amp4h_sb],
                          [self.ui.cen4_sb, self.ui.cen4l_sb, self.ui.cen4h_sb],
                          [self.ui.sigma4_sb, self.ui.sigma4l_sb, self.ui.sigma4h_sb]], [
                          [self.ui.amp5_sb, self.ui.amp5l_sb, self.ui.amp5h_sb],
                          [self.ui.cen5_sb, self.ui.cen5l_sb, self.ui.cen5h_sb],
                          [self.ui.sigma5_sb, self.ui.sigma5l_sb, self.ui.sigma5h_sb]], [
                          [self.ui.amp6_sb, self.ui.amp6l_sb, self.ui.amp6h_sb],
                          [self.ui.cen6_sb, self.ui.cen6l_sb, self.ui.cen6h_sb],
                          [self.ui.sigma6_sb, self.ui.sigma6l_sb, self.ui.sigma6h_sb]], [
                          [self.ui.amp7_sb, self.ui.amp7l_sb, self.ui.amp7h_sb],
                          [self.ui.cen7_sb, self.ui.cen7l_sb, self.ui.cen7h_sb],
                          [self.ui.sigma7_sb, self.ui.sigma7l_sb, self.ui.sigma7h_sb]], [
                          [self.ui.amp8_sb, self.ui.amp8l_sb, self.ui.amp8h_sb],
                          [self.ui.cen8_sb, self.ui.cen8l_sb, self.ui.cen8h_sb],
                          [self.ui.sigma8_sb, self.ui.sigma8l_sb, self.ui.sigma8h_sb]]
        return checked, cons, nums_checked, constraints

    def initial_fit(self):
        self.removing_xps_lines()
        checked, cons, nums_checked,_ = self.checked_cons()
        obj = self.fit_obj[self.ui.fit_range_cb.currentText()]
        result = obj.initial_plot(checked, cons,self.ui.hold_vgratio_box.isChecked(), self.ui.weight_dsb.value())
        ApplicationSettings.ALL_DATA_PLOTTED[self.ui.fit_range_cb.currentText() + '_init'] = \
            self.main_window.ax.plot(obj.x_data, result + obj.shirley[1], 'k--',
                                     label=self.ui.fit_range_cb.currentText() + '_init')
        self.main_window.canvas.draw()

    def xps_basic(self):
        limits = self.main_window.ax.get_xlim()
        if limits[1] > limits[0]:
            self.main_window.ax.set_xlim(self.main_window.ax.get_xlim()[::-1])
        self.main_window.ax.set_xlabel('B. E. (eV)')
        self.main_window.ax.set_ylabel('Counts')
        leg = self.main_window.ax.legend(loc='best')
        leg.set_draggable(True)
        self.main_window.fig.tight_layout()
        self.main_window.canvas.draw()

    def fit_fun(self):
        self.removing_xps_lines()
        checked, cons, nums_checked, constraints = self.checked_cons()
        # constraints = [[self.ui.amp1_sb, self.ui.amp1l_sb, self.ui.amp1h_sb],
        #                [self.ui.cen1_sb, self.ui.cen1l_sb, self.ui.cen1h_sb],
        #                [self.ui.sigma1_sb, self.ui.sigma1l_sb, self.ui.sigma1h_sb]], [[self.ui.amp2_sb, self.ui.amp2l_sb, self.ui.amp2h_sb],
        #                [self.ui.cen2_sb, self.ui.cen2l_sb, self.ui.cen2h_sb],
        #                [self.ui.sigma2_sb, self.ui.sigma2l_sb, self.ui.sigma2h_sb]], [[self.ui.amp3_sb, self.ui.amp3l_sb, self.ui.amp3h_sb],
        #                [self.ui.cen3_sb, self.ui.cen3l_sb, self.ui.cen3h_sb],
        #                [self.ui.sigma3_sb, self.ui.sigma3l_sb, self.ui.sigma3h_sb]], [[self.ui.amp4_sb, self.ui.amp4l_sb, self.ui.amp4h_sb],
        #                [self.ui.cen4_sb, self.ui.cen4l_sb, self.ui.cen4h_sb],
        #                [self.ui.sigma4_sb, self.ui.sigma4l_sb, self.ui.sigma4h_sb]], [[self.ui.amp5_sb, self.ui.amp5l_sb, self.ui.amp5h_sb],
        #                [self.ui.cen5_sb, self.ui.cen5l_sb, self.ui.cen5h_sb],
        #                [self.ui.sigma5_sb, self.ui.sigma5l_sb, self.ui.sigma5h_sb]], [[self.ui.amp6_sb, self.ui.amp6l_sb, self.ui.amp6h_sb],
        #                [self.ui.cen6_sb, self.ui.cen6l_sb, self.ui.cen6h_sb],
        #                [self.ui.sigma6_sb, self.ui.sigma6l_sb, self.ui.sigma6h_sb]],[[self.ui.amp7_sb, self.ui.amp7l_sb, self.ui.amp7h_sb],
        #                [self.ui.cen7_sb, self.ui.cen7l_sb, self.ui.cen7h_sb],
        #                [self.ui.sigma7_sb, self.ui.sigma7l_sb, self.ui.sigma7h_sb]],[[self.ui.amp8_sb, self.ui.amp8l_sb, self.ui.amp8h_sb],
        #                [self.ui.cen8_sb, self.ui.cen8l_sb, self.ui.cen8h_sb],
        #                [self.ui.sigma8_sb, self.ui.sigma8l_sb, self.ui.sigma8h_sb]]

        obj = self.fit_obj[self.ui.fit_range_cb.currentText()]
        result = obj.fit(checked, cons,self.ui.hold_vgratio_box.isChecked(), self.ui.weight_dsb.value())
        comps = result.eval_components()
        ApplicationSettings.ALL_DATA_PLOTTED[self.ui.fit_range_cb.currentText()+'_fit'] = \
            self.main_window.ax.plot(obj.x_data, result.best_fit+obj.shirley[1], 'k--', label=self.ui.fit_range_cb.currentText()+'_fit')
        self.ui.fitreport_te.setText(result.fit_report())
        if self.ui.sd_box.isChecked():
            try:
                dely = result.eval_uncertainty(sigma=3)
                ApplicationSettings.ALL_DATA_PLOTTED['Verr_' + self.ui.fit_range_cb.currentText()] = \
                    self.main_window.ax.fill_between(obj.x_data, result.best_fit - dely + obj.shirley[1],
                                                     result.best_fit + dely + obj.shirley[1], color="#ABABAB",
                                                     label='3-$\sigma$ uncertainty band')
            except TypeError:
                pass
        for i in nums_checked:
            constraints[i][0][0].setValue(result.params['p%s_amplitude' % str(i)].value)
            constraints[i][1][0].setValue(result.params['p%s_center' % str(i)].value)
            constraints[i][2][0].setValue(result.params['p%s_sigma' % str(i)].value)
            obj.peak_constraints[i][0][0] = result.params['p%s_amplitude' % str(i)].value
            obj.peak_constraints[i][1][0] = result.params['p%s_center' % str(i)].value
            obj.peak_constraints[i][2][0] = result.params['p%s_sigma' % str(i)].value
            if self.ui.plot_what_box.isChecked():
                ApplicationSettings.ALL_DATA_PLOTTED['V%s_' % str(i)+self.ui.fit_range_cb.currentText()] = \
                    self.main_window.ax.plot(obj.x_data,  obj.shirley[1]+ comps['p%s_' % str(i)], 'k--', label='_V1')
        self.main_window.canvas.draw()

    def clear_fit_objs(self):
        self.ui.fit_range_cb.clear()
        self.fit_obj = {}

    def removing_xps_lines(self):
        try:
            line0 = ApplicationSettings.ALL_DATA_PLOTTED[self.ui.fit_range_cb.currentText() + '_fit']
            self.main_window.ax.lines.remove(line0[0])
        except KeyError:
            pass
        except ValueError:
            pass
        for i in range(8):
            try:
                line0 = ApplicationSettings.ALL_DATA_PLOTTED['V%s_' % str(i)+self.ui.fit_range_cb.currentText()]
                self.main_window.ax.lines.remove(line0[0])
            except KeyError:
                pass
            except ValueError:
                pass
        try:
            line1 = ApplicationSettings.ALL_DATA_PLOTTED[self.ui.fit_range_cb.currentText() + '_init']
            self.main_window.ax.lines.remove(line1[0])
        except KeyError:
            pass
        except ValueError:
            pass
        try:
            poly = ApplicationSettings.ALL_DATA_PLOTTED['Verr_'+self.ui.fit_range_cb.currentText()]
            poly.remove()
            ApplicationSettings.ALL_DATA_PLOTTED.pop('Verr_'+self.ui.fit_range_cb.currentText())
            del poly
        except KeyError:
            pass
        except ValueError:
            pass
        self.main_window.canvas.draw()


class Fit_Object(object):
    def __init__(self, x_data, y_data, minimum, maximum):
        self.peak_constraints = []
        self.constraints = []
        self.peak_type = {}
        self.peak_fitted_values = {}
        self.shirley = None
        self.x_data = x_data
        self.y_data = y_data
        self.shirley_in_range(minimum, maximum)
        self.mini = minimum
        self.maxi = maximum
        self.init_constraints(minimum, maximum)
        self.fit_result = None

    def init_constraints(self, minimum, maximum):
        middle = minimum + (maximum-minimum)/2
        centers = [middle for i in range(8)]
        for i in range(8):
            self.peak_constraints.append([[5000, 0, 999999], [centers[i], minimum, maximum],[1,.0001,10]])

    def shirley_calculate(self, x, y, tol=1e-5, maxit=15):
        """ S = specs.shirley_calculate(x,y, tol=1e-5, maxit=10)
        Calculate the best auto-Shirley background S for a dataset (x,y). Finds the biggest peak
        and then uses the minimum value either side of this peak as the terminal points of the
        Shirley background.
        The tolerance sets the convergence criterion, maxit sets the maximum number
        of iterations.
        """

        # Make sure we've been passed arrays and not lists.
        x = np.array(x)
        y = np.array(y)

        # Sanity check: Do we actually have data to process here?
        if not (x.any() and y.any()):
            print("specs.shirley_calculate: One of the arrays x or y is empty. Returning zero background.")
            return np.zeros(x.shape)

        # Next ensure the energy values are *decreasing* in the array,
        # if not, reverse them.
        if x[0] < x[-1]:
            is_reversed = True
            x = x[::-1]
            y = y[::-1]
        else:
            is_reversed = False

        # Locate the biggest peak.
        maxidx = abs(y - np.amax(y)).argmin()

        # It's possible that maxidx will be 0 or -1. If that is the case,
        # we can't use this algorithm, we return a zero background.
        if maxidx == 0 or maxidx >= len(y) - 1:
            print("specs.shirley_calculate: Boundaries too high for algorithm: returning a zero background.")
            return np.zeros(x.shape)

        # Locate the minima either side of maxidx.
        lmidx = abs(y[0:maxidx] - np.amin(y[0:maxidx])).argmin()
        rmidx = abs(y[maxidx:] - np.amin(y[maxidx:])).argmin() + maxidx
        xl = x[lmidx]
        yl = y[lmidx]
        xr = x[rmidx]
        yr = y[rmidx]

        # Max integration index
        imax = rmidx - 1

        # Initial value of the background shape B. The total background S = yr + B,
        # and B is equal to (yl - yr) below lmidx and initially zero above.
        B = np.zeros(x.shape)
        B[:lmidx] = yl - yr
        Bnew = B.copy()

        it = 0
        while it < maxit:
            # if DEBUG:
            #     print("Shirley iteration: ", it)
            # Calculate new k = (yl - yr) / (int_(xl)^(xr) J(x') - yr - B(x') dx')
            ksum = 0.0
            for i in range(lmidx, imax):
                ksum += (x[i] - x[i + 1]) * 0.5 * (y[i] + y[i + 1]
                                                   - 2 * yr - B[i] - B[i + 1])
            k = (yl - yr) / ksum
            # Calculate new B
            for i in range(lmidx, rmidx):
                ysum = 0.0
                for j in range(i, imax):
                    ysum += (x[j] - x[j + 1]) * 0.5 * (y[j] +
                                                       y[j + 1] - 2 * yr - B[j] - B[j + 1])
                Bnew[i] = k * ysum
            # If Bnew is close to B, exit.
            if norm(Bnew - B) < tol:
                B = Bnew.copy()
                break
            else:
                B = Bnew.copy()
            it += 1

        if it >= maxit:
            print("specs.shirley_calculate: Max iterations exceeded before convergence.")
        if is_reversed:
            return (yr + B)[::-1]
        else:
            return yr + B

    def shirley_in_range(self, minimum, maximum):
        lims = [find_nearest(self.x_data, minimum), find_nearest(self.x_data, maximum)]
        self.x_data = self.x_data[lims[1]:lims[0]]
        self.y_data = self.y_data[lims[1]:lims[0]]
        self.shirley = [self.x_data,self.shirley_calculate(self.x_data,self.y_data)]

    def fit(self, checked, cons, vghold, vgratio):
        self.update_constraints(cons)
        line_shape_mods = [PseudoVoigtModel(prefix='p0_'), PseudoVoigtModel(prefix='p1_'),
                           PseudoVoigtModel(prefix='p2_'), PseudoVoigtModel(prefix='p3_'),
                           PseudoVoigtModel(prefix='p4_'), PseudoVoigtModel(prefix='p5_'),
                           PseudoVoigtModel(prefix='p6_'), PseudoVoigtModel(prefix='p7_')]
        cur_mods = []
        checked_peaks = []
        params = Parameters()
        # add with tuples: (NAME VALUE VARY MIN  MAX  EXPR  BRUTE_STEP)
        for x in range(8):
            if checked[x]:
                params.add_many(('p%s_amplitude' % str(x), self.peak_constraints[x][0][0], True, self.peak_constraints[x][0][1], self.peak_constraints[x][0][2]),
                                ('p%s_center' % str(x), self.peak_constraints[x][1][0], True, self.peak_constraints[x][1][1], self.peak_constraints[x][1][2]),
                                ('p%s_sigma' % str(x), self.peak_constraints[x][2][0], True, self.peak_constraints[x][2][1], self.peak_constraints[x][2][2]),
                                ('p%s_fraction' % str(x), vgratio, vghold))
                checked_peaks.append(x)
                cur_mods.append(line_shape_mods[x])
        if len(checked_peaks) == 1:
            mod = cur_mods[0]
        elif len(checked_peaks) == 2:
            mod = cur_mods[0] + cur_mods[1]
        elif len(checked_peaks) == 3:
            mod = cur_mods[0] + cur_mods[1] + cur_mods[2]
        elif len(checked_peaks) == 4:
            mod = cur_mods[0] + cur_mods[1] + cur_mods[2] + cur_mods[3]
        elif len(checked_peaks) == 5:
            mod = cur_mods[0] + cur_mods[1] + cur_mods[2] + cur_mods[3] + cur_mods[4]
        elif len(checked_peaks) == 6:
            mod = cur_mods[0] + cur_mods[1] + cur_mods[2] + cur_mods[3] + cur_mods[4] + cur_mods[5]
        elif len(checked_peaks) == 7:
            mod = cur_mods[0] + cur_mods[1] + cur_mods[2] + cur_mods[3] + cur_mods[4] + cur_mods[5]+ cur_mods[6]
        elif len(checked_peaks) == 8:
            mod = cur_mods[0] + cur_mods[1] + cur_mods[2] + cur_mods[3] + cur_mods[4]+ cur_mods[5]+ cur_mods[6]+ cur_mods[7]
        # add with tuples: (NAME VALUE VARY MIN  MAX  EXPR  BRUTE_STEP)
        result = mod.fit(self.y_data-self.shirley[1], params, x=self.x_data)
        # comps = result.eval_components()
        self.fit_result = result.fit_report()
        return result

    def update_constraints(self, constraints):
        for i in range(5):
            for j in range(3):
                for k in range(3):
                    self.peak_constraints[i][j][k] = constraints[i][j][k]

    def initial_plot(self, checked, cons,vghold, vgratio):
        self.update_constraints(cons)
        line_shape_mods = [PseudoVoigtModel(prefix='p0_'), PseudoVoigtModel(prefix='p1_'),
                           PseudoVoigtModel(prefix='p2_'),PseudoVoigtModel(prefix='p3_'),
                           PseudoVoigtModel(prefix='p4_'),PseudoVoigtModel(prefix='p5_'),
                           PseudoVoigtModel(prefix='p6_'),PseudoVoigtModel(prefix='p7_')]
        cur_mods = []
        checked_peaks = []
        params = Parameters()
        # add with tuples: (NAME VALUE VARY MIN  MAX  EXPR  BRUTE_STEP)
        for x in range(8):
            if checked[x]:
                params.add_many(('p%s_amplitude' % str(x), self.peak_constraints[x][0][0], True,
                                 self.peak_constraints[x][0][1], self.peak_constraints[x][0][2]),
                                ('p%s_center' % str(x), self.peak_constraints[x][1][0], True,
                                 self.peak_constraints[x][1][1], self.peak_constraints[x][1][2]),
                                ('p%s_sigma' % str(x), self.peak_constraints[x][2][0], True,
                                 self.peak_constraints[x][2][1], self.peak_constraints[x][2][2]),
                                ('p%s_fraction' % str(x), vgratio, vghold))
                checked_peaks.append(x)
                cur_mods.append(line_shape_mods[x])
        if len(checked_peaks) == 1:
            mod = cur_mods[0]
        elif len(checked_peaks) == 2:
            mod = cur_mods[0] + cur_mods[1]
        elif len(checked_peaks) == 3:
            mod = cur_mods[0] + cur_mods[1] + cur_mods[2]
        elif len(checked_peaks) == 4:
            mod = cur_mods[0] + cur_mods[1] + cur_mods[2] + cur_mods[3]
        elif len(checked_peaks) == 5:
            mod = cur_mods[0] + cur_mods[1] + cur_mods[2] + cur_mods[3] + cur_mods[4]
        elif len(checked_peaks) == 6:
            mod = cur_mods[0] + cur_mods[1] + cur_mods[2] + cur_mods[3] + cur_mods[4] + cur_mods[5]
        elif len(checked_peaks) == 7:
            mod = cur_mods[0] + cur_mods[1] + cur_mods[2] + cur_mods[3] + cur_mods[4] + cur_mods[5] + cur_mods[6]
        elif len(checked_peaks) == 8:
            mod = cur_mods[0] + cur_mods[1] + cur_mods[2] + cur_mods[3] + cur_mods[4] + cur_mods[5] + cur_mods[6] + \
                  cur_mods[7]
        # add with tuples: (NAME VALUE VARY MIN  MAX  EXPR  BRUTE_STEP)
        result = mod.fit(self.y_data - self.shirley[1], params, x=self.x_data)
        # comps = result.eval_components()
        # self.fit_result = result.fit_report()
        return result.init_fit

