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
        self._init_widgets()
        self._init_UI()

    def _init_vars(self):
        self.current_data_container = None
        self.data = None
        self.shirley = None
        self.model = None
        self.x_data = None
        self.y_data = None
        self.constraints = np.asarray([[100000,0,9999999,285,0,4000,2,.001,4],[100000,0,9999999,285,0,4000,2,.001,4],
                                       [100000,0,9999999,100,0,4000,2,.001,4],[100000,0,9999999,100,0,4000,2,.001,4],
                                       [100000,0,9999999,100,0,4000,2,.001,4]])
        self.con_2 = []
        for row in range(9):
            for column in range(5):
                self.ui.tableWidget.setItem(row,column,QtWidgets.QTableWidgetItem(str(self.constraints[column][row])))
        self.fit_obj = {}

    def _init_widgets(self):
        self.tree_view = self.ui.XPS_treeView
        self.context_menu = QtWidgets.QMenu(self)
        # Create context menu
        rc_browser_options(self)

    def _init_UI(self):
        self.model = QtWidgets.QFileSystemModel()
        self.model.setRootPath('')

        self.tree_view.setModel(self.model)
        self.tree_view.setSortingEnabled(True)

        self.tree_view.sortByColumn(True)
        self.tree_view.setRootIndex(self.model.index(self.main_window.settings.value('XPS_PATH')))

        self.tree_view.setModel(self.model)
        self.tree_view.installEventFilter(self)
        self.tree_view.setColumnWidth(0, 200)

        # self.peak_num_changed()

        self.ui.plot_pb.clicked.connect(lambda: self.plot())
        # self.ui.fit_pb.clicked.connect(lambda: self.fit_fun())
        # self.ui.shirley_pb.clicked.connect(lambda: self.shirley_fun())
        # self.ui.num_peaks_sb.valueChanged.connect(lambda: self.sb_change())
        # self.ui.tableWidget.cellChanged.connect(lambda: self.save_constraints())
        # self.ui.plot_curr_pb.clicked.connect(lambda: self.plot_init())
        self.ui.fill_cols_pb.clicked.connect(lambda: self.fill_cols())
        self.ui.xpsrange_rb.toggled.connect(self.select_xps_range)
        self.ui.fit_range_cb.currentIndexChanged.connect(lambda: self.fit_range_changed())
        self.ui.fit_pb_2.clicked.connect(lambda: self.fit_fun_2())

    def eventFilter(self, object, event):
        # For right click events
        if event.type() == QtCore.QEvent.ContextMenu:
            self.context_menu.exec_(self.mapToGlobal(event.pos()))
        return False

    # def shirley_fun(self):
    #     self.save_constraints()
    #     self.main_window.cleargraph()
    #     x_lim = ApplicationSettings.C_X_LIM
    #     print(x_lim)
    #     #  Y is data[0]..... whyyyyyyy x is data[1]
    #     # self.data = np.flip(ApplicationSettings.CURRENT_PLOT[0].get_data())
    #     # self.data = np.flip(self.data)
    #     indexs = [find_nearest(self.x_data, x_lim[0]), find_nearest(self.x_data, x_lim[1])]
    #     self.x_data = self.x_data[indexs[0]:indexs[1]]
    #     self.y_data = self.y_data[indexs[0]:indexs[1]]
    #     ApplicationSettings.ALL_DATA_PLOTTED['y_data'] = self.main_window.ax.plot(self.x_data,self.y_data)
    #     self.shirley = self.shirley_calculate(self.x_data, self.y_data)
    #     ApplicationSettings.ALL_DATA_PLOTTED['Shirley'] = self.main_window.ax.plot(self.x_data, self.shirley, '.k', markersize=2)
    #     self.xps_basic()
    #     self.main_window.canvas.draw()

    # def fit_fun(self):
    #     self.main_window.cleargraph()
    #     self.save_constraints()
    #     con = self.constraints
    #     #  Y is data[0]..... whyyyyyyy x is data[1]
    #     if self.ui.fit_shape_cb.currentText() == 'Gaussian':
    #         if self.ui.num_peaks_sb.value()==1:
    #             gmodel = GaussianModel()
    #             params = Parameters()
    #             # add with tuples: (NAME VALUE VARY MIN  MAX  EXPR  BRUTE_STEP)
    #             params.add_many(('amplitude', con[0][0], True, con[0][1], con[0][2]),
    #                             ('center', con[0][3], True, con[0][4], con[0][5]),
    #                             ('sigma', con[0][6], True, con[0][7], con[0][8]))
    #             result = gmodel.fit(self.y_data-self.shirley, params, x=self.x_data)
    #             self.ui.fit_report_TE.setText(result.fit_report())
    #             ApplicationSettings.ALL_DATA_PLOTTED['Shirley'] = self.main_window.ax.plot(self.x_data,self.shirley,'k--',label='Shirley')
    #             ApplicationSettings.ALL_DATA_PLOTTED['Fit'] =self.main_window.ax.plot(self.x_data, result.best_fit+self.shirley,'r--',label='Result')
    #
    #         elif self.ui.num_peaks_sb.value() == 2:
    #             gmodel = GaussianModel(prefix='p1_') + GaussianModel(prefix='p2_')
    #             params = Parameters()
    #             # add with tuples: (NAME VALUE VARY MIN  MAX  EXPR  BRUTE_STEP)
    #             params.add_many(('p1_amplitude', con[0][0],True,con[0][1],con[0][2]),
    #                             ('p1_center', con[0][3],True,con[0][4],con[0][5]),
    #                             ('p1_sigma', con[0][6],True,con[0][7],con[0][8]),
    #                             ('p2_amplitude', con[1][0],True,con[1][1],con[1][2]),
    #                             ('p2_center', con[1][3],True,con[1][4],con[1][5]),
    #                             ('p2_sigma', con[1][6],True,con[1][7],con[1][8]))
    #             result = gmodel.fit(self.y_data - self.shirley, params, x=self.x_data)
    #             comps = result.eval_components()
    #             self.ui.fit_report_TE.setText(result.fit_report())
    #             ApplicationSettings.ALL_DATA_PLOTTED['Shirley'] = self.main_window.ax.plot(self.x_data,self.shirley,'k--',label='Shirley')
    #             ApplicationSettings.ALL_DATA_PLOTTED['G1'] = self.main_window.ax.plot(self.x_data,self.shirley+comps['p1_'],'k--',label='G1')
    #             ApplicationSettings.ALL_DATA_PLOTTED['G2'] = self.main_window.ax.plot(self.x_data,self.shirley+comps['p2_'],'k--',label='G2')
    #             ApplicationSettings.ALL_DATA_PLOTTED['Fit'] = self.main_window.ax.plot(self.x_data, result.best_fit + self.shirley,'r--',label='Result')
    #             leg = self.main_window.ax.legend(loc='best', fontsize='small')
    #             leg.set_draggable(True)
    #
    #         elif self.ui.num_peaks_sb.value() == 3:
    #             gmodel = GaussianModel(prefix='p1_') + GaussianModel(prefix='p2_')+Model(prefix='p3_')
    #             params = Parameters()
    #             # add with tuples: (NAME VALUE VARY MIN  MAX  EXPR  BRUTE_STEP)
    #             params.add_many(('p1_amplitude', con[0][0],True,con[0][1],con[0][2]),
    #                             ('p1_center', con[0][3],True,con[0][4],con[0][5]),
    #                             ('p1_sigma', con[0][6],True,con[0][7],con[0][8]),
    #                             ('p2_amplitude', con[1][0],True,con[1][1],con[1][2]),
    #                             ('p2_center', con[1][3],True,con[1][4],con[1][5]),
    #                             ('p2_sigma', con[1][6],True,con[1][7],con[1][8]),
    #                             ('p3_amplitude', con[2][0], True, con[2][1], con[2][2]),
    #                             ('p3_center', con[2][3], True, con[2][4], con[2][5]),
    #                             ('p3_sigma', con[2][6], True, con[2][7], con[2][8]))
    #             result = gmodel.fit(self.y_data - self.shirley, params, x=self.x_data)
    #             comps = result.eval_components()
    #             ApplicationSettings.ALL_DATA_PLOTTED['Shirley'] = self.main_window.ax.plot(self.x_data,self.shirley,'k--',label='Shirley')
    #             ApplicationSettings.ALL_DATA_PLOTTED['G1'] = self.main_window.ax.plot(self.x_data,self.shirley+comps['p1_'],'k--',label='G1')
    #             ApplicationSettings.ALL_DATA_PLOTTED['G2'] = self.main_window.ax.plot(self.x_data,self.shirley+comps['p2_'],'k--',label='G2')
    #             ApplicationSettings.ALL_DATA_PLOTTED['G3'] = self.main_window.ax.plot(self.x_data,self.shirley+comps['p3_'],'k--',label='G3')
    #             ApplicationSettings.ALL_DATA_PLOTTED['Fit'] = self.main_window.ax.plot(self.x_data, result.best_fit + self.shirley,'r--',label='Result')
    #             self.ui.fit_report_TE.setText(result.fit_report())
    #
    #         elif self.ui.num_peaks_sb.value() == 4:
    #             gmodel = GaussianModel(prefix='p1_') + GaussianModel(prefix='p2_') + \
    #                      GaussianModel(prefix='p3_') + GaussianModel(prefix='p4_')
    #             params = Parameters()
    #             # add with tuples: (NAME VALUE VARY MIN  MAX  EXPR  BRUTE_STEP)
    #             params.add_many(('p1_amplitude', con[0][0], True, con[0][1], con[0][2]),
    #                             ('p1_center', con[0][3], True, con[0][4], con[0][5]),
    #                             ('p1_sigma', con[0][6], True, con[0][7], con[0][8]),
    #                             ('p2_amplitude', con[1][0], True, con[1][1], con[1][2]),
    #                             ('p2_center', con[1][3], True, con[1][4], con[1][5]),
    #                             ('p2_sigma', con[1][6], True, con[1][7], con[1][8]),
    #                             ('p3_amplitude', con[2][0], True, con[2][1], con[2][2]),
    #                             ('p3_center', con[2][3], True, con[2][4], con[2][5]),
    #                             ('p3_sigma', con[2][6], True, con[2][7], con[2][8]),
    #                             ('p4_amplitude', con[3][0], True, con[3][1], con[3][2]),
    #                             ('p4_center', con[3][3], True, con[3][4], con[3][5]),
    #                             ('p4_sigma', con[3][6], True, con[3][7], con[3][8]))
    #             result = gmodel.fit(self.y_data - self.shirley, params, x=self.x_data)
    #             comps = result.eval_components()
    #             ApplicationSettings.ALL_DATA_PLOTTED['Shirley'] = self.main_window.ax.plot(self.x_data, self.shirley, 'k--', label='Shirley')
    #             ApplicationSettings.ALL_DATA_PLOTTED['G1'] = self.main_window.ax.plot(self.x_data, self.shirley + comps['p1_'], 'k--', label='G1')
    #             ApplicationSettings.ALL_DATA_PLOTTED['G2'] = self.main_window.ax.plot(self.x_data, self.shirley + comps['p2_'], 'k--', label='G2')
    #             ApplicationSettings.ALL_DATA_PLOTTED['G3'] = self.main_window.ax.plot(self.x_data, self.shirley + comps['p3_'], 'k--', label='G3')
    #             ApplicationSettings.ALL_DATA_PLOTTED['G4'] = self.main_window.ax.plot(self.x_data, self.shirley + comps['p4_'], 'k--', label='G4')
    #             ApplicationSettings.ALL_DATA_PLOTTED['Fit'] = self.main_window.ax.plot(self.x_data, result.best_fit + self.shirley, 'r--', label='Result')
    #             leg = self.main_window.ax.legend(loc='best',fontsize='small')
    #             leg.set_draggable(True)
    #             self.ui.fit_report_TE.setText(result.fit_report())
    #
    #         elif self.ui.num_peaks_sb.value() == 5:
    #
    #             gmodel = GaussianModel(prefix='p1_') + GaussianModel(prefix='p2_') + \
    #                      GaussianModel(prefix='p3_') + GaussianModel(prefix='p4_') + GaussianModel(prefix='p5_')
    #             params = Parameters()
    #             # add with tuples: (NAME VALUE VARY MIN  MAX  EXPR  BRUTE_STEP)
    #             params.add_many(('p1_amplitude', con[0][0], True, con[0][1], con[0][2]),
    #                             ('p1_center', con[0][3], True, con[0][4], con[0][5]),
    #                             ('p1_sigma', con[0][6], True, con[0][7], con[0][8]),
    #                             ('p2_amplitude', con[1][0], True, con[1][1], con[1][2]),
    #                             ('p2_center', con[1][3], True, con[1][4], con[1][5]),
    #                             ('p2_sigma', con[1][6], True, con[1][7], con[1][8]),
    #                             ('p3_amplitude', con[2][0], True, con[2][1], con[2][2]),
    #                             ('p3_center', con[2][3], True, con[2][4], con[2][5]),
    #                             ('p3_sigma', con[2][6], True, con[2][7], con[2][8]),
    #                             ('p4_amplitude', con[3][0], True, con[3][1], con[3][2]),
    #                             ('p4_center', con[3][3], True, con[3][4], con[3][5]),
    #                             ('p4_sigma', con[3][6], True, con[3][7], con[3][8]),
    #                             ('p5_amplitude', con[4][0], True, con[4][1], con[4][2]),
    #                             ('p5_center', con[4][3], True, con[4][4], con[4][5]),
    #                             ('p5_sigma', con[4][6], True, con[4][7], con[4][8]))
    #             result = gmodel.fit(self.y_data - self.shirley, params, x=self.x_data)
    #             comps = result.eval_components()
    #             ApplicationSettings.ALL_DATA_PLOTTED['Shirley'] = self.main_window.ax.plot(self.x_data, self.shirley, 'k--', label='Shirley')
    #             ApplicationSettings.ALL_DATA_PLOTTED['G1'] =self.main_window.ax.plot(self.x_data, self.shirley + comps['p1_'], 'k--', label='G1')
    #             ApplicationSettings.ALL_DATA_PLOTTED['G2'] =self.main_window.ax.plot(self.x_data, self.shirley + comps['p2_'], 'k--', label='G2')
    #             ApplicationSettings.ALL_DATA_PLOTTED['G3'] =self.main_window.ax.plot(self.x_data, self.shirley + comps['p3_'], 'k--', label='G3')
    #             ApplicationSettings.ALL_DATA_PLOTTED['G4'] =self.main_window.ax.plot(self.x_data, self.shirley + comps['p4_'], 'k--', label='G4')
    #             ApplicationSettings.ALL_DATA_PLOTTED['G5'] = self.main_window.ax.plot(self.x_data,self.shirley + comps['p5_'],'k--', label='G5')
    #             ApplicationSettings.ALL_DATA_PLOTTED['Fit'] =self.main_window.ax.plot(self.x_data, result.best_fit + self.shirley, 'r--', label='Result')
    #             self.ui.fit_report_TE.setText(result.fit_report())
    #
    #     elif self.ui.fit_shape_cb.currentText() == 'Lorentz':
    #         if self.ui.num_peaks_sb.value() == 1:
    #             lmodel = LorentzianModel()
    #             params = Parameters()
    #             # add with tuples: (NAME VALUE VARY MIN  MAX  EXPR  BRUTE_STEP)
    #             params.add_many(('amplitude', con[0][0], True, con[0][1], con[0][2]),
    #                             ('center', con[0][3], True, con[0][4], con[0][5]),
    #                             ('sigma', con[0][6], True, con[0][7], con[0][8]), )
    #             result = lmodel.fit(self.y_data - self.shirley, params, x=self.x_data)
    #             self.ui.fit_report_TE.setText(result.fit_report())
    #             ApplicationSettings.ALL_DATA_PLOTTED['Shirley'] = self.main_window.ax.plot(self.x_data, self.shirley,
    #                                                                                        'k--', label='Shirley')
    #             ApplicationSettings.ALL_DATA_PLOTTED['Fit'] = self.main_window.ax.plot(self.x_data,
    #                                                                                    result.best_fit + self.shirley,
    #                                                                                    'r--', label='Result')
    #             leg = self.main_window.ax.legend(loc='best', fontsize='small')
    #             leg.set_draggable(True)
    #         elif self.ui.num_peaks_sb.value() == 2:
    #             lmodel = LorentzianModel(prefix='p1_') + LorentzianModel(prefix='p2_')
    #             params = Parameters()
    #             # add with tuples: (NAME VALUE VARY MIN  MAX  EXPR  BRUTE_STEP)
    #             params.add_many(('p1_amplitude', con[0][0], True, con[0][1], con[0][2]),
    #                             ('p1_center', con[0][3], True, con[0][4], con[0][5]),
    #                             ('p1_sigma', con[0][6], True, con[0][7], con[0][8]),
    #                             ('p2_amplitude', con[1][0], True, con[1][1], con[1][2]),
    #                             ('p2_center', con[1][3], True, con[1][4], con[1][5]),
    #                             ('p2_sigma', con[1][6], True, con[1][7], con[1][8]))
    #             result = lmodel.fit(self.y_data - self.shirley, params, x=self.x_data)
    #             comps = result.eval_components()
    #             self.ui.fit_report_TE.setText(result.fit_report())
    #             ApplicationSettings.ALL_DATA_PLOTTED['Shirley'] = self.main_window.ax.plot(self.x_data, self.shirley,
    #                                                                                        'k--', label='Shirley')
    #             ApplicationSettings.ALL_DATA_PLOTTED['L1'] = self.main_window.ax.plot(self.x_data,
    #                                                                                   self.shirley + comps['p1_'],
    #                                                                                   'k--', label='L1')
    #             ApplicationSettings.ALL_DATA_PLOTTED['L2'] = self.main_window.ax.plot(self.x_data,
    #                                                                                   self.shirley + comps['p2_'],
    #                                                                                   'k--', label='L2')
    #             ApplicationSettings.ALL_DATA_PLOTTED['Fit'] = self.main_window.ax.plot(self.x_data,
    #                                                                                    result.best_fit + self.shirley,
    #                                                                                    'r--', label='Result')
    #             leg = self.main_window.ax.legend(loc='best', fontsize='small')
    #             leg.set_draggable(True)
    #
    #     elif self.ui.fit_shape_cb.currentText() == 'Voigt':
    #         if self.ui.num_peaks_sb.value() == 1:
    #             vmodel = VoigtModel()
    #             params = Parameters()
    #             params.add_many(('amplitude', con[0][0], True, con[0][1], con[0][2]),
    #                             ('center', con[0][3], True, con[0][4], con[0][5]),
    #                             ('sigma', con[0][6], True, con[0][7], con[0][8]))
    #             result = vmodel.fit(self.y_data - self.shirley, params, x=self.x_data)
    #             self.ui.fit_report_TE.setText(result.fit_report())
    #             ApplicationSettings.ALL_DATA_PLOTTED['Shirley'] = self.main_window.ax.plot(self.x_data, self.shirley,
    #                                                                                        'k--', label='Shirley')
    #             ApplicationSettings.ALL_DATA_PLOTTED['Fit'] = self.main_window.ax.plot(self.x_data,
    #                                                                                    result.best_fit + self.shirley,
    #                                                                                    'r--', label='Result')
    #         elif self.ui.num_peaks_sb.value() == 2:
    #             vmodel = VoigtModel(prefix='p1_') + VoigtModel(prefix='p2_')
    #             params = Parameters()
    #             # add with tuples: (NAME VALUE VARY MIN  MAX  EXPR  BRUTE_STEP)
    #             params.add_many(('p1_amplitude', con[0][0], True, con[0][1], con[0][2]),
    #                             ('p1_center', con[0][3], True, con[0][4], con[0][5]),
    #                             ('p1_sigma', con[0][6], True, con[0][7], con[0][8]),
    #                             ('p2_amplitude', con[1][0], True, con[1][1], con[1][2]),
    #                             ('p2_center', con[1][3], True, con[1][4], con[1][5]),
    #                             ('p2_sigma', con[1][6], True, con[1][7], con[1][8]))
    #             result = vmodel.fit(self.y_data - self.shirley, params, x=self.x_data)
    #             comps = result.eval_components()
    #             self.ui.fit_report_TE.setText(result.fit_report())
    #             ApplicationSettings.ALL_DATA_PLOTTED['Shirley'] = self.main_window.ax.plot(self.x_data, self.shirley,
    #                                                                                        'k--', label='Shirley')
    #             ApplicationSettings.ALL_DATA_PLOTTED['V1'] = self.main_window.ax.plot(self.x_data,
    #                                                                                   self.shirley + comps['p1_'],
    #                                                                                   'k--', label='_V1')
    #             ApplicationSettings.ALL_DATA_PLOTTED['V2'] = self.main_window.ax.plot(self.x_data,
    #                                                                                   self.shirley + comps['p2_'],
    #                                                                                   'k--', label='_V2')
    #             ApplicationSettings.ALL_DATA_PLOTTED['Fit'] = self.main_window.ax.plot(self.x_data,
    #                                                                                    result.best_fit + self.shirley,
    #                                                                                    'r--', label='Result')
    #         elif self.ui.num_peaks_sb.value() == 3:
    #             vmodel = VoigtModel(prefix='p1_') + VoigtModel(prefix='p2_') + VoigtModel(prefix='p3_')
    #             params = Parameters()
    #             # add with tuples: (NAME VALUE VARY MIN  MAX  EXPR  BRUTE_STEP)
    #             params.add_many(('p1_amplitude', con[0][0], True, con[0][1], con[0][2]),
    #                             ('p1_center', con[0][3], True, con[0][4], con[0][5]),
    #                             ('p1_sigma', con[0][6], True, con[0][7], con[0][8]),
    #                             ('p2_amplitude', con[1][0], True, con[1][1], con[1][2]),
    #                             ('p2_center', con[1][3], True, con[1][4], con[1][5]),
    #                             ('p2_sigma', con[1][6], True, con[1][7], con[1][8]),
    #                             ('p3_amplitude', con[2][0], True, con[2][1], con[2][2]),
    #                             ('p3_center', con[2][3], True, con[2][4], con[2][5]),
    #                             ('p3_sigma', con[2][6], True, con[2][7], con[2][8]))
    #             result = vmodel.fit(self.y_data - self.shirley, params, x=self.x_data)
    #             comps = result.eval_components()
    #             ApplicationSettings.ALL_DATA_PLOTTED['Shirley'] = self.main_window.ax.plot(self.x_data, self.shirley,
    #                                                                                        'k--', label='Shirley')
    #             ApplicationSettings.ALL_DATA_PLOTTED['V1'] = self.main_window.ax.plot(self.x_data,
    #                                                                                   self.shirley + comps['p1_'],
    #                                                                                   'k--', label='_V1')
    #             ApplicationSettings.ALL_DATA_PLOTTED['V2'] = self.main_window.ax.plot(self.x_data,
    #                                                                                   self.shirley + comps['p2_'],
    #                                                                                   'k--', label='_V2')
    #             ApplicationSettings.ALL_DATA_PLOTTED['V3'] = self.main_window.ax.plot(self.x_data,
    #                                                                                   self.shirley + comps['p3_'],
    #                                                                                   'k--', label='_V3')
    #             ApplicationSettings.ALL_DATA_PLOTTED['Fit'] = self.main_window.ax.plot(self.x_data,
    #                                                                                    result.best_fit + self.shirley,
    #                                                                                    'r--', label='Result')
    #             self.ui.fit_report_TE.setText(result.fit_report())
    #         elif self.ui.num_peaks_sb.value() == 4:
    #             vmodel = VoigtModel(prefix='p1_') + VoigtModel(prefix='p2_') + \
    #                      VoigtModel(prefix='p3_') + VoigtModel(prefix='p4_')
    #             params = Parameters()
    #             # add with tuples: (NAME VALUE VARY MIN  MAX  EXPR  BRUTE_STEP)
    #             params.add_many(('p1_amplitude', con[0][0], True, con[0][1], con[0][2]),
    #                             ('p1_center', con[0][3], True, con[0][4], con[0][5]),
    #                             ('p1_sigma', con[0][6], True, con[0][7], con[0][8]),
    #                             ('p2_amplitude', con[1][0], True, con[1][1], con[1][2]),
    #                             ('p2_center', con[1][3], True, con[1][4], con[1][5]),
    #                             ('p2_sigma', con[1][6], True, con[1][7], con[1][8]),
    #                             ('p3_amplitude', con[2][0], True, con[2][1], con[2][2]),
    #                             ('p3_center', con[2][3], True, con[2][4], con[2][5]),
    #                             ('p3_sigma', con[2][6], True, con[2][7], con[2][8]),
    #                             ('p4_amplitude', con[3][0], True, con[3][1], con[3][2]),
    #                             ('p4_center', con[3][3], True, con[3][4], con[3][5]),
    #                             ('p4_sigma', con[3][6], True, con[3][7], con[3][8]))
    #             result = vmodel.fit(self.y_data - self.shirley, params, x=self.x_data)
    #             comps = result.eval_components()
    #             ApplicationSettings.ALL_DATA_PLOTTED['Shirley'] = self.main_window.ax.plot(self.x_data, self.shirley, 'k--', label='Shirley')
    #             ApplicationSettings.ALL_DATA_PLOTTED['V1'] = self.main_window.ax.plot(self.x_data, self.shirley + comps['p1_'], 'k--', label='_V1')
    #             ApplicationSettings.ALL_DATA_PLOTTED['V2'] = self.main_window.ax.plot(self.x_data, self.shirley + comps['p2_'], 'k--', label='_V2')
    #             ApplicationSettings.ALL_DATA_PLOTTED['V3'] = self.main_window.ax.plot(self.x_data, self.shirley + comps['p3_'], 'k--', label='_V3')
    #             ApplicationSettings.ALL_DATA_PLOTTED['V4'] = self.main_window.ax.plot(self.x_data, self.shirley + comps['p4_'], 'k--', label='_V4')
    #             ApplicationSettings.ALL_DATA_PLOTTED['Fit'] = self.main_window.ax.plot(self.x_data, result.best_fit + self.shirley, 'r--', label='Result')
    #             leg = self.main_window.ax.legend(loc='best',fontsize='small')
    #             leg.set_draggable(True)
    #             self.ui.fit_report_TE.setText(result.fit_report())
    #         elif self.ui.num_peaks_sb.value() == 5:
    #             vmodel = VoigtModel(prefix='p1_') + VoigtModel(prefix='p2_') + \
    #                      VoigtModel(prefix='p3_') + VoigtModel(prefix='p4_') + VoigtModel(prefix='p5_')
    #             params = Parameters()
    #             # add with tuples: (NAME VALUE VARY MIN  MAX  EXPR  BRUTE_STEP)
    #             params.add_many(('p1_amplitude', con[0][0], True, con[0][1], con[0][2]),
    #                             ('p1_center', con[0][3], True, con[0][4], con[0][5]),
    #                             ('p1_sigma', con[0][6], True, con[0][7], con[0][8]),
    #                             ('p2_amplitude', con[1][0], True, con[1][1], con[1][2]),
    #                             ('p2_center', con[1][3], True, con[1][4], con[1][5]),
    #                             ('p2_sigma', con[1][6], True, con[1][7], con[1][8]),
    #                             ('p3_amplitude', con[2][0], True, con[2][1], con[2][2]),
    #                             ('p3_center', con[2][3], True, con[2][4], con[2][5]),
    #                             ('p3_sigma', con[2][6], True, con[2][7], con[2][8]),
    #                             ('p4_amplitude', con[3][0], True, con[3][1], con[3][2]),
    #                             ('p4_center', con[3][3], True, con[3][4], con[3][5]),
    #                             ('p4_sigma', con[3][6], True, con[3][7], con[3][8]),
    #                             ('p5_amplitude', con[4][0], True, con[4][1], con[4][2]),
    #                             ('p5_center', con[4][3], True, con[4][4], con[4][5]),
    #                             ('p5_sigma', con[4][6], True, con[4][7], con[4][8]))
    #             result = vmodel.fit(self.y_data - self.shirley, params, x=self.x_data)
    #             comps = result.eval_components()
    #             ApplicationSettings.ALL_DATA_PLOTTED['Shirley'] = self.main_window.ax.plot(self.x_data, self.shirley, 'k--', label='Shirley')
    #             ApplicationSettings.ALL_DATA_PLOTTED['V1'] =self.main_window.ax.plot(self.x_data, self.shirley + comps['p1_'], 'k--', label='_V1')
    #             ApplicationSettings.ALL_DATA_PLOTTED['V2'] =self.main_window.ax.plot(self.x_data, self.shirley + comps['p2_'], 'k--', label='_V2')
    #             ApplicationSettings.ALL_DATA_PLOTTED['V3'] =self.main_window.ax.plot(self.x_data, self.shirley + comps['p3_'], 'k--', label='_V3')
    #             ApplicationSettings.ALL_DATA_PLOTTED['V4'] =self.main_window.ax.plot(self.x_data, self.shirley + comps['p4_'], 'k--', label='_V4')
    #             ApplicationSettings.ALL_DATA_PLOTTED['V5'] = self.main_window.ax.plot(self.x_data,self.shirley + comps['p5_'],'k--', label='_V5')
    #             ApplicationSettings.ALL_DATA_PLOTTED['Fit'] =self.main_window.ax.plot(self.x_data, result.best_fit + self.shirley, 'r--', label='Result')
    #             self.ui.fit_report_TE.setText(result.fit_report())
    #     self.xps_basic()
    #     ApplicationSettings.ALL_DATA_PLOTTED['Y Data'] = self.main_window.ax.plot(self.x_data,self.y_data)
    #     self.main_window.canvas.draw()
    # def lorentz(self, x, amp, cen, sigma):
    #     return (amp/np.pi)*(1/2*sigma)/((x-cen)**2+(1/2*sigma)**2)
    #
    # def gaussian(self,x, amp, cen, sigma):
    #     return amp/(sigma*np.sqrt(2*np.pi))*np.exp(-(x-cen)**2/(2*sigma**2))
    #
    # def plot_init(self):
    #     self.main_window.cleargraph()
    #     if self.ui.fit_shape_cb.currentText()=='Lorentz':
    #         model = self.lorentz
    #     else:
    #         model = self.gaussian
    #     con = self.constraints
    #     if self.ui.num_peaks_sb.value() == 1:
    #         start_plot = model(self.x_data,con[0][0],con[0][3],con[0][6])
    #     elif self.ui.num_peaks_sb.value() == 2:
    #         start_plot = model(self.x_data, con[0][0], con[0][3], con[0][6])+\
    #                      model(self.x_data, con[1][0], con[1][3], con[1][6])
    #     elif self.ui.num_peaks_sb.value() == 3:
    #         start_plot = model(self.x_data, con[0][0], con[0][3], con[0][6])+\
    #                      model(self.x_data, con[1][0], con[1][3], con[1][6])+\
    #                      model(self.x_data, con[2][0], con[2][3], con[2][6])
    #     elif self.ui.num_peaks_sb.value() == 4:
    #         start_plot = model(self.x_data, con[0][0], con[0][3], con[0][6]) + \
    #                      model(self.x_data, con[1][0], con[1][3], con[1][6]) + \
    #                      model(self.x_data, con[2][0], con[2][3], con[2][6]) + \
    #                      model(self.x_data, con[3][0], con[3][3], con[3][6])
    #     elif self.ui.num_peaks_sb.value() == 5:
    #         start_plot = model(self.x_data, con[0][0], con[0][3], con[0][6]) + \
    #                      model(self.x_data, con[1][0], con[1][3], con[1][6]) + \
    #                      model(self.x_data, con[2][0], con[2][3], con[2][6]) + \
    #                      model(self.x_data, con[3][0], con[3][3], con[3][6]) + \
    #                      model(self.x_data, con[4][0], con[4][3], con[4][6])
    #     ApplicationSettings.ALL_DATA_PLOTTED['Y_Data'] = self.main_window.ax.plot(self.x_data,self.y_data)
    #     ApplicationSettings.ALL_DATA_PLOTTED['Shirley'] = \
    #         self.main_window.ax.plot(self.x_data,self.shirley,'.k', markersize=4)
    #     ApplicationSettings.ALL_DATA_PLOTTED['XPS Init Values'] = \
    #         self.main_window.ax.plot(self.x_data,start_plot + self.shirley, '-y')
    #     self.xps_basic()
    #     self.main_window.canvas.draw()
    # def save_constraints(self):
    #     try:
    #         for row in range(9):
    #             for column in range(5):
    #                 self.constraints[column][row] = float(self.ui.tableWidget.item(row, column).text())
    #     except ValueError:
    #         print('No constraint save')

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

    def fit_range_changed(self):
        try:
            temp = self.fit_obj[self.ui.fit_range_cb.currentText()].peak_constraints
            constraints = [[self.ui.amp1_sb,self.ui.amp1l_sb,self.ui.amp1h_sb],
                    [self.ui.cen1_sb,self.ui.cen1l_sb,self.ui.cen1h_sb],
                    [self.ui.sigma1_sb,self.ui.sigma1l_sb,self.ui.sigma1h_sb]],\
                          [[self.ui.amp2_sb, self.ui.amp2l_sb, self.ui.amp2h_sb],
                  [self.ui.cen2_sb, self.ui.cen2l_sb, self.ui.cen2h_sb],
                  [self.ui.sigma2_sb, self.ui.sigma2l_sb, self.ui.sigma2h_sb]],\
                          [[self.ui.amp3_sb, self.ui.amp3l_sb, self.ui.amp3h_sb],
                  [self.ui.cen3_sb, self.ui.cen3l_sb, self.ui.cen3h_sb],
                  [self.ui.sigma3_sb, self.ui.sigma3l_sb, self.ui.sigma3h_sb]],\
                          [[self.ui.amp4_sb, self.ui.amp4l_sb, self.ui.amp4h_sb],
                  [self.ui.cen4_sb, self.ui.cen4l_sb, self.ui.cen4h_sb],
                  [self.ui.sigma4_sb, self.ui.sigma4l_sb, self.ui.sigma4h_sb]],\
                          [[self.ui.amp5_sb, self.ui.amp5l_sb, self.ui.amp5h_sb],
                  [self.ui.cen5_sb, self.ui.cen5l_sb, self.ui.cen5h_sb],
                  [self.ui.sigma5_sb, self.ui.sigma5l_sb, self.ui.sigma5h_sb]]
            for i in range(5):
                for j in range(3):
                    for k in range(3):
                        constraints[i][j][k].setValue(temp[i][j][k])
            self.ui.fitreport_te.setText(self.fit_obj[self.ui.fit_range_cb.currentText()].fit_result)
        except KeyError:
            pass

    def plot(self):
        x = self.ui.tw_x.currentIndex().data()
        self.x_data = self.data[x].to_numpy()
        self.x_data = self.x_data[~np.isnan(self.x_data)]
        y = self.ui.tw_y.currentIndex().data()
        self.y_data = self.data[y].to_numpy()
        self.y_data = self.y_data[~np.isnan(self.y_data)]
        # self.x_data = self.x_data+float(self.ui.offset_LE.text())
        self.x_data = self.correct_to(self.x_data,self.y_data, self.ui.correctc1s_dsb.value())
        ApplicationSettings.ALL_DATA_PLOTTED[str(x)] = \
            self.main_window.ax.plot(self.x_data, self.y_data, label=x)
        self.xps_basic()

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

    def shirley_calculate(self,x, y, tol=1e-5, maxit=15):
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

    def fit_fun_2(self):
        try:
            line0 = ApplicationSettings.ALL_DATA_PLOTTED[self.ui.fit_range_cb.currentText()+'_fit']
            self.main_window.ax.lines.remove(line0[0])
        except KeyError:
            pass
        for i in range(5):
            try:
                line0=ApplicationSettings.ALL_DATA_PLOTTED['V%s' % str(i)]
                poly = ApplicationSettings.ALL_DATA_PLOTTED['V%s_err' % str(i)]
                self.main_window.ax.lines.remove(line0[0])
                poly[0].remove(self)
            except KeyError:
                pass
            except ValueError:
                pass
        checked = [self.ui.peak1_box.isChecked(), self.ui.peak2_box.isChecked(), self.ui.peak3_box.isChecked(),
                   self.ui.peak4_box.isChecked(), self.ui.peak5_box.isChecked()]
        nums_checked = []
        for i in range(len(checked)):
            if checked[i]:
                nums_checked.append(i)
        constraints = [[self.ui.amp1_sb, self.ui.amp1l_sb, self.ui.amp1h_sb],
                       [self.ui.cen1_sb, self.ui.cen1l_sb, self.ui.cen1h_sb],
                       [self.ui.sigma1_sb, self.ui.sigma1l_sb, self.ui.sigma1h_sb]], [[self.ui.amp2_sb, self.ui.amp2l_sb, self.ui.amp2h_sb],
                       [self.ui.cen2_sb, self.ui.cen2l_sb, self.ui.cen2h_sb],
                       [self.ui.sigma2_sb, self.ui.sigma2l_sb, self.ui.sigma2h_sb]], [[self.ui.amp3_sb, self.ui.amp3l_sb, self.ui.amp3h_sb],
                       [self.ui.cen3_sb, self.ui.cen3l_sb, self.ui.cen3h_sb],
                       [self.ui.sigma3_sb, self.ui.sigma3l_sb, self.ui.sigma3h_sb]], [[self.ui.amp4_sb, self.ui.amp4l_sb, self.ui.amp4h_sb],
                       [self.ui.cen4_sb, self.ui.cen4l_sb, self.ui.cen4h_sb],
                       [self.ui.sigma4_sb, self.ui.sigma4l_sb, self.ui.sigma4h_sb]], [[self.ui.amp5_sb, self.ui.amp5l_sb, self.ui.amp5h_sb],
                       [self.ui.cen5_sb, self.ui.cen5l_sb, self.ui.cen5h_sb],
                       [self.ui.sigma5_sb, self.ui.sigma5l_sb, self.ui.sigma5h_sb]]
        cons = [[self.ui.amp1_sb.value(), self.ui.amp1l_sb.value(), self.ui.amp1h_sb.value()],
                       [self.ui.cen1_sb.value(), self.ui.cen1l_sb.value(), self.ui.cen1h_sb.value()],
                       [self.ui.sigma1_sb.value(), self.ui.sigma1l_sb.value(), self.ui.sigma1h_sb.value()]], [[self.ui.amp2_sb.value(), self.ui.amp2l_sb.value(), self.ui.amp2h_sb.value()],
                       [self.ui.cen2_sb.value(), self.ui.cen2l_sb.value(), self.ui.cen2h_sb.value()],
                       [self.ui.sigma2_sb.value(), self.ui.sigma2l_sb.value(), self.ui.sigma2h_sb.value()]], [[self.ui.amp3_sb.value(), self.ui.amp3l_sb.value(), self.ui.amp3h_sb.value()],
                       [self.ui.cen3_sb.value(), self.ui.cen3l_sb.value(), self.ui.cen3h_sb.value()],
                       [self.ui.sigma3_sb.value(), self.ui.sigma3l_sb.value(), self.ui.sigma3h_sb.value()]], [[self.ui.amp4_sb.value(), self.ui.amp4l_sb.value(), self.ui.amp4h_sb.value()],
                       [self.ui.cen4_sb.value(), self.ui.cen4l_sb.value(), self.ui.cen4h_sb.value()],
                       [self.ui.sigma4_sb.value(), self.ui.sigma4l_sb.value(), self.ui.sigma4h_sb.value()]], [[self.ui.amp5_sb.value(), self.ui.amp5l_sb.value(), self.ui.amp5h_sb.value()],
                       [self.ui.cen5_sb.value(), self.ui.cen5l_sb.value(), self.ui.cen5h_sb.value()],
                       [self.ui.sigma5_sb.value(), self.ui.sigma5l_sb.value(), self.ui.sigma5h_sb.value()]]
        obj = self.fit_obj[self.ui.fit_range_cb.currentText()]
        shirl = obj.shirley
        result = obj.fit(checked, cons)
        ApplicationSettings.ALL_DATA_PLOTTED[self.ui.fit_range_cb.currentText()+'_fit'] = \
            self.main_window.ax.plot(obj.x_data, result.best_fit+shirl[1], 'k--', label=self.ui.fit_range_cb.currentText()+'_fit')
        self.ui.fitreport_te.setText(result.fit_report())
        comps = result.eval_components()
        dely = result.eval_uncertainty(sigma=3)
        for i in nums_checked:
            constraints[i][0][0].setValue(result.params['p%s_amplitude' % str(i)].value)
            constraints[i][1][0].setValue(result.params['p%s_center' % str(i)].value)
            constraints[i][2][0].setValue(result.params['p%s_sigma' % str(i)].value)
            obj.peak_constraints[i][0][0] = result.params['p%s_amplitude' % str(i)].value
            obj.peak_constraints[i][0][0] = result.params['p%s_center' % str(i)].value
            obj.peak_constraints[i][0][0] = result.params['p%s_sigma' % str(i)].value
            if not self.ui.plot_what_box.isChecked():
                ApplicationSettings.ALL_DATA_PLOTTED['V%s' % str(i)] = \
                    self.main_window.ax.plot(obj.x_data,  obj.shirley[1]+ comps['p%s_' % str(i)], 'k--', label='_V1')
        ApplicationSettings.ALL_DATA_PLOTTED['V%s_err' % str(i)] = \
            self.main_window.ax.fill_between(obj.x_data, result.best_fit - dely+obj.shirley[1], result.best_fit + dely+obj.shirley[1], color="#ABABAB",label='3-$\sigma$ uncertainty band')
        self.main_window.canvas.draw()

    def select_xps_range(self,enabled):
        if enabled:
            self.span = SpanSelector(self.main_window.ax, self.on_select, 'horizontal', useblit=False,
                                     rectprops=dict(alpha=0.2, facecolor='blue'))
        else:
            del self.span

    def on_select(self,minimum, maximum):
        # lims = [find_nearest(self.x_data,minimum),find_nearest(self.x_data,maximum)]
        # temp_x = self.x_data[lims[1]:lims[0]]
        # temp_y = self.y_data[lims[1]:lims[0]]
        # shirley = self.shirley_calculate(temp_x,temp_y)
        self.fit_obj[str(np.round(minimum,1))+'+'+str(np.round(maximum,1))] =  Fit_Object(self.x_data,self.y_data,minimum,maximum)
        ApplicationSettings.ALL_DATA_PLOTTED[str(np.round(minimum,1))+'+'+str(np.round(maximum,1))] = \
            self.main_window.ax.plot(self.fit_obj[str(np.round(minimum,1))+'+'+str(np.round(maximum,1))].shirley[0],
                                     self.fit_obj[str(np.round(minimum,1))+'+'+str(np.round(maximum,1))].shirley[1])
        self.ui.fit_range_cb.clear()
        self.ui.fit_range_cb.addItems([i for i in self.fit_obj.keys()])
        self.ui.xpsrange_rb.setChecked(False)
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
        centers = np.linspace(minimum,maximum, 5)
        for i in range(5):
            self.peak_constraints.append([[5000, 0, 999999], [centers[i], minimum, maximum],[1,.0001,10]])

    def lorentz(self, x, amp, cen, sigma):
        return (amp/np.pi)*(1/2*sigma)/((x-cen)**2+(1/2*sigma)**2)

    def gaussian(self,x, amp, cen, sigma):
        return amp/(sigma*np.sqrt(2*np.pi))*np.exp(-(x-cen)**2/(2*sigma**2))

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

    def fit(self, checked, cons):
        fit_params = []
        self.update_constraints(cons)
        line_shape_mods = [PseudoVoigtModel(prefix='p0_'), PseudoVoigtModel(prefix='p1_'), PseudoVoigtModel(prefix='p2_'),
                           PseudoVoigtModel(prefix='p3_'), PseudoVoigtModel(prefix='p4_')]
        cur_mods = []
        checked_peaks = []
        params = Parameters()
        # add with tuples: (NAME VALUE VARY MIN  MAX  EXPR  BRUTE_STEP)
        for x in range(5):
            if checked[x]:
                params.add_many(('p%s_amplitude' % str(x), self.peak_constraints[x][0][0], True, self.peak_constraints[x][0][1], self.peak_constraints[x][0][2]),
                                ('p%s_center' % str(x), self.peak_constraints[x][1][0], True, self.peak_constraints[x][1][1], self.peak_constraints[x][1][2]),
                                ('p%s_sigma' % str(x), self.peak_constraints[x][2][0], True, self.peak_constraints[x][2][1], self.peak_constraints[x][2][2]),
                                ('p%s_fraction' % str(x), .7, False))
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
