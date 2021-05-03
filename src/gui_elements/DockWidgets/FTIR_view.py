from src.Ui_Files.DockWidgets.Py.dw_FTIR import Ui_DockWidget
from src.gui_elements.RC_Fucntions import *
import glob
from scipy.signal import savgol_filter
from lmfit.models import VoigtModel, GaussianModel, LorentzianModel, PseudoVoigtModel
from lmfit import Model, Parameters
from src.Ui_Files.Dialogs.simple_treeWidget_dialog import Ui_Dialog as twDialog_ui
from src.gui_elements.plotting_functions import baseline_als
from src.gui_elements.general_functions import find_nearest
from matplotlib.widgets import SpanSelector

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
        self.data_x = None
        self.data_y = None
        self.constraints = np.asarray(
            [[10, -1000, 1000, 3700, 400, 4000, 50, 1, 400], [10, -1000, 2900, 285, 400, 4000, 50, 1, 400],
             [1, -1000, 1000, 2890, 400, 4000, 50, 1, 400], [10, -1000, 1000, 1215, 400, 4000, 50, 1, 400],
             [10, -1000, 1000, 900, 400, 4000, 50, 1, 400]])
        for row in range(9):
            for column in range(5):
                self.ui.tableWidget_2.setItem(row, column, QtWidgets.QTableWidgetItem(str(self.constraints[column][row])))

    def _init_widgets(self):
        self.tree_view = self.ui.FTIR_treeView
        self.context_menu = QtWidgets.QMenu(self)
        # Create context menu
        rc_browser_options(self)

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
        # self.ui.

        self.ui.fit_pb.clicked.connect(lambda: self.fitting_function())
        self.ui.plot_current_pb.clicked.connect(lambda: self.plot_init())
        self.ui.tableWidget_2.cellChanged.connect(lambda: self.save_constraints())
        self.ui.selectdata_pb.clicked.connect(lambda: self.select_data())
        self.ui.baseline_pb.clicked.connect(lambda: self.baseline_data())
        self.ui.integratemode_rb.toggled.connect(self.integrate_mode)

        self.ui.sub_dir_pb.clicked.connect(lambda: self.ir_plot('sub'))
        self.ui.diff_2_pb.clicked.connect(lambda: self.ir_plot('diff2'))
        self.ui.diff_dir_pb.clicked.connect(lambda: self.ir_plot('diff'))
        self.ui.abs_dir_pb.clicked.connect(lambda: self.ir_plot('abs'))
        self.ui.spectra_pb.clicked.connect(lambda: self.ir_plot('spectra'))
        self.ui.fit2_pb.clicked.connect(lambda: self.fitting_function_2())
        self.ui.select_data_pb.clicked.connect(lambda: self.select_data())
        self.ui.fit_init_pb.clicked.connect(lambda: self.plot_init_2())

    def eventFilter(self, object, event):
        # For right click events
        if event.type() == QtCore.QEvent.ContextMenu:
            self.context_menu.exec_(self.mapToGlobal(event.pos()))
        return False

    def save_constraints(self):
        try:
            for row in range(9):
                for column in range(5):
                    self.constraints[column][row] = float(self.ui.tableWidget_2.item(row, column).text())
        except ValueError:
            print('No constraint save')

    def fitting_function(self):
        self.main_window.cleargraph()
        self.save_constraints()
        con = self.constraints

        if self.ui.fit_shape_cb.currentText() == 'Gaussian':
            if self.ui.num_peaks_sb.value() == 1:
                gmodel = GaussianModel()
                params = Parameters()
                # add with tuples: (NAME VALUE VARY MIN  MAX  EXPR  BRUTE_STEP)
                params.add_many(('amplitude', con[0][0], True, con[0][1], con[0][2]),
                                ('center', con[0][3], True, con[0][4], con[0][5]),
                                ('sigma', con[0][6], True, con[0][7], con[0][8]))
                result = gmodel.fit(self.data_y, params, x=self.data_x)
                self.ui.fit_report_TE.setText(result.fit_report())
                ApplicationSettings.ALL_DATA_PLOTTED['Fit'] = self.main_window.ax.plot(self.data_x,
                                                                                       result.best_fit,
                                                                                       'r--', label='Result')

            elif self.ui.num_peaks_sb.value() == 2:
                gmodel = GaussianModel(prefix='p1_') + GaussianModel(prefix='p2_')
                params = Parameters()
                # add with tuples: (NAME VALUE VARY MIN  MAX  EXPR  BRUTE_STEP)
                params.add_many(('p1_amplitude', con[0][0], True, con[0][1], con[0][2]),
                                ('p1_center', con[0][3], True, con[0][4], con[0][5]),
                                ('p1_sigma', con[0][6], True, con[0][7], con[0][8]),
                                ('p2_amplitude', con[1][0], True, con[1][1], con[1][2]),
                                ('p2_center', con[1][3], True, con[1][4], con[1][5]),
                                ('p2_sigma', con[1][6], True, con[1][7], con[1][8]))
                result = gmodel.fit(self.data_y, params, x=self.data_x)
                comps = result.eval_components()
                self.ui.fit_report_TE.setText(result.fit_report())
                ApplicationSettings.ALL_DATA_PLOTTED['G1'] = self.main_window.ax.plot(self.data_x,
                                                                                      comps['p1_'],
                                                                                      'k--', label='G1')
                ApplicationSettings.ALL_DATA_PLOTTED['G2'] = self.main_window.ax.plot(self.data_x,
                                                                                      comps['p2_'],
                                                                                      'k--', label='G2')
                ApplicationSettings.ALL_DATA_PLOTTED['Fit'] = self.main_window.ax.plot(self.data_x,
                                                                                       result.best_fit,
                                                                                       'r--', label='Result')
                leg = self.main_window.ax.legend(loc='best', fontsize='small')
                leg.set_draggable(True)

            elif self.ui.num_peaks_sb.value() == 3:
                gmodel = GaussianModel(prefix='p1_') + GaussianModel(prefix='p2_') + Model(prefix='p3_')
                params = Parameters()
                # add with tuples: (NAME VALUE VARY MIN  MAX  EXPR  BRUTE_STEP)
                params.add_many(('p1_amplitude', con[0][0], True, con[0][1], con[0][2]),
                                ('p1_center', con[0][3], True, con[0][4], con[0][5]),
                                ('p1_sigma', con[0][6], True, con[0][7], con[0][8]),
                                ('p2_amplitude', con[1][0], True, con[1][1], con[1][2]),
                                ('p2_center', con[1][3], True, con[1][4], con[1][5]),
                                ('p2_sigma', con[1][6], True, con[1][7], con[1][8]),
                                ('p3_amplitude', con[2][0], True, con[2][1], con[2][2]),
                                ('p3_center', con[2][3], True, con[2][4], con[2][5]),
                                ('p3_sigma', con[2][6], True, con[2][7], con[2][8]))
                result = gmodel.fit(self.data_y, params, x=self.data_x)
                comps = result.eval_components()
                ApplicationSettings.ALL_DATA_PLOTTED['G1'] = self.main_window.ax.plot(self.data_x,
                                                                                      comps['p1_'],
                                                                                      'k--', label='G1')
                ApplicationSettings.ALL_DATA_PLOTTED['G2'] = self.main_window.ax.plot(self.data_x,
                                                                                      comps['p2_'],
                                                                                      'k--', label='G2')
                ApplicationSettings.ALL_DATA_PLOTTED['G3'] = self.main_window.ax.plot(self.data_x,
                                                                                      comps['p3_'],
                                                                                      'k--', label='G3')
                ApplicationSettings.ALL_DATA_PLOTTED['Fit'] = self.main_window.ax.plot(self.data_x,
                                                                                       result.best_fit,
                                                                                       'r--', label='Result')
                self.ui.fit_report_TE.setText(result.fit_report())

            elif self.ui.num_peaks_sb.value() == 4:
                gmodel = GaussianModel(prefix='p1_') + GaussianModel(prefix='p2_') + \
                         GaussianModel(prefix='p3_') + GaussianModel(prefix='p4_')
                params = Parameters()
                # add with tuples: (NAME VALUE VARY MIN  MAX  EXPR  BRUTE_STEP)
                params.add_many(('p1_amplitude', con[0][0], True, con[0][1], con[0][2]),
                                ('p1_center', con[0][3], True, con[0][4], con[0][5]),
                                ('p1_sigma', con[0][6], True, con[0][7], con[0][8]),
                                ('p2_amplitude', con[1][0], True, con[1][1], con[1][2]),
                                ('p2_center', con[1][3], True, con[1][4], con[1][5]),
                                ('p2_sigma', con[1][6], True, con[1][7], con[1][8]),
                                ('p3_amplitude', con[2][0], True, con[2][1], con[2][2]),
                                ('p3_center', con[2][3], True, con[2][4], con[2][5]),
                                ('p3_sigma', con[2][6], True, con[2][7], con[2][8]),
                                ('p4_amplitude', con[3][0], True, con[3][1], con[3][2]),
                                ('p4_center', con[3][3], True, con[3][4], con[3][5]),
                                ('p4_sigma', con[3][6], True, con[3][7], con[3][8]))
                result = gmodel.fit(self.data_y, params, x=self.data_x)
                comps = result.eval_components()
                ApplicationSettings.ALL_DATA_PLOTTED['G1'] = self.main_window.ax.plot(self.data_x,
                                                                                      comps['p1_'],
                                                                                      'k--', label='G1')
                ApplicationSettings.ALL_DATA_PLOTTED['G2'] = self.main_window.ax.plot(self.data_x,
                                                                                      comps['p2_'],
                                                                                      'k--', label='G2')
                ApplicationSettings.ALL_DATA_PLOTTED['G3'] = self.main_window.ax.plot(self.data_x,
                                                                                      comps['p3_'],
                                                                                      'k--', label='G3')
                ApplicationSettings.ALL_DATA_PLOTTED['G4'] = self.main_window.ax.plot(self.data_x,
                                                                                      comps['p4_'],
                                                                                      'k--', label='G4')
                ApplicationSettings.ALL_DATA_PLOTTED['Fit'] = self.main_window.ax.plot(self.data_x,
                                                                                       result.best_fit,
                                                                                       'r--', label='Result')
                leg = self.main_window.ax.legend(loc='best', fontsize='small')
                leg.set_draggable(True)
                self.ui.fit_report_TE.setText(result.fit_report())

            elif self.ui.num_peaks_sb.value() == 5:

                gmodel = GaussianModel(prefix='p1_') + GaussianModel(prefix='p2_') + \
                         GaussianModel(prefix='p3_') + GaussianModel(prefix='p4_') + GaussianModel(prefix='p5_')
                params = Parameters()
                # add with tuples: (NAME VALUE VARY MIN  MAX  EXPR  BRUTE_STEP)
                params.add_many(('p1_amplitude', con[0][0], True, con[0][1], con[0][2]),
                                ('p1_center', con[0][3], True, con[0][4], con[0][5]),
                                ('p1_sigma', con[0][6], True, con[0][7], con[0][8]),
                                ('p2_amplitude', con[1][0], True, con[1][1], con[1][2]),
                                ('p2_center', con[1][3], True, con[1][4], con[1][5]),
                                ('p2_sigma', con[1][6], True, con[1][7], con[1][8]),
                                ('p3_amplitude', con[2][0], True, con[2][1], con[2][2]),
                                ('p3_center', con[2][3], True, con[2][4], con[2][5]),
                                ('p3_sigma', con[2][6], True, con[2][7], con[2][8]),
                                ('p4_amplitude', con[3][0], True, con[3][1], con[3][2]),
                                ('p4_center', con[3][3], True, con[3][4], con[3][5]),
                                ('p4_sigma', con[3][6], True, con[3][7], con[3][8]),
                                ('p5_amplitude', con[4][0], True, con[4][1], con[4][2]),
                                ('p5_center', con[4][3], True, con[4][4], con[4][5]),
                                ('p5_sigma', con[4][6], True, con[4][7], con[4][8]))
                result = gmodel.fit(self.data_y, params, x=self.data_x)
                comps = result.eval_components()
                ApplicationSettings.ALL_DATA_PLOTTED['G1'] = self.main_window.ax.plot(self.data_x,
                                                                                      comps['p1_'],
                                                                                      'k--', label='G1')
                ApplicationSettings.ALL_DATA_PLOTTED['G2'] = self.main_window.ax.plot(self.data_x,
                                                                                      comps['p2_'],
                                                                                      'k--', label='G2')
                ApplicationSettings.ALL_DATA_PLOTTED['G3'] = self.main_window.ax.plot(self.data_x,
                                                                                      comps['p3_'],
                                                                                      'k--', label='G3')
                ApplicationSettings.ALL_DATA_PLOTTED['G4'] = self.main_window.ax.plot(self.data_x,
                                                                                      comps['p4_'],
                                                                                      'k--', label='G4')
                ApplicationSettings.ALL_DATA_PLOTTED['G5'] = self.main_window.ax.plot(self.data_x,
                                                                                      comps['p5_'],
                                                                                      'k--', label='G5')
                ApplicationSettings.ALL_DATA_PLOTTED['Fit'] = self.main_window.ax.plot(self.data_x,
                                                                                       result.best_fit,
                                                                                       'r--', label='Result')
                self.ui.fit_report_TE.setText(result.fit_report())

        elif self.ui.fit_shape_cb.currentText() == 'Lorentz':
            if self.ui.num_peaks_sb.value() == 1:
                lmodel = LorentzianModel()
                params = Parameters()
                # add with tuples: (NAME VALUE VARY MIN  MAX  EXPR  BRUTE_STEP)
                params.add_many(('amplitude', con[0][0], True, con[0][1], con[0][2]),
                                ('center', con[0][3], True, con[0][4], con[0][5]),
                                ('sigma', con[0][6], True, con[0][7], con[0][8]), )
                result = lmodel.fit(self.data_y, params, x=self.data_x)
                self.ui.fit_report_TE.setText(result.fit_report())
                ApplicationSettings.ALL_DATA_PLOTTED['Fit'] = self.main_window.ax.plot(self.data_x,
                                                                                       result.best_fit,
                                                                                       'r--', label='Result')
                leg = self.main_window.ax.legend(loc='best', fontsize='small')
                leg.set_draggable(True)
            elif self.ui.num_peaks_sb.value() == 2:
                lmodel = LorentzianModel(prefix='p1_') + LorentzianModel(prefix='p2_')
                params = Parameters()
                # add with tuples: (NAME VALUE VARY MIN  MAX  EXPR  BRUTE_STEP)
                params.add_many(('p1_amplitude', con[0][0], True, con[0][1], con[0][2]),
                                ('p1_center', con[0][3], True, con[0][4], con[0][5]),
                                ('p1_sigma', con[0][6], True, con[0][7], con[0][8]),
                                ('p2_amplitude', con[1][0], True, con[1][1], con[1][2]),
                                ('p2_center', con[1][3], True, con[1][4], con[1][5]),
                                ('p2_sigma', con[1][6], True, con[1][7], con[1][8]))
                result = lmodel.fit(self.data_y, params, x=self.data_x)
                comps = result.eval_components()
                self.ui.fit_report_TE.setText(result.fit_report())
                ApplicationSettings.ALL_DATA_PLOTTED['L1'] = self.main_window.ax.plot(self.data_x,
                                                                                      comps['p1_'],
                                                                                      'k--', label='L1')
                ApplicationSettings.ALL_DATA_PLOTTED['L2'] = self.main_window.ax.plot(self.data_x,
                                                                                      comps['p2_'],
                                                                                      'k--', label='L2')
                ApplicationSettings.ALL_DATA_PLOTTED['Fit'] = self.main_window.ax.plot(self.data_x,
                                                                                       result.best_fit,
                                                                                       'r--', label='Result')
                leg = self.main_window.ax.legend(loc='best', fontsize='small')
                leg.set_draggable(True)
            elif self.ui.num_peaks_sb.value() == 3:
                lmodel = LorentzianModel(prefix='p1_') + LorentzianModel(prefix='p2_')+LorentzianModel(prefix='p3_')
                params = Parameters()
                # add with tuples: (NAME VALUE VARY MIN  MAX  EXPR  BRUTE_STEP)
                params.add_many(('p1_amplitude', con[0][0], True, con[0][1], con[0][2]),
                                ('p1_center', con[0][3], True, con[0][4], con[0][5]),
                                ('p1_sigma', con[0][6], True, con[0][7], con[0][8]),
                                ('p2_amplitude', con[1][0], True, con[1][1], con[1][2]),
                                ('p2_center', con[1][3], True, con[1][4], con[1][5]),
                                ('p2_sigma', con[1][6], True, con[1][7], con[1][8]),
                                ('p3_amplitude', con[2][0], True, con[2][1], con[2][2]),
                                ('p3_center', con[2][3], True, con[2][4], con[2][5]),
                                ('p3_sigma', con[2][6], True, con[2][7], con[2][8]))
                result = lmodel.fit(self.data_y, params, x=self.data_x)
                comps = result.eval_components()
                self.ui.fit_report_TE.setText(result.fit_report())
                ApplicationSettings.ALL_DATA_PLOTTED['L1'] = self.main_window.ax.plot(self.data_x,
                                                                                      comps['p1_'],
                                                                                      'k--', label='L1')
                ApplicationSettings.ALL_DATA_PLOTTED['L2'] = self.main_window.ax.plot(self.data_x,
                                                                                      comps['p2_'],
                                                                                      'k--', label='L2')
                ApplicationSettings.ALL_DATA_PLOTTED['L3'] = self.main_window.ax.plot(self.data_x,
                                                                                      comps['p3_'],
                                                                                      'k--', label='L3')
                ApplicationSettings.ALL_DATA_PLOTTED['Fit'] = self.main_window.ax.plot(self.data_x,
                                                                                       result.best_fit,
                                                                                       'r--', label='Result')
                leg = self.main_window.ax.legend(loc='best', fontsize='small')
                leg.set_draggable(True)
            elif self.ui.num_peaks_sb.value() == 4:
                lmodel = LorentzianModel(prefix='p1_') + LorentzianModel(prefix='p2_')+LorentzianModel(prefix='p3_') \
                         + LorentzianModel(prefix='p4_')
                params = Parameters()
                # add with tuples: (NAME VALUE VARY MIN  MAX  EXPR  BRUTE_STEP)
                params.add_many(('p1_amplitude', con[0][0], True, con[0][1], con[0][2]),
                                ('p1_center', con[0][3], True, con[0][4], con[0][5]),
                                ('p1_sigma', con[0][6], True, con[0][7], con[0][8]),
                                ('p2_amplitude', con[1][0], True, con[1][1], con[1][2]),
                                ('p2_center', con[1][3], True, con[1][4], con[1][5]),
                                ('p2_sigma', con[1][6], True, con[1][7], con[1][8]),
                                ('p3_amplitude', con[2][0], True, con[2][1], con[2][2]),
                                ('p3_center', con[2][3], True, con[2][4], con[2][5]),
                                ('p3_sigma', con[2][6], True, con[2][7], con[2][8]),
                                ('p4_amplitude', con[3][0], True, con[3][1], con[3][2]),
                                ('p4_center', con[3][3], True, con[3][4], con[3][5]),
                                ('p4_sigma', con[3][6], True, con[3][7], con[3][8]))
                result = lmodel.fit(self.data_y, params, x=self.data_x)
                comps = result.eval_components()
                self.ui.fit_report_TE.setText(result.fit_report())
                ApplicationSettings.ALL_DATA_PLOTTED['L1'] = self.main_window.ax.plot(self.data_x,
                                                                                      comps['p1_'],
                                                                                      'k--', label='L1')
                ApplicationSettings.ALL_DATA_PLOTTED['L2'] = self.main_window.ax.plot(self.data_x,
                                                                                      comps['p2_'],
                                                                                      'k--', label='L2')
                ApplicationSettings.ALL_DATA_PLOTTED['L3'] = self.main_window.ax.plot(self.data_x,
                                                                                      comps['p3_'],
                                                                                      'k--', label='L3')
                ApplicationSettings.ALL_DATA_PLOTTED['L4'] = self.main_window.ax.plot(self.data_x,
                                                                                      comps['p4_'],
                                                                                      'k--', label='L4')
                ApplicationSettings.ALL_DATA_PLOTTED['Fit'] = self.main_window.ax.plot(self.data_x,
                                                                                       result.best_fit,
                                                                                       'r--', label='Result')
                leg = self.main_window.ax.legend(loc='best', fontsize='small')
                leg.set_draggable(True)
            elif self.ui.num_peaks_sb.value() == 5:
                lmodel = LorentzianModel(prefix='p1_') + LorentzianModel(prefix='p2_')+LorentzianModel(prefix='p3_')
                + LorentzianModel(prefix='p4_') + LorentzianModel(prefix='p5_')
                params = Parameters()
                # add with tuples: (NAME VALUE VARY MIN  MAX  EXPR  BRUTE_STEP)
                params.add_many(('p1_amplitude', con[0][0], True, con[0][1], con[0][2]),
                                ('p1_center', con[0][3], True, con[0][4], con[0][5]),
                                ('p1_sigma', con[0][6], True, con[0][7], con[0][8]),
                                ('p2_amplitude', con[1][0], True, con[1][1], con[1][2]),
                                ('p2_center', con[1][3], True, con[1][4], con[1][5]),
                                ('p2_sigma', con[1][6], True, con[1][7], con[1][8]),
                                ('p3_amplitude', con[2][0], True, con[2][1], con[2][2]),
                                ('p3_center', con[2][3], True, con[2][4], con[2][5]),
                                ('p3_sigma', con[2][6], True, con[2][7], con[2][8]),
                                ('p4_amplitude', con[3][0], True, con[3][1], con[3][2]),
                                ('p4_center', con[3][3], True, con[3][4], con[3][5]),
                                ('p4_sigma', con[3][6], True, con[3][7], con[3][8]),
                                ('p5_amplitude', con[4][0], True, con[4][1], con[4][2]),
                                ('p5_center', con[4][3], True, con[4][4], con[4][5]),
                                ('p5_sigma', con[4][6], True, con[4][7], con[4][8]))
                result = lmodel.fit(self.data_y, params, x=self.data_x)
                comps = result.eval_components()
                self.ui.fit_report_TE.setText(result.fit_report())
                ApplicationSettings.ALL_DATA_PLOTTED['L1'] = self.main_window.ax.plot(self.data_x,
                                                                                      comps['p1_'],
                                                                                      'k--', label='L1')
                ApplicationSettings.ALL_DATA_PLOTTED['L2'] = self.main_window.ax.plot(self.data_x,
                                                                                      comps['p2_'],
                                                                                      'k--', label='L2')
                ApplicationSettings.ALL_DATA_PLOTTED['L3'] = self.main_window.ax.plot(self.data_x,
                                                                                      comps['p3_'],
                                                                                      'k--', label='L3')
                ApplicationSettings.ALL_DATA_PLOTTED['L4'] = self.main_window.ax.plot(self.data_x,
                                                                                      comps['p4_'],
                                                                                      'k--', label='L4')
                ApplicationSettings.ALL_DATA_PLOTTED['L5'] = self.main_window.ax.plot(self.data_x,
                                                                                      comps['p5_'],
                                                                                      'k--', label='L5')
                ApplicationSettings.ALL_DATA_PLOTTED['Fit'] = self.main_window.ax.plot(self.data_x,
                                                                                       result.best_fit,
                                                                                       'r--', label='Result')
                leg = self.main_window.ax.legend(loc='best', fontsize='small')
                leg.set_draggable(True)

        elif self.ui.fit_shape_cb.currentText() == 'Voigt':
            if self.ui.num_peaks_sb.value() == 1:
                vmodel = VoigtModel()
                params = Parameters()
                params.add_many(('amplitude', con[0][0], True, con[0][1], con[0][2]),
                                ('center', con[0][3], True, con[0][4], con[0][5]),
                                ('sigma', con[0][6], True, con[0][7], con[0][8]))
                result = vmodel.fit(self.data_y, params, x=self.data_x)
                # self.ui.fit_report_TE.setText(result.fit_report())
                ApplicationSettings.ALL_DATA_PLOTTED['Fit'] = self.main_window.ax.plot(self.data_x,
                                                                                       result.best_fit,
                                                                                       'r--', label='Result')
            elif self.ui.num_peaks_sb.value() == 2:
                vmodel = VoigtModel(prefix='p1_') + VoigtModel(prefix='p2_')
                params = Parameters()
                # add with tuples: (NAME VALUE VARY MIN  MAX  EXPR  BRUTE_STEP)
                params.add_many(('p1_amplitude', con[0][0], True, con[0][1], con[0][2]),
                                ('p1_center', con[0][3], True, con[0][4], con[0][5]),
                                ('p1_sigma', con[0][6], True, con[0][7], con[0][8]),
                                ('p2_amplitude', con[1][0], True, con[1][1], con[1][2]),
                                ('p2_center', con[1][3], True, con[1][4], con[1][5]),
                                ('p2_sigma', con[1][6], True, con[1][7], con[1][8]))
                result = vmodel.fit(self.data_y, params, x=self.data_x)
                comps = result.eval_components()
                self.ui.fit_report_TE.setText(result.fit_report())
                ApplicationSettings.ALL_DATA_PLOTTED['V1'] = self.main_window.ax.plot(self.data_x,
                                                                                      comps['p1_'],
                                                                                      'k--', label='V1')
                ApplicationSettings.ALL_DATA_PLOTTED['V2'] = self.main_window.ax.plot(self.data_x,
                                                                                      comps['p2_'],
                                                                                      'k--', label='V2')
                ApplicationSettings.ALL_DATA_PLOTTED['Fit'] = self.main_window.ax.plot(self.data_x,
                                                                                       result.best_fit,
                                                                                       'r--', label='Result')
            elif self.ui.num_peaks_sb.value() == 3:
                vmodel = VoigtModel(prefix='p1_') + VoigtModel(prefix='p2_') + VoigtModel(prefix='p3_')
                params = Parameters()
                # add with tuples: (NAME VALUE VARY MIN  MAX  EXPR  BRUTE_STEP)
                params.add_many(('p1_amplitude', con[0][0], True, con[0][1], con[0][2]),
                                ('p1_center', con[0][3], True, con[0][4], con[0][5]),
                                ('p1_sigma', con[0][6], True, con[0][7], con[0][8]),
                                ('p2_amplitude', con[1][0], True, con[1][1], con[1][2]),
                                ('p2_center', con[1][3], True, con[1][4], con[1][5]),
                                ('p2_sigma', con[1][6], True, con[1][7], con[1][8]),
                                ('p3_amplitude', con[2][0], True, con[2][1], con[2][2]),
                                ('p3_center', con[2][3], True, con[2][4], con[2][5]),
                                ('p3_sigma', con[2][6], True, con[2][7], con[2][8]))
                result = vmodel.fit(self.data_y, params, x=self.data_x)
                comps = result.eval_components()
                ApplicationSettings.ALL_DATA_PLOTTED['V1'] = self.main_window.ax.plot(self.data_x,
                                                                                      comps['p1_'],
                                                                                      'k--', label='V1')
                ApplicationSettings.ALL_DATA_PLOTTED['V2'] = self.main_window.ax.plot(self.data_x,
                                                                                      comps['p2_'],
                                                                                      'k--', label='V2')
                ApplicationSettings.ALL_DATA_PLOTTED['V3'] = self.main_window.ax.plot(self.data_x,
                                                                                      comps['p3_'],
                                                                                      'k--', label='V3')
                ApplicationSettings.ALL_DATA_PLOTTED['Fit'] = self.main_window.ax.plot(self.data_x,
                                                                                       result.best_fit,
                                                                                       'r--', label='Result')
                self.ui.fit_report_TE.setText(result.fit_report())
            elif self.ui.num_peaks_sb.value() == 4:
                vmodel = VoigtModel(prefix='p1_') + VoigtModel(prefix='p2_') + \
                         VoigtModel(prefix='p3_') + VoigtModel(prefix='p4_')
                params = Parameters()
                # add with tuples: (NAME VALUE VARY MIN  MAX  EXPR  BRUTE_STEP)
                params.add_many(('p1_amplitude', con[0][0], True, con[0][1], con[0][2]),
                                ('p1_center', con[0][3], True, con[0][4], con[0][5]),
                                ('p1_sigma', con[0][6], True, con[0][7], con[0][8]),
                                ('p2_amplitude', con[1][0], True, con[1][1], con[1][2]),
                                ('p2_center', con[1][3], True, con[1][4], con[1][5]),
                                ('p2_sigma', con[1][6], True, con[1][7], con[1][8]),
                                ('p3_amplitude', con[2][0], True, con[2][1], con[2][2]),
                                ('p3_center', con[2][3], True, con[2][4], con[2][5]),
                                ('p3_sigma', con[2][6], True, con[2][7], con[2][8]),
                                ('p4_amplitude', con[3][0], True, con[3][1], con[3][2]),
                                ('p4_center', con[3][3], True, con[3][4], con[3][5]),
                                ('p4_sigma', con[3][6], True, con[3][7], con[3][8]))
                result = vmodel.fit(self.data_y, params, x=self.data_x)
                comps = result.eval_components()
                ApplicationSettings.ALL_DATA_PLOTTED['V1'] = self.main_window.ax.plot(self.data_x,
                                                                                      comps['p1_'],
                                                                                      'k--', label='V1')
                ApplicationSettings.ALL_DATA_PLOTTED['V2'] = self.main_window.ax.plot(self.data_x,
                                                                                      comps['p2_'],
                                                                                      'k--', label='V2')
                ApplicationSettings.ALL_DATA_PLOTTED['V3'] = self.main_window.ax.plot(self.data_x,
                                                                                      comps['p3_'],
                                                                                      'k--', label='V3')
                ApplicationSettings.ALL_DATA_PLOTTED['V4'] = self.main_window.ax.plot(self.data_x,
                                                                                      comps['p4_'],
                                                                                      'k--', label='V4')
                ApplicationSettings.ALL_DATA_PLOTTED['Fit'] = self.main_window.ax.plot(self.data_x,
                                                                                       result.best_fit,
                                                                                       'r--', label='Result')
                leg = self.main_window.ax.legend(loc='best', fontsize='small')
                leg.set_draggable(True)
                self.ui.fit_report_TE.setText(result.fit_report())
            elif self.ui.num_peaks_sb.value() == 5:
                vmodel = VoigtModel(prefix='p1_') + VoigtModel(prefix='p2_') + \
                         VoigtModel(prefix='p3_') + VoigtModel(prefix='p4_') + VoigtModel(prefix='p5_')
                params = Parameters()
                # add with tuples: (NAME VALUE VARY MIN  MAX  EXPR  BRUTE_STEP)
                params.add_many(('p1_amplitude', con[0][0], True, con[0][1], con[0][2]),
                                ('p1_center', con[0][3], True, con[0][4], con[0][5]),
                                ('p1_sigma', con[0][6], True, con[0][7], con[0][8]),
                                ('p2_amplitude', con[1][0], True, con[1][1], con[1][2]),
                                ('p2_center', con[1][3], True, con[1][4], con[1][5]),
                                ('p2_sigma', con[1][6], True, con[1][7], con[1][8]),
                                ('p3_amplitude', con[2][0], True, con[2][1], con[2][2]),
                                ('p3_center', con[2][3], True, con[2][4], con[2][5]),
                                ('p3_sigma', con[2][6], True, con[2][7], con[2][8]),
                                ('p4_amplitude', con[3][0], True, con[3][1], con[3][2]),
                                ('p4_center', con[3][3], True, con[3][4], con[3][5]),
                                ('p4_sigma', con[3][6], True, con[3][7], con[3][8]),
                                ('p5_amplitude', con[4][0], True, con[4][1], con[4][2]),
                                ('p5_center', con[4][3], True, con[4][4], con[4][5]),
                                ('p5_sigma', con[4][6], True, con[4][7], con[4][8]))
                result = vmodel.fit(self.data_y, params, x=self.data_x)
                comps = result.eval_components()
                ApplicationSettings.ALL_DATA_PLOTTED['V1'] = self.main_window.ax.plot(self.data_x,
                                                                                      comps['p1_'],
                                                                                      'k--', label='V1')
                ApplicationSettings.ALL_DATA_PLOTTED['V2'] = self.main_window.ax.plot(self.data_x,
                                                                                      comps['p2_'],
                                                                                      'k--', label='V2')
                ApplicationSettings.ALL_DATA_PLOTTED['V3'] = self.main_window.ax.plot(self.data_x,
                                                                                      comps['p3_'],
                                                                                      'k--', label='V3')
                ApplicationSettings.ALL_DATA_PLOTTED['V4'] = self.main_window.ax.plot(self.data_x,
                                                                                      comps['p4_'],
                                                                                      'k--', label='V4')
                ApplicationSettings.ALL_DATA_PLOTTED['V5'] = self.main_window.ax.plot(self.data_x,
                                                                                      comps['p5_'],
                                                                                      'k--', label='V5')
                ApplicationSettings.ALL_DATA_PLOTTED['Fit'] = self.main_window.ax.plot(self.data_x,
                                                                                       result.best_fit,
                                                                                       'r--', label='Result')
                self.ui.fit_report_TE.setText(result.fit_report())

        ApplicationSettings.ALL_DATA_PLOTTED['Y Data'] = self.main_window.ax.plot(self.data_x, self.data_y)
        self.ir_basic()

    def fitting_function_2(self):
        self.main_window.cleargraph()
        constraints = [[self.ui.p1_amp_sb.value(), self.ui.p1_ampl_sb.value(),self.ui.p1_amph_sb.value(),
                        self.ui.p1_cen_sb.value(), self.ui.p1_cenl_sb.value(), self.ui.p1_cenh_sb.value(),
                        self.ui.p1_sig_sb.value(), self.ui.p1_sigl_sb.value(), self.ui.p1_sigh_sb.value()],[self.ui.p2_amp_sb.value(), self.ui.p2_ampl_sb.value(), self.ui.p2_amph_sb.value(),
                        self.ui.p2_cen_sb.value(), self.ui.p2_cenl_sb.value(), self.ui.p2_cenh_sb.value(),
                        self.ui.p2_sig_sb.value(), self.ui.p2_sigl_sb.value(), self.ui.p2_sigh_sb.value()],[self.ui.p3_amp_sb.value(), self.ui.p3_ampl_sb.value(), self.ui.p3_amph_sb.value(),
                        self.ui.p3_cen_sb.value(), self.ui.p3_cenl_sb.value(), self.ui.p3_cenh_sb.value(),
                        self.ui.p3_sig_sb.value(), self.ui.p3_sigl_sb.value(), self.ui.p3_sigh_sb.value()],[self.ui.p4_amp_sb.value(), self.ui.p4_ampl_sb.value(), self.ui.p4_amph_sb.value(),
                        self.ui.p4_cen_sb.value(), self.ui.p4_cenl_sb.value(), self.ui.p4_cenh_sb.value(),
                        self.ui.p4_sig_sb.value(), self.ui.p4_sigl_sb.value(), self.ui.p4_sigh_sb.value()],[self.ui.p5_amp_sb.value(), self.ui.p5_ampl_sb.value(), self.ui.p5_amph_sb.value(),
                        self.ui.p5_cen_sb.value(), self.ui.p5_cenl_sb.value(), self.ui.p5_cenh_sb.value(),
                        self.ui.p5_sig_sb.value(), self.ui.p5_sigl_sb.value(), self.ui.p5_sigh_sb.value()]]
        fit_params = []
        checked = [self.ui.p1_cb.isChecked(),self.ui.p2_cb.isChecked(),self.ui.p3_cb.isChecked(),
                   self.ui.p4_cb.isChecked(),self.ui.p5_cb.isChecked()]
        # line_shapes = [self.ui.lineshape_1,self.ui.lineshape_2,self.ui.lineshape_3,self.ui.lineshape_4,self.ui.lineshape_5]
        line_shape_mods = [VoigtModel(prefix='p1_'),VoigtModel(prefix='p2_'),VoigtModel(prefix='p3_'),
                           VoigtModel(prefix='p4_'),VoigtModel(prefix='p5_')]
        cur_mods = []
        checked_peaks = []
        for x in range(1,6):
            if checked[x-1]:
                fit_params.append(('p%s_amplitude'% x,constraints[x-1][0],True,constraints[x-1][1],constraints[x-1][2]))
                fit_params.append(('p%s_center' % x,constraints[x-1][3],True,constraints[x-1][4],constraints[x-1][5]))
                fit_params.append(('p%s_sigma' % x,constraints[x-1][6],True,constraints[x-1][7],constraints[x-1][8]))
                checked_peaks.append(x-1)
                cur_mods.append(line_shape_mods[x-1])
        if len(checked_peaks) == 1:
            mod = cur_mods[0]
        elif len(checked_peaks) == 2:
            mod = cur_mods[0] + cur_mods[1]
        elif len(checked_peaks) == 3:
            mod = cur_mods[0] + cur_mods[1] +cur_mods[2]
        elif len(checked_peaks) == 4:
            mod = cur_mods[0] + cur_mods[1] + cur_mods[2] + cur_mods[3]
        elif len(checked_peaks) == 5:
            mod = cur_mods[0] + cur_mods[1] + cur_mods[2] + cur_mods[3] + cur_mods[4]

        params = Parameters()
        # add with tuples: (NAME VALUE VARY MIN  MAX  EXPR  BRUTE_STEP)
        for i in fit_params:
            params.add_many(i)
        result = mod.fit(self.data_y, params, x=self.data_x)
        self.ui.textEdit.setText(result.fit_report())
        ApplicationSettings.ALL_DATA_PLOTTED['Fit'] = \
            self.main_window.ax.plot(self.data_x, result.best_fit, 'r--', label='Result')
        ApplicationSettings.ALL_DATA_PLOTTED['Y Data'] = self.main_window.ax.plot(self.data_x, self.data_y)
        comps = result.eval_components()
        print(checked_peaks)
        for i in checked_peaks:
            ApplicationSettings.ALL_DATA_PLOTTED['Peak %s' % i] = \
                self.main_window.ax.plot(self.data_x, comps['p%s_' % str(i+1)])
        self.ir_basic()

    def select_data(self):
        def finish():
            key = ui.treeWidget.currentItem().text(0)
            if type(dict[key]) is list:
                self.data_x = dict[key][0]._xy.T[0]
                self.data_y = dict[key][0]._xy.T[1]
            else:
                self.data_x = dict[key]._xy.T[0]
                self.data_y = dict[key]._xy.T[1]
            x_lim = ApplicationSettings.C_X_LIM
            indexs = [find_nearest(self.data_x, x_lim[1]), find_nearest(self.data_x, x_lim[0])]
            self.data_x = self.data_x[indexs[0]:indexs[1]]
            self.data_y = self.data_y[indexs[0]:indexs[1]]
        dialog = QtWidgets.QDialog()
        ui = twDialog_ui()
        ui.setupUi(dialog)
        dict = ApplicationSettings.ALL_DATA_PLOTTED
        Key_List = []
        for i in dict.keys():
            Key_List.append(QtWidgets.QTreeWidgetItem([i]))
        ui.treeWidget.addTopLevelItems(Key_List)
        ui.buttonBox.accepted.connect(lambda: finish())
        dialog.exec_()

    def save_constraints(self):
        try:
            for row in range(9):
                for column in range(5):
                    self.constraints[column][row] = float(self.ui.tableWidget_2.item(row, column).text())
        except ValueError:
            print('No constraint save')

    def gaussian(self,x, amp, cen, sigma):
        return amp/(sigma*np.sqrt(2*np.pi))*np.exp(-(x-cen)**2/(2*sigma**2))

    def lorentz(self, x, amp, cen, sigma):
        return (amp/np.pi)*(1/2*sigma)/((x-cen)**2+(1/2*sigma)**2)

    def plot_init_2(self):
        self.main_window.cleargraph()
        model = self.gaussian
        peaks = None
        constraints = [[self.ui.p1_amp_sb.value(), self.ui.p1_ampl_sb.value(), self.ui.p1_amph_sb.value(),
                        self.ui.p1_cen_sb.value(), self.ui.p1_cenl_sb.value(), self.ui.p1_cenh_sb.value(),
                        self.ui.p1_sig_sb.value(), self.ui.p1_sigl_sb.value(), self.ui.p1_sigh_sb.value()],
                       [self.ui.p2_amp_sb.value(), self.ui.p2_ampl_sb.value(), self.ui.p2_amph_sb.value(),
                        self.ui.p2_cen_sb.value(), self.ui.p2_cenl_sb.value(), self.ui.p2_cenh_sb.value(),
                        self.ui.p2_sig_sb.value(), self.ui.p2_sigl_sb.value(), self.ui.p2_sigh_sb.value()],
                       [self.ui.p3_amp_sb.value(), self.ui.p3_ampl_sb.value(), self.ui.p3_amph_sb.value(),
                        self.ui.p3_cen_sb.value(), self.ui.p3_cenl_sb.value(), self.ui.p3_cenh_sb.value(),
                        self.ui.p3_sig_sb.value(), self.ui.p3_sigl_sb.value(), self.ui.p3_sigh_sb.value()],
                       [self.ui.p4_amp_sb.value(), self.ui.p4_ampl_sb.value(), self.ui.p4_amph_sb.value(),
                        self.ui.p4_cen_sb.value(), self.ui.p4_cenl_sb.value(), self.ui.p4_cenh_sb.value(),
                        self.ui.p4_sig_sb.value(), self.ui.p4_sigl_sb.value(), self.ui.p4_sigh_sb.value()],
                       [self.ui.p5_amp_sb.value(), self.ui.p5_ampl_sb.value(), self.ui.p5_amph_sb.value(),
                        self.ui.p5_cen_sb.value(), self.ui.p5_cenl_sb.value(), self.ui.p5_cenh_sb.value(),
                        self.ui.p5_sig_sb.value(), self.ui.p5_sigl_sb.value(), self.ui.p5_sigh_sb.value()]]

        checked = [self.ui.p1_cb.isChecked(), self.ui.p2_cb.isChecked(), self.ui.p3_cb.isChecked(),
                   self.ui.p4_cb.isChecked(), self.ui.p5_cb.isChecked()]
        for i in range(5):
            if checked[i]:
                if peaks is None:
                    peaks = model(self.data_x,constraints[i][0],constraints[i][3],constraints[i][6])
                else:
                    peaks = model(self.data_x, constraints[i][0], constraints[i][3], constraints[i][6]) + peaks

        ApplicationSettings.ALL_DATA_PLOTTED['Y_Data'] = self.main_window.ax.plot(self.data_x,self.data_y)
        ApplicationSettings.ALL_DATA_PLOTTED['FTIR Init Values'] = self.main_window.ax.plot(self.data_x,peaks, '--k')
        self.ir_basic()

    def plot_init(self):
        self.main_window.cleargraph()
        if self.ui.fit_shape_cb.currentText() == 'Lorentz':
            model = self.lorentz
        else:
            model = self.gaussian
        con = self.constraints
        if self.ui.num_peaks_sb.value() == 1:
            start_plot = model(self.data_x,con[0][0],con[0][3],con[0][6])
        elif self.ui.num_peaks_sb.value() == 2:
            start_plot = model(self.data_x, con[0][0], con[0][3], con[0][6])+\
                         model(self.data_x, con[1][0], con[1][3], con[1][6])
        elif self.ui.num_peaks_sb.value() == 3:
            start_plot = model(self.data_x, con[0][0], con[0][3], con[0][6])+\
                         model(self.data_x, con[1][0], con[1][3], con[1][6])+\
                         model(self.data_x, con[2][0], con[2][3], con[2][6])
        elif self.ui.num_peaks_sb.value() == 4:
            start_plot = model(self.data_x, con[0][0], con[0][3], con[0][6]) + \
                         model(self.data_x, con[1][0], con[1][3], con[1][6]) + \
                         model(self.data_x, con[2][0], con[2][3], con[2][6]) + \
                         model(self.data_x, con[3][0], con[3][3], con[3][6])
        elif self.ui.num_peaks_sb.value() == 5:
            start_plot = model(self.data_x, con[0][0], con[0][3], con[0][6]) + \
                         model(self.data_x, con[1][0], con[1][3], con[1][6]) + \
                         model(self.data_x, con[2][0], con[2][3], con[2][6]) + \
                         model(self.data_x, con[3][0], con[3][3], con[3][6]) + \
                         model(self.data_x, con[4][0], con[4][3], con[4][6])


        ApplicationSettings.ALL_DATA_PLOTTED['Y_Data'] = self.main_window.ax.plot(self.data_x,self.data_y)
        ApplicationSettings.ALL_DATA_PLOTTED['FTIR Init Values'] = \
            self.main_window.ax.plot(self.data_x,start_plot, '--k')
        self.ir_basic()

    def ir_plot(self,type):
        path = self.model.filePath(self.tree_view.currentIndex())
        head, tail = os.path.split(path)
        if type == 'spectra':
            temp = pd.read_csv(path,delimiter=',')
            self.data = temp.to_numpy().T
            # self.data = np.genfromtxt(path,delimiter=',').T
            ApplicationSettings.ALL_DATA_PLOTTED[tail] = self.main_window.ax.plot(
                self.data[0],self.data[1],label=tail)
        elif type == 'sub':
            if os.path.isdir(path):
                csv_list = sorted(glob.glob(path + '/*CSV'))
                self.sub = self.subtraction_from_survey(csv_list)
                for i in range(0,len(self.sub)-1,self.ui.skip_sb.value()+1):
                    ApplicationSettings.ALL_DATA_PLOTTED['Sub_'+str(i)] = \
                        self.main_window.ax.plot(self.sub[0],self.sub[i+1],label='Sub_'+str(i))
        elif type == 'diff':
            if os.path.isdir(path):
                csv_list = sorted(glob.glob(path + '/*CSV'))
                self.diff = self.difference_from_survey(csv_list)
                for i in range(0,len(self.diff)-1,self.ui.skip_sb.value()+1):
                    try:
                        ApplicationSettings.ALL_DATA_PLOTTED['Diff_'+str(i)] = \
                            self.main_window.ax.plot(self.diff[0],self.diff[i+1],label='Diff_'+str(i))
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
                        self.main_window.ax.plot(self.data[0],self.data[j+1])
        elif type == 'diff2':
            paths = [self.model.filePath(self.tree_view.selectedIndexes()[0]),
                     self.model.filePath(self.tree_view.selectedIndexes()[5])]
            temp1 = pd.read_csv(paths[0],delimiter=',').to_numpy().T
            temp2 = pd.read_csv(paths[1],delimiter=',').to_numpy().T
            self.data = [temp1[0],temp1[1]-temp2[1]]
            print(self.data)
            ApplicationSettings.ALL_DATA_PLOTTED[tail] = self.main_window.ax.plot(
                self.data[0], self.data[1], label=tail)

        self.ir_basic()

    def ir_basic(self):
        limits = self.main_window.ax.get_xlim()
        if limits[1] > limits[0]:
            self.main_window.ax.set_xlim(self.main_window.ax.get_xlim()[::-1])
        self.main_window.ax.set_xlabel('Wavenumber ($cm^{-1}$)')
        self.main_window.ax.set_ylabel('Absorbance')
        self.main_window.fig.tight_layout()
        self.main_window.canvas.draw()

    def integrate(self):
        # dict = ApplicationSettings.ALL_DATA_PLOTTED
        # Key_List = []
        # data = []
        # index = 0
        # for i in dict.keys():
        #     if index == 0:
        #         data.append(dict[i][0]._xy.T[0])
        #         index += 1
        #     Key_List.append(i)
        #     data.append(dict[i][0]._xy.T[1])
        # inte = self.integrate_ir(data, self.ui.min_sb.value(), self.ui.max_sb.value())
        # self.main_window.ax.plot(inte, '.-', label=str(np.round(self.ui.min_sb.value(), 4)) + '-' +
        #                                              str(np.round(self.ui.max_sb.value(), 4)))
        # self.main_window.canvas.draw()
        path = self.model.filePath(self.tree_view.currentIndex())
        csv_list = sorted(glob.glob(path + '/*CSV'))
        # self.sub = self.subtraction_from_survey(csv_list)
        # min_max = [[400,4000],[400,4000],[400,4000],[400,4000]]
        # labels = ['','','','']
        # for row in range(4):
        #     labels[row] = self.ui.tableWidget.item(row, 2).text()
        #     for column in range(2):
        #         min_max[row][column] = float(self.ui.tableWidget.item(row,column).text())
        # print(labels)
        # minimum = float(self.ui.tableWidget.item(0,0).text())
        # maximum = float(self.ui.tableWidget.item(0, 1).text())
        # num_of_int = self.ui.spinBox.value()

        if self.ui.leftrightaxis_cb.currentText()=='Left Axis':
            ax = self.main_window.ax
        elif self.ui.leftrightaxis_cb.currentText()=='Right Axis':
            if self.main_window.ax_2 is None:
                self.main_window.ax_2 = self.main_window.ax.twinx()
            ax = self.main_window.ax_2
        if self.ui.int_type_cb.currentText() == 'Absolute':
            print('Passed')
        elif self.ui.int_type_cb.currentText() == 'Subtraction_C':
            # for i in range(num_of_int):
            self.sub = self.subtraction_from_survey(csv_list)
            inte = self.integrate_ir(self.sub, self.ui.min_sb.value(), self.ui.max_sb.value())
            inte_c = [i-inte[0] for i in inte]
            ApplicationSettings.ALL_DATA_PLOTTED['Int. ' + str(self.ui.min_sb.value()) + '-' + str(self.ui.max_sb.value())] = \
                ax.plot(inte_c, '.-', label=str(self.ui.min_sb.value()) + '-' + str(self.ui.max_sb.value()))
        elif self.ui.int_type_cb.currentText() == 'Subtraction':
            # for i in range(num_of_int):

            self.sub = self.subtraction_from_survey(csv_list)
            inte = self.integrate_ir(self.sub, self.ui.min_sb.value(), self.ui.max_sb.value())
        elif self.ui.int_type_cb.currentText() == 'Difference':
            # for i in range(num_of_int):
            self.diff = self.difference_from_survey(csv_list)
            inte = self.integrate_ir(self.diff, self.ui.min_sb.value(), self.ui.max_sb.value())
        if self.ui.xaxis_cb.currentText() == 'Ints':
            x = np.linspace(1, len(inte), len(inte))
        elif self.ui.xaxis_cb.currentText() == 'Half-Ints':
            x = np.linspace(0.5, len(inte)/2, len(inte))
        ApplicationSettings.ALL_DATA_PLOTTED[
            'Int. ' + str(self.ui.min_sb.value()) + '-' + str(self.ui.max_sb.value())] = \
            ax.plot(x,inte, '.-', label='Int. ' + str(self.ui.min_sb.value()) + '-' + str(self.ui.max_sb.value()))
        self.main_window.canvas.draw()

    def smooth(self):
        dict = ApplicationSettings.ALL_DATA_PLOTTED
        Key_List = []
        data = []
        index = 0
        for i in dict.keys():
            if index == 0:
                data.append(dict[i][0]._xy.T[0])
                index += 1
            Key_List.append(i)
            data.append(dict[i][0]._xy.T[1])
        self.main_window.cleargraph()
        for i in range(len(Key_List)):
            ApplicationSettings.ALL_DATA_PLOTTED[str(i)+'_sm'] = self.main_window.ax.plot(
                data[0],savgol_filter(data[i+1], self.ui.smooth_sb.value(), 3))
        self.ir_basic()

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

    def difference_from_survey(self,list_of_csv):
        data = []
        for csv in list_of_csv:
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
        return sub_list

    def subtraction_from_survey(self,list_of_csv):
        data = []
        for csv in list_of_csv:
            data.append(np.genfromtxt(csv, delimiter=',').T)
        sub_list = [data[0][0]]
        for l in range(len(data) - 1):
            length = len(data[0][0])
            sub_list.append(data[l + 1][1][:length] - data[0][1][:length])
        return sub_list

    def diff_select_survey(self,list_of_csv):
        def finish():
            data = []
            for csv in list_of_csv:
                data.append(np.genfromtxt(csv, delimiter=',').T)
            sub_list = [data[0][0]]
            for l in range(len(data) - 1):
                sub_list.append(data[l + 1][1] - data[l][1])
            return sub_list

        dialog = QtWidgets.QDialog()
        ui = simple_tw()
        ui.setupUi(dialog)
        Key_List = []
        for i in list_of_csv:
            Key_List.append(QtWidgets.QTreeWidgetItem([i]))
        ui.treeWidget.addTopLevelItems(Key_List)
        ui.buttonBox.accepted.connect(lambda: finish())
        dialog.exec_()

    def integrate_ir(self, data, minimum, maximum):
        integral_list = []
        lim = [min(range(len(data[0])), key=lambda i: abs(data[0][i] - minimum)),
               min(range(len(data[0])), key=lambda i: abs(data[0][i] - maximum))]
        for numb in range(len(data) - 1):
            integral_list.append(integrate.trapz(data[numb + 1][lim[0]:lim[1]], data[0][lim[0]:lim[1]]))
        return integral_list

    def integrate_mode(self, enabled):
        if enabled:
            self.span = SpanSelector(self.main_window.ax, self.onselect, 'horizontal', useblit=True,
                                     rectprops=dict(alpha=0.2, facecolor='red'))
        else:
            del self.span

    def onselect(self, minimum, maximum):
        dict = ApplicationSettings.ALL_DATA_PLOTTED
        Key_List = []
        data = []
        index = 0
        for i in dict.keys():
            if index == 0:
                data.append(dict[i][0]._xy.T[0])
                index += 1
            Key_List.append(i)
            data.append(dict[i][0]._xy.T[1])
        # print(Key_List)
        inte = self.integrate_ir(data, minimum, maximum)
        self.main_window.ax_2.plot(inte, '.-', label=str(np.round(minimum,1)) + '-' + str(np.round(maximum,1)))
        self.main_window.canvas.draw()
        col_count = self.ui.tableWidget.columnCount()
        self.ui.tableWidget.setColumnCount(col_count+1)
        row_count = self.ui.tableWidget.rowCount()
        if len(inte) > row_count:
            self.ui.tableWidget.setRowCount(len(inte))
        for i in range(len(inte)):
            self.ui.tableWidget.setItem(i,col_count,QtWidgets.QTableWidgetItem(str(inte[i])))

