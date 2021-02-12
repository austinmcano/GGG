from src.Ui_Files.DockWidgets.Py.dw_XRD import Ui_DockWidget
from src.gui_elements.RC_Fucntions import *
# from src.gui_elements.Plotting_Functions import *
from lmfit import Parameters
from lmfit.models import VoigtModel, GaussianModel, LorentzianModel

class XRD_view(QtWidgets.QDockWidget):
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
        self.data = None
        self.baseline = None
        self.model = None
        self.x_data = None
        self.y_data = None
        self.constraints = np.asarray(
            [[1000,36,.1], [1000,50,.1]])
        for row in range(2):
            for column in range(3):
                self.ui.tw_fit_params.setItem(row,column,QtWidgets.QTableWidgetItem(str(self.constraints[row][column])))


    def _init_widgets(self):
        self.tree_view = self.ui.treeView
        self.context_menu = QtWidgets.QMenu(self)
        # Create context menu
        rc_browser_options(self)

    def _init_UI(self):
        self.model = QtWidgets.QFileSystemModel()
        self.model.setRootPath('')

        self.tree_view.setModel(self.model)
        self.tree_view.setSortingEnabled(True)

        self.tree_view.sortByColumn(True)
        self.tree_view.setRootIndex(self.model.index(self.main_window.settings.value('XRD_PATH')))

        self.tree_view.setModel(self.model)
        self.tree_view.installEventFilter(self)
        self.tree_view.setColumnWidth(0, 200)

        self.ui.tw_fit_params.cellChanged.connect(lambda: self.save_constraints())
        self.ui.fillcols_pb.clicked.connect(lambda: self.fill_cols())
        self.ui.plot_pb.clicked.connect(lambda: self.plot_xrd())
        self.ui.baseline_pb.clicked.connect(lambda: self.baseline_function())
        self.ui.go_pb.clicked.connect(lambda: self.scherrer_calculate())
        self.ui.fit_init_pb.clicked.connect(lambda: self.plot_init_fit())
        self.ui.fit_pb.clicked.connect(lambda: self.fitting_function())

    def eventFilter(self, object, event):
        # For right click events
        if event.type() == QtCore.QEvent.ContextMenu:
            self.context_menu.exec_(self.mapToGlobal(event.pos()))
        return False

    def save_constraints(self):
        try:
            for row in range(2):
                for column in range(3):
                    self.constraints[row][column] = float(self.ui.tw_fit_params.item(row, column).text())
        except ValueError:
            print('No constraint save')

    def gaussian(self,x, amp, cen, sigma):
        return amp/(sigma*np.sqrt(2*np.pi))*np.exp(-(x-cen)**2/(2*sigma**2))

    def lorentz(self, x, amp, cen, sigma):
        return (amp/np.pi)*(1/2*sigma)/((x-cen)**2+(1/2*sigma)**2)

    def fill_cols(self):
        self.ui.tw_x.clear()
        self.ui.tw_y.clear()
        path = self.model.filePath(self.tree_view.currentIndex())
        filename, extension = os.path.splitext(self.model.filePath(self.tree_view.currentIndex()))
        if extension == '.CSV' or extension == '.csv':
            self.data = pd.read_csv(path, delimiter=',', skiprows=0)
        elif extension == '.xls' or extension == '.xlxs':
            excelfile = pd.ExcelFile(path)
            self.data = pd.read_excel(excelfile, "Sheet1")
        elif extension == '.X01':
            self.data = pd.read_csv(path, delimiter='   ', skiprows=48, engine='python')
        elif extension =='.txt':
            self.data = pd.read_csv(path, sep='\t', skiprows=self.ui.skip_rows_sb.value())
        else:
            print(extension)
            self.data = pd.read_csv(path, sep='\t')

        strings = [col for col in self.data.columns]
        column_list_x = []
        column_list_y = []
        for i in strings:
            column_list_x.append(QtWidgets.QTreeWidgetItem([i]))
            column_list_y.append(QtWidgets.QTreeWidgetItem([i]))
            self.ui.tw_x.addTopLevelItems(column_list_x)
            self.ui.tw_y.addTopLevelItems(column_list_y)

    def plot_xrd(self):
        x = self.ui.tw_x.currentIndex().data()
        self.x_data = self.data[x].to_numpy()
        self.x_data = self.x_data[~np.isnan(self.x_data)]
        y = self.ui.tw_y.currentIndex().data()
        self.y_data = self.data[y].to_numpy()
        self.y_data = self.y_data[~np.isnan(self.y_data)]
        ApplicationSettings.ALL_DATA_PLOTTED[str(x)] = \
            self.main_window.ax.plot(self.x_data, self.y_data, label=x)
        self.xrd_basic()

    def xrd_basic(self):
        self.main_window.ax.set_xlabel('2$\\theta$ ($^\circ$)')
        self.main_window.ax.set_ylabel('Counts')
        leg = self.main_window.ax.legend(loc='best')
        leg.set_draggable(True)
        self.main_window.fig.tight_layout()
        self.main_window.canvas.draw()

    def fitting_function(self):
        self.main_window.cleargraph()
        self.save_constraints()
        con = self.constraints
        x_lim = ApplicationSettings.C_X_LIM
        indexs = [find_nearest(self.x_data, x_lim[0]), find_nearest(self.x_data, x_lim[1])]
        self.x_data = self.x_data[indexs[0]:indexs[1]]
        self.y_data = self.y_data[indexs[0]:indexs[1]]

        if self.ui.fittype_cb.currentText() == 'Gaussian':
            if self.ui.num_peaks_sb.value() == 1:
                gmodel = GaussianModel()
                params = Parameters()
                # add with tuples: (NAME VALUE VARY MIN  MAX  EXPR  BRUTE_STEP)
                params.add_many(('amplitude', con[0][0]),
                                ('center', con[0][1]),
                                ('sigma', con[0][2]))
                result = gmodel.fit(self.y_data, params, x=self.x_data)
                ApplicationSettings.ALL_DATA_PLOTTED['Fit'] = self.main_window.ax.plot(self.x_data,
                                                                                       result.best_fit,
                                                                                       'r--', label='Result')
                self.ui.fwhm_sb.setValue(2.3548 * result.params['sigma'].value*np.pi/180)
            elif self.ui.num_peaks_sb.value() == 2:
                gmodel = GaussianModel(prefix='p1_') + GaussianModel(prefix='p2_')
                params = Parameters()
                # add with tuples: (NAME VALUE VARY MIN  MAX  EXPR  BRUTE_STEP)
                params.add_many(('p1_amplitude', con[0][0]),
                                ('p1_center', con[0][1]),
                                ('p1_sigma', con[0][2]),
                                ('p2_amplitude', con[1][0]),
                                ('p2_center', con[1][1]),
                                ('p2_sigma', con[1][2]))
                result = gmodel.fit(self.y_data, params, x=self.x_data)
                comps = result.eval_components()
                ApplicationSettings.ALL_DATA_PLOTTED['G1'] = self.main_window.ax.plot(self.x_data,
                                                                                      comps['p1_'],
                                                                                      'k--', label='G1')
                ApplicationSettings.ALL_DATA_PLOTTED['G2'] = self.main_window.ax.plot(self.x_data,
                                                                                      comps['p2_'],
                                                                                      'k--', label='G2')
                ApplicationSettings.ALL_DATA_PLOTTED['Fit'] = self.main_window.ax.plot(self.x_data,
                                                                                       result.best_fit,
                                                                                       'r--', label='Result')
                leg = self.main_window.ax.legend(loc='best', fontsize='small')
                leg.set_draggable(True)

        elif self.ui.fittype_cb.currentText() == 'Lorentz':
            if self.ui.num_peaks_sb.value() == 1:
                lmodel = LorentzianModel()
                params = Parameters()
                # add with tuples: (NAME VALUE VARY MIN  MAX  EXPR  BRUTE_STEP)
                params.add_many(('amplitude', con[0][0]),
                                ('center', con[0][1]),
                                ('sigma', con[0][2]), )
                result = lmodel.fit(self.y_data, params, x=self.x_data)
                ApplicationSettings.ALL_DATA_PLOTTED['Fit'] = self.main_window.ax.plot(self.x_data,
                                                                                       result.best_fit,
                                                                                       'r--', label='Result')
                leg = self.main_window.ax.legend(loc='best', fontsize='small')
                self.ui.fwhm_sb.setValue(2 * result.params['sigma'].value*np.pi/180)
                leg.set_draggable(True)
            elif self.ui.num_peaks_sb.value() == 2:
                lmodel = LorentzianModel(prefix='p1_') + LorentzianModel(prefix='p2_')
                params = Parameters()
                # add with tuples: (NAME VALUE VARY MIN  MAX  EXPR  BRUTE_STEP)
                params.add_many(('p1_amplitude', con[0][0]),
                                ('p1_center', con[0][1]),
                                ('p1_sigma', con[0][2]),
                                ('p2_amplitude', con[1][0]),
                                ('p2_center', con[1][1]),
                                ('p2_sigma', con[1][2]))
                result = lmodel.fit(self.y_data, params, x=self.x_data)
                comps = result.eval_components()
                ApplicationSettings.ALL_DATA_PLOTTED['L1'] = self.main_window.ax.plot(self.x_data,
                                                                                      comps['p1_'],
                                                                                      'k--', label='L1')
                ApplicationSettings.ALL_DATA_PLOTTED['L2'] = self.main_window.ax.plot(self.x_data,
                                                                                      comps['p2_'],
                                                                                      'k--', label='L2')
                ApplicationSettings.ALL_DATA_PLOTTED['Fit'] = self.main_window.ax.plot(self.x_data,
                                                                                       result.best_fit,
                                                                                       'r--', label='Result')
                leg = self.main_window.ax.legend(loc='best', fontsize='small')
                leg.set_draggable(True)

        elif self.ui.fittype_cb.currentText() == 'Pseudo-Voigt':
            if self.ui.num_peaks_sb.value() == 1:
                vmodel = VoigtModel()
                params = Parameters()
                params.add_many(('amplitude', con[0][0]),
                                ('center', con[0][1]),
                                ('sigma', con[0][2]))
                result = vmodel.fit(self.y_data, params, x=self.x_data)
                ApplicationSettings.ALL_DATA_PLOTTED['Fit'] = self.main_window.ax.plot(self.x_data,
                                                                                       result.best_fit,
                                                                                       'r--', label='Result')
                self.ui.fwhm_sb.setValue(3.6013 * result.params['sigma'].value*np.pi/180)
                self.ui.theta_sb.setValue(result.params['center']* np.pi/180)
            elif self.ui.num_peaks_sb.value() == 2:
                vmodel = VoigtModel(prefix='p1_') + VoigtModel(prefix='p2_')
                params = Parameters()
                # add with tuples: (NAME VALUE VARY MIN  MAX  EXPR  BRUTE_STEP)
                params.add_many(('p1_amplitude', con[0][0]),
                                ('p1_center', con[0][1]),
                                ('p1_sigma', con[0][2]),
                                ('p2_amplitude', con[1][0]),
                                ('p2_center', con[1][1]),
                                ('p2_sigma', con[1][2]))
                result = vmodel.fit(self.y_data, params, x=self.x_data)
                comps = result.eval_components()
                ApplicationSettings.ALL_DATA_PLOTTED['V1'] = self.main_window.ax.plot(self.x_data,
                                                                                      comps['p1_'],
                                                                                      'k--', label='V1')
                ApplicationSettings.ALL_DATA_PLOTTED['V2'] = self.main_window.ax.plot(self.x_data,
                                                                                      comps['p2_'],
                                                                                      'k--', label='V2')
                ApplicationSettings.ALL_DATA_PLOTTED['Fit'] = self.main_window.ax.plot(self.x_data,
                                                                                       result.best_fit,
                                                                                       'r--', label='Result')

        ApplicationSettings.ALL_DATA_PLOTTED['Y Data'] = self.main_window.ax.plot(
            self.x_data, self.y_data, label='data')
        self.ui.fit_results_te.setText(result.fit_report())
        self.xrd_basic()

    def plot_init_fit(self):
        # x_lim = ApplicationSettings.C_X_LIM
        # indexs = [find_nearest(self.x_data, x_lim[1]), find_nearest(self.x_data, x_lim[0])]
        # self.x_data = self.x_data[indexs[0]:indexs[1]]
        # self.y_data = self.y_data[indexs[0]:indexs[1]]

        if self.ui.fittype_cb.currentText() == 'Lorentz':
            model = self.lorentz
        else:
            model = self.gaussian
        con = self.constraints
        if self.ui.num_peaks_sb.value() == 1:
            start_plot = model(self.x_data, con[0][0], con[0][1], con[0][2])
        elif self.ui.num_peaks_sb.value() == 2:
            start_plot = model(self.x_data, con[0][0], con[0][1], con[0][2]) + \
                         model(self.x_data, con[1][0], con[1][1], con[1][2])
        ApplicationSettings.ALL_DATA_PLOTTED['init_fit'] = \
            self.main_window.ax.plot(self.x_data, start_plot, label='init_fit')
        self.xrd_basic()

    def baseline_function(self):
        self.main_window.cleargraph()
        self.baseline = baseline_als(self.y_data,self.ui.lambda_sb.value(),self.ui.p_sb.value())
        ApplicationSettings.ALL_DATA_PLOTTED['corrected'] = \
            self.main_window.ax.plot(self.x_data, self.y_data-self.baseline, label='corrected')
        ApplicationSettings.ALL_DATA_PLOTTED['raw'] = \
            self.main_window.ax.plot(self.x_data, self.y_data, label='raw')
        ApplicationSettings.ALL_DATA_PLOTTED['baseline'] = \
            self.main_window.ax.plot(self.x_data,self.baseline, label='baseline')
        # ApplicationSettings.ALL_DATA_PLOTTED['baseline'] = \
        #     self.main_window.ax.plot(self.x_data, self.baseline, label='baseline')
        self.xrd_basic()

    def scherrer_calculate(self):
        k = self.ui.k_sb.value()
        lam = self.ui.lambda_sb.value()
        theta = self.ui.theta_sb.value()
        fwhm = self.ui.fwhm_sb.value()
        size = (k*lam)/(np.cos(theta)*fwhm)
        self.ui.c_size_label.setText(str(size))
