from Ui_Files.DockWidgets.Py.dw_FTIR import Ui_DockWidget
from gui_elements.RC_Fucntions import *
import glob
from scipy.signal import savgol_filter
from lmfit.models import VoigtModel, ConstantModel, LinearModel
from lmfit import Model, Parameters
from Ui_Files.Dialogs.simple_treeWidget_dialog import Ui_Dialog as twDialog_ui
from gui_elements.plotting_functions import baseline_als, find_nearest
from matplotlib.widgets import SpanSelector
from dataclasses import dataclass

class FTIR_view(QtWidgets.QDockWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.ui = Ui_DockWidget()
        self.ui.setupUi(self)

        self._init_vars()
        self._init_widgets()
        self._init_UI()

    def _init_vars(self):
        self.current_data_container = None
        self.sub = None
        self.diff = None
        self.model = None
        self.data = None
        self.x_data = None
        self.y_data = None
        self.fit_name = None
        self.data_list = []
        # self.constraints = np.asarray(
        #     [[10, -1000, 1000, 3700, 400, 4000, 50, 1, 400], [10, -1000, 2900, 285, 400, 4000, 50, 1, 400],
        #      [1, -1000, 1000, 2890, 400, 4000, 50, 1, 400], [10, -1000, 1000, 1215, 400, 4000, 50, 1, 400],
        #      [10, -1000, 1000, 900, 400, 4000, 50, 1, 400]])
        # for row in range(9):
        #     for column in range(5):
        #         self.ui.tableWidget_2.setItem(row, column, QtWidgets.QTableWidgetItem(str(self.constraints[column][row])))

        self.fit_obj = {}

    def _init_widgets(self):
        self.tree_view = self.ui.FTIR_treeView
        self.context_menu = QtWidgets.QMenu(self)
        # Create context menu
        rc_browser_options(self)
        self.colors = [self.ui.int_color_1, self.ui.int_color_2,self.ui.int_color_3, self.ui.int_color_4, self.ui.int_color_5]
        for i in self.colors:
            i.setStyleSheet("background-color: {}".format('#ff0000'))
            i.setText('#ff0000')

    def _init_UI(self):
        self.model = QtWidgets.QFileSystemModel()
        self.model.setRootPath('')

        self.tree_view.setModel(self.model)
        self.tree_view.setSortingEnabled(True)

        # self.tree_view.sortByColumn(True)
        self.tree_view.setRootIndex(self.model.index(self.main_window.settings.value('FTIR_PATH')))
        self.tree_view.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)

        self.tree_view.setModel(self.model)
        self.tree_view.installEventFilter(self)
        self.tree_view.setColumnWidth(0, 200)

        self.ui.smooth_pb.clicked.connect(lambda: self.smooth())
        self.ui.integrate_pb.clicked.connect(lambda: self.integrate())

        self.ui.ir_range_cb.currentIndexChanged.connect(lambda: self.fit_range_changed())
        self.ui.fit_pb.clicked.connect(lambda: self.fit_fun())
        self.ui.fit_init_pb.clicked.connect(lambda: self.initial_fit())
        # self.ui.tableWidget_2.cellChanged.connect(lambda: self.save_constraints())
        # self.ui.selectdata_pb.clicked.connect(lambda: self.select_data())
        # self.ui.baseline_pb.clicked.connect(lambda: self.baseline_data())
        # self.ui.integratemode_rb.toggled.connect(self.integrate_mode)
        self.ui.integratemode_rb.toggled.connect(self.select_integrate_range)
        self.ui.select_ir_range_cb.toggled.connect(self.select_ir_range)
        self.ui.sub_dir_pb.clicked.connect(lambda: self.ir_plot('sub', self.ui.plotside_cb.currentText()))
        self.ui.diff_2_pb.clicked.connect(lambda: self.ir_plot('diff2',self.ui.plotside_cb.currentText()))
        self.ui.diff_dir_pb.clicked.connect(lambda: self.ir_plot('diff',self.ui.plotside_cb.currentText()))
        self.ui.abs_dir_pb.clicked.connect(lambda: self.ir_plot('abs',self.ui.plotside_cb.currentText()))
        self.ui.clear_fit_pb.clicked.connect(lambda: self.clear_fit_objs())
        self.ui.spectra_pb.clicked.connect(lambda: self.ir_plot('spectra',self.ui.plotside_cb.currentText()))

        self.ui.int_color_1.clicked.connect(lambda: color_test(self.ui.int_color_1))
        self.ui.int_color_2.clicked.connect(lambda: color_test(self.ui.int_color_2))
        self.ui.int_color_3.clicked.connect(lambda: color_test(self.ui.int_color_3))
        self.ui.int_color_4.clicked.connect(lambda: color_test(self.ui.int_color_4))
        self.ui.int_color_5.clicked.connect(lambda: color_test(self.ui.int_color_5))
        # self.ui.fit2_pb.clicked.connect(lambda: self.fitting_function_2())
        # self.ui.select_data_pb.clicked.connect(lambda: self.select_data())
        # self.ui.fit_init_pb.clicked.connect(lambda: self.plot_init_2())

    def eventFilter(self, object, event):
        # For right click events
        if event.type() == QtCore.QEvent.ContextMenu:
            self.context_menu.exec_(self.mapToGlobal(event.pos()))
        return False

    def ir_plot(self, type, axis):
        self.data_list = []
        path = self.model.filePath(self.tree_view.currentIndex())
        head, tail = os.path.split(path)
        if axis == 'Left Ax':
            ax = self.main_window.ax
        elif axis == 'Right Ax':
            self.main_window.ax_2 = self.main_window.ax.twinx()
            ax = self.main_window.ax_2
        try:
            if type == 'spectra':
                try:
                    temp = pd.read_csv(path,delimiter=',', skiprows=self.ui.skiprows_sb.value())
                    self.data = temp.to_numpy().T
                    ApplicationSettings.ALL_DATA_PLOTTED[tail] = ax.plot(
                        self.data[0], self.data[1], label=tail)
                except IndexError:
                    temp = pd.read_csv(path, delimiter='\t', skiprows=self.ui.skiprows_sb.value())
                    self.data = temp.to_numpy().T
                    ApplicationSettings.ALL_DATA_PLOTTED[tail] = ax.plot(
                        self.data[0], self.data[1], label=tail)
            elif type == 'sub':
                if os.path.isdir(path):
                    csv_list = sorted(glob.glob(path + '/*CSV'))
                    data = []
                    for csv in csv_list:
                        data.append(np.genfromtxt(csv, delimiter=',').T)
                    sub_list = [data[0][0]]
                    for l in range(len(data) - 1):
                        length = len(data[0][0])
                        sub_list.append(data[l + 1][1][:length] - data[0][1][:length])
                    self.sub = sub_list
                    for i in range(0,len(self.sub)-1,self.ui.skip_sb.value()+1):
                        ApplicationSettings.ALL_DATA_PLOTTED['Sub_'+str(i)] = \
                            ax.plot(self.sub[0],self.sub[i+1],label='Sub_'+str(i))
            elif type == 'diff':
                if os.path.isdir(path):
                    csv_list = sorted(glob.glob(path + '/*CSV'))

                    data = []
                    for csv in csv_list:
                        temp_data = pd.read_csv(csv, delimiter=',')
                        temp_data = temp_data.dropna(how='any')
                        data.append(temp_data.to_numpy().T)
                    sub_list = [data[0][0]]
                    for l in range(len(data) - 1):
                        length = len(data[0][0])
                        if len(data[l + 1][1][:length]) == len(data[l][1][:length]):
                            try:
                                sub_list.append(data[l + 1][1][:length] - data[l][1][:length])
                            except TypeError:
                                print('problem with unequal lengths')
                    self.diff = sub_list

                    for i in range(0,len(self.diff)-1,self.ui.skip_sb.value()+1):
                        try:
                            ApplicationSettings.ALL_DATA_PLOTTED['Diff_'+str(i)] = \
                                ax.plot(self.diff[0],self.diff[i+1],label='Diff_'+str(i))
                        except ValueError:
                            print('not the same size thing')
            elif type == 'abs':
                if os.path.isdir(path):
                    csv_list = sorted(glob.glob(path + '/*CSV'))
                    data = []
                    for csv in csv_list:
                        data.append(np.genfromtxt(csv, delimiter=',').T)
                    self.data = [data[0][0]]
                    for i in range(0,len(data),self.ui.skip_sb.value()+1):
                        self.data.append(data[i][1])
                    for j in range(0,len(self.data)-1,self.ui.skip_sb.value()+1):
                        ApplicationSettings.ALL_DATA_PLOTTED['IR_'+str(j)] = \
                            ax.plot(self.data[0],self.data[j+1])
            elif type == 'diff2':

                paths = [self.model.filePath(self.tree_view.selectedIndexes()[0]),
                         self.model.filePath(self.tree_view.selectedIndexes()[5])]
                temp1 = pd.read_csv(paths[0],delimiter=',').to_numpy().T
                temp2 = pd.read_csv(paths[1],delimiter=',').to_numpy().T
                self.data = [temp1[0],temp1[1]-temp2[1]]
                ApplicationSettings.ALL_DATA_PLOTTED[tail] = ax.plot(
                    self.data[0], self.data[1], label=tail)
            self.ir_basic()
        except PermissionError:
            msg = QtWidgets.QMessageBox()
            msg.setText('Aint Nottin Her')
            msg.exec_()
        except IndexError:
            msg = QtWidgets.QMessageBox()
            msg.setText('Aint Nottin Here')
            msg.exec_()

    def ir_basic(self):
        self.main_window.ax.set_xlim(self.ui.xmin.value(), self.ui.xmax.value())
        limits = self.main_window.ax.get_xlim()
        if limits[1] > limits[0]:
            self.main_window.ax.set_xlim(self.main_window.ax.get_xlim()[::-1])
        self.main_window.ax.set_xlabel('Wavenumber (cm$^{-1}$)')
        self.main_window.ax.set_ylabel('Absorbance')
        self.main_window.fig.tight_layout()
        self.main_window.canvas.draw()

    def select_integrate_range(self,enabled):
        if enabled:
            self.span = SpanSelector(self.main_window.ax_1, self.on_int_select, 'horizontal', useblit=False,
                                     rectprops=dict(alpha=0.2, facecolor='blue'))
        else:
            del self.span

    def on_int_select(self, minimum, maximum):
        data_list = []
        for i in ApplicationSettings.ALL_DATA_PLOTTED.keys():
            print(ApplicationSettings.ALL_DATA_PLOTTED[i])
            if data_list == []:
                data_list.append(ApplicationSettings.ALL_DATA_PLOTTED[i][0]._xy.T[0])
            data_list.append(ApplicationSettings.ALL_DATA_PLOTTED[i][0]._xy.T[1])

        if self.ui.leftrightaxis_cb.currentText() == 'Left Axis':
            ax = self.main_window.ax
        elif self.ui.leftrightaxis_cb.currentText() == 'Right Axis':
            if self.main_window.ax_2 is None:
                self.main_window.ax_2 = self.main_window.ax.twinx()
            ax = self.main_window.ax_2
        inte = self.integrate_ir(data_list, minimum, maximum)
        if self.ui.xaxis_cb.currentText() == 'Ints':
            x = np.linspace(1, len(inte), len(inte))
        elif self.ui.xaxis_cb.currentText() == 'Half-Ints':
            x = np.linspace(0.5, len(inte) / 2, len(inte))
        ApplicationSettings.ALL_DATA_PLOTTED[
            'Int. ' + str(self.ui.min_sb.value()) + '-' + str(self.ui.max_sb.value())] = \
            ax.plot(x, inte, '.-', label='Int. ' + str(self.ui.min_sb.value()) + '-' + str(self.ui.max_sb.value()))
        self.main_window.canvas.draw()

    def integrate(self):
        # make list for the data
        # self.data_list = []
        # grab all the lines from applicationsettings. if it is a list of Line2D then flatten else grab the line
        # print(self.data_list)
        if self.data_list == []:
            for i in ApplicationSettings.ALL_DATA_PLOTTED.keys():
                if type(ApplicationSettings.ALL_DATA_PLOTTED[i]) == list:
                    if self.data_list == []:
                        self.data_list.append(ApplicationSettings.ALL_DATA_PLOTTED[i][0]._xy.T[0])
                    self.data_list.append(ApplicationSettings.ALL_DATA_PLOTTED[i][0]._xy.T[1])
                else:
                    try:
                        if self.data_list == []:
                            self.data_list.append(ApplicationSettings.ALL_DATA_PLOTTED[i]._xy.T[0])
                        self.data_list.append(ApplicationSettings.ALL_DATA_PLOTTED[i]._xy.T[1])
                    except AttributeError:
                        pass
            self.main_window.cleargraph()
        @dataclass()
        class data:
            ints_on = [self.ui.integrate1_cb.isChecked(), self.ui.integrate2_cb.isChecked(), self.ui.integrate3_cb.isChecked()
                , self.ui.integrate4_cb.isChecked(), self.ui.integrate5_cb.isChecked()]
            minimum_ints = [self.ui.min1_sb.value(),self.ui.min2_sb.value(),self.ui.min3_sb.value(),self.ui.min4_sb.value()
                ,self.ui.min5_sb.value()]
            maximum_ints = [self.ui.max1_sb.value(),self.ui.max2_sb.value(),self.ui.max3_sb.value(),self.ui.max4_sb.value()
            ,self.ui.max5_sb.value()]
            data = self.data_list
            colors = [self.ui.int_color_1, self.ui.int_color_2, self.ui.int_color_3, self.ui.int_color_4, self.ui.int_color_5]
        if self.ui.leftrightaxis_cb.currentText() == 'Left Axis':
            ax = self.main_window.ax
        elif self.ui.leftrightaxis_cb.currentText() == 'Right Axis':
            if self.main_window.ax_2 is None:
                self.main_window.ax_2 = self.main_window.ax.twinx()
            ax = self.main_window.ax_2

        ints_on = [self.ui.integrate1_cb.isChecked(), self.ui.integrate2_cb.isChecked(), self.ui.integrate3_cb.isChecked()
                   , self.ui.integrate4_cb.isChecked(), self.ui.integrate5_cb.isChecked()]

        minimum_ints = [self.ui.min1_sb.value(),self.ui.min2_sb.value(),self.ui.min3_sb.value(),self.ui.min4_sb.value()
                        ,self.ui.min5_sb.value()]
        maximum_ints = [self.ui.max1_sb.value(),self.ui.max2_sb.value(),self.ui.max3_sb.value(),self.ui.max4_sb.value()
                        ,self.ui.max5_sb.value()]

        for i in range(len(ints_on)):
            if ints_on[i] is True:
                # use the function integrate ir to take an array of wavenumber and data and integrate from min to max
                inte = self.integrate_ir(self.data_list,minimum_ints[i],maximum_ints[i])

                if self.ui.xaxis_cb.currentText() == 'Ints':
                    x = np.linspace(0, len(inte)-1, len(inte))
                elif self.ui.xaxis_cb.currentText() == 'Half-Ints':
                    x = np.linspace(0, (len(inte)-1)/2, len(inte))

                ApplicationSettings.ALL_DATA_PLOTTED[
                    'Int. ' + str(minimum_ints[i]) + '-' + str(maximum_ints[i])] = \
                    ax.plot(x, inte, '.-', label='Int. ' + str(minimum_ints[i]) + '-' + str(maximum_ints[i]),
                            color=self.colors[i].text(), markersize=self.ui.pointsize.value())
        self.main_window.canvas.draw()

    def integrate_ir(self, data, minimum, maximum):
        from scipy import integrate
        integral_list = []
        lim = [min(range(len(data[0])), key=lambda i: abs(data[0][i] - minimum)),
               min(range(len(data[0])), key=lambda i: abs(data[0][i] - maximum))]
        for numb in range(len(data) - 1):
            integral_list.append(integrate.trapz(data[numb + 1][lim[0]:lim[1]], data[0][lim[0]:lim[1]]))
        return integral_list

    def smooth(self):
        dict = ApplicationSettings.ALL_DATA_PLOTTED
        Key_List = []
        data_dict = {}
        @dataclass
        class smooth_data:
            data = []
            colors = []
            keys = []
            index = 0
        # try:
        #     for i in dict.keys():
        #         colors.append(dict[i][0]._color)
        #         if index == 0:
        #             data.append(dict[i][0]._xy.T[0])
        #             index += 1
        #         Key_List.append(i)
        #         data.append(dict[i][0]._xy.T[1])
        # except TypeError:
        #         try:
        #             for i in dict.keys():
        #                 colors.append(dict[i]._color)
        #                 if index == 0:
        #                     data.append(dict[i]._xy.T[0])
        #                     index += 1
        #                 Key_List.append(i)
        #                 data.append(dict[i]._xy.T[1])
        #         except TypeError:
        #             pass
        try:
            for i in dict.keys():
                smooth_data.colors.append(dict[i][0]._color)
                if smooth_data.index == 0:
                    smooth_data.data.append(dict[i][0]._xy.T[0])
                    smooth_data.index += 1
                smooth_data.keys.append(i)
                smooth_data.data.append(dict[i][0]._xy.T[1])
        except TypeError:
                try:
                    for i in dict.keys():
                        smooth_data.colors.append(dict[i]._color)
                        if smooth_data.index == 0:
                            smooth_data.data.append(dict[i]._xy.T[0])
                            smooth_data.index += 1
                        smooth_data.keys.append(i)
                        smooth_data.data.append(dict[i]._xy.T[1])
                except TypeError:
                    pass
        self.main_window.cleargraph()
        for i in range(len(smooth_data.keys)):
            ApplicationSettings.ALL_DATA_PLOTTED[smooth_data.keys[i]+'_sm'] = self.main_window.ax.plot(
                smooth_data.data[0],savgol_filter(smooth_data.data[i+1], self.ui.smooth_sb.value(), 3),
                color=smooth_data.colors[i], label=smooth_data.keys[i]+'_sm')
        self.ir_basic()
        self.main_window.fig.tight_layout()
        self.main_window.canvas.draw()

    def baseline_data(self):
        all_lines = ApplicationSettings.ALL_DATA_PLOTTED
        all_data = []
        for line in all_lines.keys():
            all_data.append(all_lines[line][0]._xy.T)
        x_data = all_data[0][0]
        self.main_window.cleargraph()
        for i in range(len(all_data)):
            baseline = baseline_als(all_data[i][1],self.ui.lambda_sb.value(),self.ui.p_sb.value())
            # ApplicationSettings.ALL_DATA_PLOTTED['Corr_IR_' + str(i)] = \
            #     self.main_window.ax.plot(x_data, all_data[i][1]-corrected, label='Corr_IR_' + str(i))
            ApplicationSettings.ALL_DATA_PLOTTED['data'] = \
                         self.main_window.ax.plot(x_data, all_data[i][1]-baseline,label='corrected')
            ApplicationSettings.ALL_DATA_PLOTTED['baseline'] = \
                self.main_window.ax.plot(x_data, baseline,label='baseline')
            ApplicationSettings.ALL_DATA_PLOTTED['raw'] = \
                self.main_window.ax.plot(x_data, all_data[i][1], label='raw')
        self.ir_basic()
        # need to first get the keys from the dict, than grab the ._xy from Line2D object, put through the baseline
        # correction, clear the data and then plot all the corrected baselines. Not too hard right?

    def select_ir_range(self,enabled):
        if enabled:
            self.span = SpanSelector(self.main_window.ax, self.on_select, 'horizontal', useblit=False,
                                     rectprops=dict(alpha=0.2, facecolor='blue'))
        else:
            del self.span

    def on_select(self,minimum, maximum):
        line = list(ApplicationSettings.ALL_DATA_PLOTTED.keys())
        if len(line) == 1:
            try:
                line = ApplicationSettings.ALL_DATA_PLOTTED[list(ApplicationSettings.ALL_DATA_PLOTTED.keys())[0]][0]
            except TypeError:
                line = ApplicationSettings.ALL_DATA_PLOTTED[list(ApplicationSettings.ALL_DATA_PLOTTED.keys())[0]]
            self.x_data = line._xy.T[0]
            self.y_data = line._xy.T[1]
            self.fit_obj[str(np.round(minimum, 1)) + '+' + str(np.round(maximum, 1))] = \
                IR_Fit_Object(self.x_data, self.y_data, minimum, maximum)
            self.ui.ir_range_cb.clear()
            self.ui.ir_range_cb.addItems([i for i in self.fit_obj.keys()])
            self.ui.ir_range_cb.setCurrentText(str(np.round(minimum, 1)) + '+' + str(np.round(maximum, 1)))
            self.ui.select_ir_range_cb.setChecked(False)
            # self.main_window.ax.set_xlim(maximum + 50, minimum - 50)
            # self.main_window.ax.set_ylim(auto=True)
            self.main_window.canvas.draw()
        else:
            mbox = QtWidgets.QMessageBox()
            mbox.setText('Please only have one spectra to fit!')
            mbox.exec_()
            self.ui.select_ir_range_cb.setChecked(False)

    def fit_range_changed(self):
        try:
            temp = self.fit_obj[self.ui.ir_range_cb.currentText()]
            self.main_window.ax.set_xlim(temp.maxi+50,temp.mini-50)
            self.main_window.ax.set_ylim(auto=True)
            _, _, _, constraints, holds, lin_pars = self.checked_cons()
            for i in range(8):
                for j in range(3):
                    for k in range(3):
                        constraints[i][j][k].setValue(temp.peak_constraints[i][j][k])
            self.ui.fit_results_te.setText(self.fit_obj[self.ui.ir_range_cb.currentText()].fit_result)
            self.main_window.canvas.draw()
        except KeyError:
            print('Change Failed')

    def checked_cons(self):
        checked = [self.ui.p1_cb.isChecked(), self.ui.p2_cb.isChecked(), self.ui.p3_cb.isChecked(),
                   self.ui.p4_cb.isChecked(), self.ui.p5_cb.isChecked(), self.ui.p6_cb.isChecked(),
                   self.ui.p7_cb.isChecked(), self.ui.p8_cb.isChecked()]

        cons = [[self.ui.p1_amp_sb.value(), self.ui.p1_ampl_sb.value(), self.ui.p1_amph_sb.value()],
                [self.ui.p1_cen_sb.value(), self.ui.p1_cenl_sb.value(), self.ui.p1_cenh_sb.value()],
                [self.ui.p1_sig_sb.value(), self.ui.p1_sigl_sb.value(), self.ui.p1_sigh_sb.value()]],\
               [[self.ui.p2_amp_sb.value(), self.ui.p2_ampl_sb.value(), self.ui.p2_amph_sb.value()],
                [self.ui.p2_cen_sb.value(), self.ui.p2_cenl_sb.value(), self.ui.p2_cenh_sb.value()],
                [self.ui.p2_sig_sb.value(), self.ui.p2_sigl_sb.value(), self.ui.p2_sigh_sb.value()]],\
               [[self.ui.p3_amp_sb.value(), self.ui.p3_ampl_sb.value(), self.ui.p3_amph_sb.value()],
                [self.ui.p3_cen_sb.value(), self.ui.p3_cenl_sb.value(), self.ui.p3_cenh_sb.value()],
                [self.ui.p3_sig_sb.value(), self.ui.p3_sigl_sb.value(), self.ui.p3_sigh_sb.value()]],\
               [[self.ui.p4_amp_sb.value(), self.ui.p4_ampl_sb.value(), self.ui.p4_amph_sb.value()],
                [self.ui.p4_cen_sb.value(), self.ui.p4_cenl_sb.value(), self.ui.p4_cenh_sb.value()],
                [self.ui.p4_sig_sb.value(), self.ui.p4_sigl_sb.value(), self.ui.p4_sigh_sb.value()]],\
               [[self.ui.p5_amp_sb.value(), self.ui.p5_ampl_sb.value(), self.ui.p5_amph_sb.value()],
                [self.ui.p5_cen_sb.value(), self.ui.p5_cenl_sb.value(), self.ui.p5_cenh_sb.value()],
                [self.ui.p5_sig_sb.value(), self.ui.p5_sigl_sb.value(), self.ui.p5_sigh_sb.value()]],\
               [[self.ui.p6_amp_sb.value(), self.ui.p6_ampl_sb.value(), self.ui.p6_amph_sb.value()],
                [self.ui.p6_cen_sb.value(), self.ui.p6_cenl_sb.value(), self.ui.p6_cenh_sb.value()],
                [self.ui.p6_sig_sb.value(), self.ui.p6_sigl_sb.value(), self.ui.p6_sigh_sb.value()]],\
               [[self.ui.p7_amp_sb.value(), self.ui.p7_ampl_sb.value(), self.ui.p7_amph_sb.value()],
                [self.ui.p7_cen_sb.value(), self.ui.p7_cenl_sb.value(), self.ui.p7_cenh_sb.value()],
                [self.ui.p7_sig_sb.value(), self.ui.p7_sigl_sb.value(), self.ui.p7_sigh_sb.value()]],\
               [[self.ui.p8_amp_sb.value(), self.ui.p8_ampl_sb.value(), self.ui.p8_amph_sb.value()],
                [self.ui.p8_cen_sb.value(), self.ui.p8_cenl_sb.value(), self.ui.p8_cenh_sb.value()],
                [self.ui.p8_sig_sb.value(), self.ui.p8_sigl_sb.value(), self.ui.p8_sigh_sb.value()]]

        nums_checked = []
        for i in range(len(checked)):
            if checked[i]:
                nums_checked.append(i)

        constraints = [[self.ui.p1_amp_sb, self.ui.p1_ampl_sb, self.ui.p1_amph_sb],
                [self.ui.p1_cen_sb, self.ui.p1_cenl_sb, self.ui.p1_cenh_sb],
                [self.ui.p1_sig_sb, self.ui.p1_sigl_sb, self.ui.p1_sigh_sb]],\
               [[self.ui.p2_amp_sb, self.ui.p2_ampl_sb, self.ui.p2_amph_sb],
                [self.ui.p2_cen_sb, self.ui.p2_cenl_sb, self.ui.p2_cenh_sb],
                [self.ui.p2_sig_sb, self.ui.p2_sigl_sb, self.ui.p2_sigh_sb]],\
               [[self.ui.p3_amp_sb, self.ui.p3_ampl_sb, self.ui.p3_amph_sb],
                [self.ui.p3_cen_sb, self.ui.p3_cenl_sb, self.ui.p3_cenh_sb],
                [self.ui.p3_sig_sb, self.ui.p3_sigl_sb, self.ui.p3_sigh_sb]],\
               [[self.ui.p4_amp_sb, self.ui.p4_ampl_sb, self.ui.p4_amph_sb],
                [self.ui.p4_cen_sb, self.ui.p4_cenl_sb, self.ui.p4_cenh_sb],
                [self.ui.p4_sig_sb, self.ui.p4_sigl_sb, self.ui.p4_sigh_sb]],\
               [[self.ui.p5_amp_sb, self.ui.p5_ampl_sb, self.ui.p5_amph_sb],
                [self.ui.p5_cen_sb, self.ui.p5_cenl_sb, self.ui.p5_cenh_sb],
                [self.ui.p5_sig_sb, self.ui.p5_sigl_sb, self.ui.p5_sigh_sb]],\
               [[self.ui.p6_amp_sb, self.ui.p6_ampl_sb, self.ui.p6_amph_sb],
                [self.ui.p6_cen_sb, self.ui.p6_cenl_sb, self.ui.p6_cenh_sb],
                [self.ui.p6_sig_sb, self.ui.p6_sigl_sb, self.ui.p6_sigh_sb]],\
               [[self.ui.p7_amp_sb, self.ui.p7_ampl_sb, self.ui.p7_amph_sb],
                [self.ui.p7_cen_sb, self.ui.p7_cenl_sb, self.ui.p7_cenh_sb],
                [self.ui.p7_sig_sb, self.ui.p7_sigl_sb, self.ui.p7_sigh_sb]],\
               [[self.ui.p8_amp_sb, self.ui.p8_ampl_sb, self.ui.p8_amph_sb],
                [self.ui.p8_cen_sb, self.ui.p8_cenl_sb, self.ui.p8_cenh_sb],
                [self.ui.p8_sig_sb, self.ui.p8_sigl_sb, self.ui.p8_sigh_sb]]

        holds = [[self.ui.p1_amp_hold.isChecked(),self.ui.p1_cen_hold.isChecked(),self.ui.p1_sigma_hold.isChecked()],
                 [self.ui.p2_amp_hold.isChecked(), self.ui.p2_cen_hold.isChecked(), self.ui.p2_sigma_hold.isChecked()],
                 [self.ui.p3_amp_hold.isChecked(), self.ui.p3_cen_hold.isChecked(), self.ui.p3_sigma_hold.isChecked()],
                 [self.ui.p4_amp_hold.isChecked(), self.ui.p4_cen_hold.isChecked(), self.ui.p4_sigma_hold.isChecked()],
                 [self.ui.p5_amp_hold.isChecked(), self.ui.p5_cen_hold.isChecked(), self.ui.p5_sigma_hold.isChecked()],
                 [self.ui.p6_amp_hold.isChecked(), self.ui.p6_cen_hold.isChecked(), self.ui.p6_sigma_hold.isChecked()],
                 [self.ui.p7_amp_hold.isChecked(), self.ui.p7_cen_hold.isChecked(), self.ui.p7_sigma_hold.isChecked()],
                 [self.ui.p8_amp_hold.isChecked(), self.ui.p8_cen_hold.isChecked(), self.ui.p8_sigma_hold.isChecked()]]

        holds = [[not holds[j][i] for i in range(3)] for j in range(8)]
        lin_pars = [self.ui.slope_dsb.value(), self.ui.intercept_dsb.value()]
        return checked, cons, nums_checked, constraints, holds, lin_pars

    def initial_fit(self):
        self.removing_ir_lines()
        checked, cons, nums_checked,_,holds, lin_pars = self.checked_cons()
        obj = self.fit_obj[self.ui.ir_range_cb.currentText()]
        result = obj.initial_plot(checked, cons, lin_pars)
        # comps = result.eval_components()
        init = result.init_fit
        ApplicationSettings.ALL_DATA_PLOTTED[self.ui.ir_range_cb.currentText() + '_init'] = \
            self.main_window.ax.plot(obj.x_data, init, 'k--',
                                     label=self.ui.ir_range_cb.currentText() + '_init')
        self.main_window.canvas.draw()

    def fit_fun(self):
        self.removing_ir_lines()
        checked, cons, nums_checked, constraints, holds, lin_pars = self.checked_cons()
        fwhm_list = [self.ui.p1_fwhm,self.ui.p2_fwhm,self.ui.p3_fwhm,self.ui.p4_fwhm,self.ui.p5_fwhm,
                     self.ui.p6_fwhm,self.ui.p7_fwhm,self.ui.p8_fwhm]
        obj = self.fit_obj[self.ui.ir_range_cb.currentText()]
        result = obj.fit(checked, cons, holds, lin_pars, self.ui.baseline_combo.currentText())
        comps = result.eval_components()
        ApplicationSettings.ALL_DATA_PLOTTED[self.ui.ir_range_cb.currentText()+'_fit'] = \
            self.main_window.ax.plot(obj.x_data, result.best_fit, 'r-', label=self.ui.ir_range_cb.currentText()+'_fit')
        # This is the best way to plot a ModelResult class but it doens't work with the shirley background being
        # Different length nparray :(
        # x_array_dense = np.linspace(min(obj.x_data), max(obj.x_data), 200)
        # ApplicationSettings.ALL_DATA_PLOTTED[self.ui.fit_range_cb.currentText() + '_fit'] = \
        #     self.main_window.ax.plot(
        #         x_array_dense, result.model.eval(result.params, **{result.model.independent_vars[0]: x_array_dense}))
        self.ui.fit_results_te.setText(result.fit_report())
        if self.ui.plot_3sig_box.isChecked():
            try:
                dely = result.eval_uncertainty(sigma=3)
                ApplicationSettings.ALL_DATA_PLOTTED['Verr_' + self.ui.ir_range_cb.currentText()] = \
                    self.main_window.ax.fill_between(obj.x_data, result.best_fit - dely,
                                                     result.best_fit + dely, color="#ABABAB",
                                                     label= '_3-$\sigma$ uncertainty band')
            except TypeError:
                pass
        for i in nums_checked:
            constraints[i][0][0].setValue(result.params['p%s_amplitude' % str(i)].value)
            constraints[i][1][0].setValue(result.params['p%s_center' % str(i)].value)
            constraints[i][2][0].setValue(result.params['p%s_sigma' % str(i)].value)
            fwhm_list[i].setValue(result.params['p%s_sigma' % str(i)].value*3.6013)
            obj.peak_constraints[i][0][0] = result.params['p%s_amplitude' % str(i)].value
            obj.peak_constraints[i][1][0] = result.params['p%s_center' % str(i)].value
            obj.peak_constraints[i][2][0] = result.params['p%s_sigma' % str(i)].value
        try:
            self.ui.slope_dsb.setValue(result.params['slope'])
            self.ui.intercept_dsb.setValue(result.params['intercept'])
        except KeyError:
            pass
        try:
            self.ui.intercept_dsb.setValue(result.params['c'])
        except KeyError:
            pass

        if self.ui.plot_components_box.isChecked():
            if self.ui.baseline_combo == 'Linear':
                for i in nums_checked:
                    ApplicationSettings.ALL_DATA_PLOTTED['V%s_' % str(i)+self.ui.ir_range_cb.currentText()] = \
                        self.main_window.ax.plot(obj.x_data,  comps['p%s_' % str(i)]+comps['linear'], 'k--', label='_V%s' % str(i)+self.ui.ir_range_cb.currentText())
                ApplicationSettings.ALL_DATA_PLOTTED['lin_part' + self.ui.ir_range_cb.currentText()] = \
                    self.main_window.ax.plot(obj.x_data, comps['linear'], 'k--',
                                             label='_linmod_' + self.ui.ir_range_cb.currentText())
            elif self.ui.baseline_combo == 'Constant':
                for i in nums_checked:
                    ApplicationSettings.ALL_DATA_PLOTTED['V%s_' % str(i)+self.ui.ir_range_cb.currentText()] = \
                        self.main_window.ax.plot(obj.x_data,  comps['p%s_' % str(i)]+comps['c'], 'k--', label='_V%s' % str(i)+self.ui.ir_range_cb.currentText())
                ApplicationSettings.ALL_DATA_PLOTTED['const_part' + self.ui.ir_range_cb.currentText()] = \
                    self.main_window.ax.plot(obj.x_data, comps['c'], 'k--',
                                             label='_cmod_' + self.ui.ir_range_cb.currentText())
            else:
                for i in nums_checked:
                    ApplicationSettings.ALL_DATA_PLOTTED['V%s_' % str(i)+self.ui.ir_range_cb.currentText()] = \
                        self.main_window.ax.plot(obj.x_data,  comps['p%s_' % str(i)], 'k--', label='_V%s' % str(i)+self.ui.ir_range_cb.currentText())
        self.main_window.canvas.draw()

    def clear_fit_objs(self):
        self.ui.ir_range_cb.clear()
        self.fit_obj = {}

    def removing_ir_lines(self):
        try:
            line0 = ApplicationSettings.ALL_DATA_PLOTTED[self.ui.ir_range_cb.currentText() + '_init']
            self.main_window.ax.lines.remove(line0[0])
        except KeyError:
            pass
        except ValueError:
            pass
        try:
            line0 = ApplicationSettings.ALL_DATA_PLOTTED[self.ui.ir_range_cb.currentText() + '_fit']
            self.main_window.ax.lines.remove(line0[0])
        except KeyError:
            pass
        except ValueError:
            pass
        for i in range(8):
            try:
                line0 = ApplicationSettings.ALL_DATA_PLOTTED['V%s_' % str(i)+self.ui.ir_range_cb.currentText()]
                self.main_window.ax.lines.remove(line0[0])
            except KeyError:
                pass
            except ValueError:
                pass
        if str('Verr_' + self.ui.ir_range_cb.currentText()) in ApplicationSettings.ALL_DATA_PLOTTED:
            poly = ApplicationSettings.ALL_DATA_PLOTTED['Verr_' + self.ui.ir_range_cb.currentText()]
            poly.remove()
            ApplicationSettings.ALL_DATA_PLOTTED.pop('Verr_' + self.ui.ir_range_cb.currentText())
            del poly
        if str('lin_part' + self.ui.ir_range_cb.currentText()) in ApplicationSettings.ALL_DATA_PLOTTED:
            line0 = ApplicationSettings.ALL_DATA_PLOTTED['lin_part' + self.ui.ir_range_cb.currentText()]
            print(line0)
            try:
                self.main_window.ax.lines.remove(line0[0])
            except ValueError:
                pass
                # line0.remove()
        self.main_window.canvas.draw()