class IR_Fit_Object(object):
    def __init__(self, x_data, y_data, minimum, maximum):
        self.peak_constraints = []
        self.constraints = []
        self.peak_type = {}
        self.peak_fitted_values = {}
        self.shirley = None
        self.x_data = x_data
        self.y_data = y_data
        self.mini = minimum
        self.maxi = maximum
        self.init_constraints(minimum, maximum)
        self.fit_result = None

    def init_constraints(self, minimum, maximum):
        middle = minimum + (maximum-minimum)/2
        centers = [middle for i in range(8)]
        for i in range(8):
            self.peak_constraints.append([[5000, 0, 999999], [centers[i], minimum, maximum],[1,.0001,10]])

    def fit(self, checked, cons, vghold, vgratio, holds):
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
                params.add_many(('p%s_amplitude' % str(x), self.peak_constraints[x][0][0], holds[x][0], self.peak_constraints[x][0][1], self.peak_constraints[x][0][2]),
                                ('p%s_center' % str(x), self.peak_constraints[x][1][0], holds[x][1], self.peak_constraints[x][1][1], self.peak_constraints[x][1][2]),
                                ('p%s_sigma' % str(x), self.peak_constraints[x][2][0], holds[x][2], self.peak_constraints[x][2][1], self.peak_constraints[x][2][2]),
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
        return result