class IR_Fit_Object(object):
    def __init__(self, x_data, y_data, minimum, maximum):
        self.peak_constraints = []
        self.constraints = []
        self.peak_type = {}
        self.peak_fitted_values = {}
        self.shirley = None
        lims = [find_nearest(x_data, minimum), find_nearest(x_data, maximum)]
        self.x_data = x_data[lims[0]:lims[1]]
        self.y_data = y_data[lims[0]:lims[1]]
        self.mini = minimum
        self.maxi = maximum
        self.init_constraints(minimum, maximum)
        self.fit_result = None

    def init_constraints(self, minimum, maximum):
        middle = minimum + (maximum-minimum)/2
        centers = [middle for i in range(8)]
        for i in range(8):
            self.peak_constraints.append([[50, -9999, 99999], [centers[i], minimum, maximum], [50, .0001, 1000]])

    def fit(self, checked, cons, holds, lin_pars, baseline):
        self.update_constraints(cons)
        if baseline == 'Linear':
            con_mod = LinearModel()
        elif baseline == 'Constant':
            con_mod = ConstantModel()
        elif baseline == 'None':
            pass
        line_shape_mods = [VoigtModel(prefix='p0_'), VoigtModel(prefix='p1_'),
                           VoigtModel(prefix='p2_'), VoigtModel(prefix='p3_'),
                           VoigtModel(prefix='p4_'), VoigtModel(prefix='p5_'),
                           VoigtModel(prefix='p6_'), VoigtModel(prefix='p7_')]
        cur_mods = []
        checked_peaks = []
        params = Parameters()
        # add with tuples: (NAME VALUE VARY MIN  MAX  EXPR  BRUTE_STEP)
        for x in range(8):
            if checked[x]:
                params.add_many(('p%s_amplitude' % str(x), self.peak_constraints[x][0][0], holds[x][0], self.peak_constraints[x][0][1], self.peak_constraints[x][0][2]),
                                ('p%s_center' % str(x), self.peak_constraints[x][1][0], holds[x][1], self.peak_constraints[x][1][1], self.peak_constraints[x][1][2]),
                                ('p%s_sigma' % str(x), self.peak_constraints[x][2][0], holds[x][2], self.peak_constraints[x][2][1], self.peak_constraints[x][2][2]))
                checked_peaks.append(x)
                cur_mods.append(line_shape_mods[x])
        if baseline == 'Linear':
            con_mod = LinearModel()
            params.add_many(('slope', lin_pars[0], False), ('intercept', lin_pars[1], False))
        elif baseline == 'Constant':
            con_mod = ConstantModel()
            params.add_many(('c', lin_pars[1], False))
        elif baseline == 'None':
            pass
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
            mod = cur_mods[0] + cur_mods[1] + cur_mods[2] + cur_mods[3] + cur_mods[4] + cur_mods[5] + cur_mods[6] + cur_mods[7]
        # add with tuples: (NAME VALUE VARY MIN  MAX  EXPR  BRUTE_STEP)
        if baseline == 'None':
            pass
        else:
            mod = mod + con_mod
        result = mod.fit(self.y_data, params, x=self.x_data)
        self.fit_result = result.fit_report()
        return result

    def update_constraints(self, constraints):
        for i in range(8):
            for j in range(3):
                for k in range(3):
                    self.peak_constraints[i][j][k] = constraints[i][j][k]

    def initial_plot(self, checked, cons, lin_pars):
        self.update_constraints(cons)
        # line_shape_mods = [PseudoVoigtModel(prefix='p0_'), PseudoVoigtModel(prefix='p1_'),
        #                    PseudoVoigtModel(prefix='p2_'),PseudoVoigtModel(prefix='p3_'),
        #                    PseudoVoigtModel(prefix='p4_'),PseudoVoigtModel(prefix='p5_'),
        #                    PseudoVoigtModel(prefix='p6_'),PseudoVoigtModel(prefix='p7_')]
        line_shape_mods = [VoigtModel(prefix='p0_'), VoigtModel(prefix='p1_'),
                           VoigtModel(prefix='p2_'), VoigtModel(prefix='p3_'),
                           VoigtModel(prefix='p4_'), VoigtModel(prefix='p5_'),
                           VoigtModel(prefix='p6_'), VoigtModel(prefix='p7_')]
        cur_mods = []
        con_mod = LinearModel()
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
                                 self.peak_constraints[x][2][1], self.peak_constraints[x][2][2]),('slope', lin_pars[0], True), ('intercept', lin_pars[1], True))
                checked_peaks.append(x)
                cur_mods.append(line_shape_mods[x])
        if len(checked_peaks) == 1:
            mod = cur_mods[0] + con_mod
        elif len(checked_peaks) == 2:
            mod = cur_mods[0] + cur_mods[1] + con_mod
        elif len(checked_peaks) == 3:
            mod = cur_mods[0] + cur_mods[1] + cur_mods[2] + con_mod
        elif len(checked_peaks) == 4:
            mod = cur_mods[0] + cur_mods[1] + cur_mods[2] + cur_mods[3] + con_mod
        elif len(checked_peaks) == 5:
            mod = cur_mods[0] + cur_mods[1] + cur_mods[2] + cur_mods[3] + cur_mods[4] + con_mod
        elif len(checked_peaks) == 6:
            mod = cur_mods[0] + cur_mods[1] + cur_mods[2] + cur_mods[3] + cur_mods[4] + cur_mods[5] + con_mod
        elif len(checked_peaks) == 7:
            mod = cur_mods[0] + cur_mods[1] + cur_mods[2] + cur_mods[3] + cur_mods[4] + cur_mods[5] + cur_mods[6] + con_mod
        elif len(checked_peaks) == 8:
            mod = cur_mods[0] + cur_mods[1] + cur_mods[2] + cur_mods[3] + cur_mods[4] + cur_mods[5] + cur_mods[6] + \
                  cur_mods[7] + con_mod
        # add with tuples: (NAME VALUE VARY MIN  MAX  EXPR  BRUTE_STEP)
        result = mod.fit(self.y_data, params, x=self.x_data)
        return result
