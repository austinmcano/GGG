from src.Ui_Files.main_window import Ui_MainWindow
from src.gui_elements.DockWidgets.data_browser import DataBrowser
from src.gui_elements.DockWidgets.project_browser import ProjectBrowser
from src.gui_elements.DockWidgets.XPS_view import XPS_view
from src.gui_elements.DockWidgets.QCM_view import QCM_view
from src.gui_elements.DockWidgets.FTIR_view import FTIR_view
from src.gui_elements.DockWidgets.SE_view import SE_view
from src.gui_elements.DockWidgets.CF_view import CurveFit_view
from src.gui_elements.DockWidgets.XRD_view import XRD_view
from src.gui_elements.DockWidgets.Calc_view import Calculator_view
from src.Ui_Files.Dialogs.start_dialog import Ui_Dialog as start_Ui
from src.gui_elements.DockWidgets.Console_view import Console_view
from src.Ui_Files.Dialogs.seaborn_settings import Ui_Dialog as Ui_sns_Dialog
import gc
from src.gui_elements.plotting_functions import *
from src.gui_elements.general_functions import *

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.settings = QtCore.QSettings('Resources/settings.ini', QtCore.QSettings.IniFormat)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self._init_UI()
        self.init_connections()

    def _init_UI(self):
        self.style = self.settings.value('sns_style')
        self.context = self.settings.value('sns_context')
        self.fs = int(self.settings.value('sns_fontscale'))
        self.c_palette = self.settings.value('sns_c_palette')
        self.font = self.settings.value('sns_font')
        self.axes_facecolor = self.settings.value('sns_axesfacecolor')
        self.fig_facecolor = self.settings.value('sns_figfacecolor')

        # sns.set(self.context, self.style, self.c_palette, self.font, self.fs, True, {"axes.facecolor": "#F0F0F0", 'figure.facecolor': '#505F69'})
        sns.set(self.context, self.style, self.c_palette, self.font,
                self.fs,True, {"axes.facecolor": self.axes_facecolor,'figure.facecolor': self.fig_facecolor})

        self.fig = figure(num=None, figsize=(8, 6), dpi=80)
        self.canvas = FigureCanvas(self.fig)
        self.ax_1 = self.fig.add_subplot(111)
        self.ax_2 = None
        self.ax_3 = None
        self.ax_4 = None
        self.canvas.draw()
        self.toolbar = NavigationToolbar(self.canvas, self.canvas, coordinates=True)
        self.ui.verticalLayout.addWidget(self.toolbar)
        self.ui.verticalLayout.addWidget(self.canvas)
        self.canvas.draw()
        self.bar = {'xlist': '', 'y1list':'','y2list':'','y3list':'', 'width':'0.35', 'num':1,
                    'label1':'','label2':'','label3':''}
        self.ax = self.ax_1
        self.dragh = DragHandler(self, figure=self.fig)

        self.dw_ProjectView = ProjectBrowser(self)
        self.dw_Data_Broswer = DataBrowser(self)
        self.dw_FTIR = FTIR_view(self)
        self.dw_XPS = XPS_view(self)
        self.dw_XRD = XRD_view(self)
        self.dw_QCM = QCM_view(self)
        self.dw_SE = SE_view(self)
        self.dw_Console = Console_view(self)
        self.dw_CF = CurveFit_view(self)
        self.dw_calc = Calculator_view(self)
        self.All_Views = [self.dw_FTIR, self.dw_QCM, self.dw_SE, self.dw_XPS, self.dw_CF, self.dw_ProjectView
            , self.dw_Data_Broswer, self.dw_XRD]

        # self.resize(self.settings.value("size", QtCore.QSize(270, 225)))
        # self.resize(self.settings.value("size"))
        # self.move(self.settings.value("pos", QtCore.QPoint(50, 50)))

        self.ax.spines['bottom'].set_color(self.settings.value('bottom_spine_color'))
        self.ax.spines['top'].set_color(self.settings.value('top_spine_color'))
        self.ax.spines['right'].set_color(self.settings.value('right_spine_color'))
        self.ax.spines['left'].set_color(self.settings.value('left_spine_color'))
        self.ax.xaxis.label.set_color(self.settings.value('bottom_spine_color'))
        self.ax.yaxis.label.set_color(self.settings.value('left_spine_color'))
        self.ax.tick_params(axis='x', colors=self.settings.value('bottom_spine_color'))
        self.ax.tick_params(axis='y', colors=self.settings.value('left_spine_color'))

        self.color_list = []
        for name in matplotlib.colors.cnames.items():
            self.color_list.append(name[0])

        self.anno_text = ''
        self.anno_size = 20
        self.anno_alpha = 1.0
        self.anno_color = 'black'
        self.anno_bgcolor = 'white'
        self.anno_fecolor = 'white'
        self.anno_frame = 'none'
        self.anno_frame_width = 2.0
        self.anno_rotation = 0.0
        self.anno_style = 'normal'

        self.legend_size = 'medium'

    def init_connections(self):
        self.plot_context_actions()
        # self.context_menu_plot = QtWidgets.QMenu(self)
        # self.canvas.installEventFilter(self)
        #
        # self.clear_menu = self.context_menu_plot.addMenu('Clear')
        # self.clear_action = self.clear_menu.addAction('Clear All')
        # self.clear_single_action = self.clear_menu.addAction('Clear Graph')
        # self.clear_all_graphs_action = self.clear_menu.addAction('Clear All Graphs')
        # self.save_menu = self.context_menu_plot.addMenu('Save')
        # self.actionSave_To_CSV = self.save_menu.addAction('Save To CSV')
        # self.graph_menu = self.context_menu_plot.addMenu(' Graphs')
        # self.removeplot_action = self.graph_menu.addAction('Remove Line')
        # self.save_figure_action = self.save_menu.addAction('Save Figure')
        # self.annotation_action = self.context_menu_plot.addAction('Annotate')
        # self.sns_settings_action = self.graph_menu.addAction('Seaborn Settings')
        # self.send_to_cf_action = self.context_menu_plot.addAction('Send to CF')
        # self.open_fig_action = self.context_menu_plot.addAction('Open Fig')
        # self.axis_colors_action = self.graph_menu.addAction('Axis Colors')
        # self.axis_setup_action = self.graph_menu.addAction('Change Axis Setup')
        # self.axis_setup_action2 = self.graph_menu.addAction('Change Axis Setup 2')
        # self.axis_setup_action3 = self.graph_menu.addAction('Change Axis Setup 3')
        # self.axis_setup_action4 = self.graph_menu.addAction('Change Axis Setup 4')
        #
        # self.clear_single_action.triggered.connect(lambda: self.clear_single_graph())
        # self.clear_all_graphs_action.triggered.connect(lambda: self.clear_all_graphs())
        # self.clear_action.triggered.connect(lambda: self.cleargraph())
        # self.removeplot_action.triggered.connect(lambda: remove_line(self))
        # self.actionSave_To_CSV.triggered.connect(lambda: Save_All_Plotted(self))
        # self.save_figure_action.triggered.connect(lambda: save_fig(self))
        # self.annotation_action.triggered.connect(lambda: plot_annotation(self))
        # self.sns_settings_action.triggered.connect(lambda: self.sns_settings())
        # self.send_to_cf_action.triggered.connect(lambda: send_to_cf(self))
        # self.open_fig_action.triggered.connect(lambda: show_pickled_fig(self))
        # self.axis_colors_action.triggered.connect(lambda: spine_color_fun(self))
        # # self.axis_setup_action.triggered.connect(lambda: axis_setup_function(self))
        # self.ui.actionAxis1.triggered.connect(lambda: change_axis(self, 'axis1'))
        # self.ui.actionAxis2.triggered.connect(lambda: change_axis(self, 'axis2'))
        # self.ui.actionAxis3.triggered.connect(lambda: change_axis(self, 'axis3'))
        # self.ui.actionAxis4.triggered.connect(lambda: change_axis(self, 'axis4'))
        #
        # self.axis_setup_action = QtWidgets.QShortcut(QtGui.QKeySequence('Ctrl+1'), self)
        # self.axis_setup_action.activated.connect(lambda: axis_setup_fun(self,1))
        # self.axis_setup_action2 = QtWidgets.QShortcut(QtGui.QKeySequence('Ctrl+2'), self)
        # self.axis_setup_action2.activated.connect(lambda: axis_setup_fun(self, 2))
        # self.axis_setup_action3 = QtWidgets.QShortcut(QtGui.QKeySequence('Ctrl+3'), self)
        # self.axis_setup_action3.activated.connect(lambda: axis_setup_fun(self, 3))
        # self.axis_setup_action4 = QtWidgets.QShortcut(QtGui.QKeySequence('Ctrl+4'), self)
        # self.axis_setup_action4.activated.connect(lambda: axis_setup_fun(self, 4))
        start_dialog = QtWidgets.QDialog()
        start_ui = start_Ui()
        start_ui.setupUi(start_dialog)
        pbs = [start_ui.FTIR_pb, start_ui.QCM_pb,start_ui.SE_pb,start_ui.XPS_pb,start_ui.XRD_pb,start_ui.CF_pb]
        [i.clicked.connect(lambda: start_dialog.accept())for i in pbs]
        start_ui.FTIR_pb.clicked.connect(lambda: self.start(self.dw_FTIR))
        start_ui.QCM_pb.clicked.connect(lambda: self.start(self.dw_QCM))
        start_ui.SE_pb.clicked.connect(lambda: self.start(self.dw_SE))
        start_ui.XPS_pb.clicked.connect(lambda: self.start(self.dw_XPS))
        start_ui.XRD_pb.clicked.connect(lambda: self.start(self.dw_XRD))
        start_ui.CF_pb.clicked.connect(lambda: self.start(self.dw_CF))
        start_dialog.exec_()

        self.ui.actionAdd_Line.triggered.connect(lambda: add_line_to_graph(self))
        self.ui.actionGraph_Test.triggered.connect(lambda: graph_test_fun(self))
        self.ui.actionFile.triggered.connect(lambda: import_file(self))
        self.ui.actionLoad_Data.triggered.connect(lambda: load_data(self))
        self.ui.actionNew_Project_2.triggered.connect(lambda: new_project(self))
        self.ui.actionOpen_Project.triggered.connect(lambda: open_project(self))
        self.ui.actionChange_Settings.triggered.connect(lambda: app_settings_fun(self))
        self.ui.actionSeaborn_Settings.triggered.connect(lambda: self.sns_settings())
        self.ui.actionLegend_Toggle.triggered.connect(lambda: toggle_legend(self))
        self.ui.actionSave_Data.triggered.connect(lambda: Save_All_Plotted(self))
        self.ui.actionClear_Graph.triggered.connect(lambda: self.cleargraph())
        self.ui.actionXPS.triggered.connect(lambda: XPS_view_fun(self))
        self.ui.actionXRD.triggered.connect(lambda: XRD_view_fun(self))
        # self.ui.actionDataBrowser.triggered.connect(lambda: DataBrowser_view_fun(self))
        # self.ui.actionProject_Tree.triggered.connect(lambda: Project_view_fun(self))
        self.ui.actionQCM.triggered.connect(lambda: QCM_view_fun(self))
        self.ui.actionFTIR.triggered.connect(lambda: FTIR_view_fun(self))
        self.ui.actionSE.triggered.connect(lambda: SE_view_fun(self))
        self.ui.actionCalculator.triggered.connect(lambda: Calc_view_fun(self))
        self.ui.actionConsole.triggered.connect(lambda: Console_view_fun(self))
        self.ui.actionCurve_Fitting.triggered.connect(lambda: CF_view_fun(self))
        self.ui.actionDirectory.triggered.connect(lambda: import_directiory_function(self))
        self.ui.actionBar_Graph.triggered.connect(lambda: bar_graph(self))
        self.ui.actionTight_Layout.triggered.connect(lambda: tight_figure(self))
        self.ui.actionQCM_Help.triggered.connect(lambda: random_c_plot(self))
        self.ui.actionSE_Help.triggered.connect(lambda: self.se_help_function())
        self.ui.actionXPS_Help.triggered.connect(lambda: self.memory_usage())
        self.ax.callbacks.connect('xlim_changed', self.lims_change)
        self.ui.actionLegend_Toggle.setShortcut(QtCore.QCoreApplication.translate("MainWindow", u"Ctrl+L", None))
        self.ui.actionClear_Graph.setShortcut(QtCore.QCoreApplication.translate("MainWindow", u"Ctrl+W", None))

    def plot_context_actions(self):
        self.context_menu_plot = QtWidgets.QMenu(self)
        self.canvas.installEventFilter(self)

        self.clear_menu = self.context_menu_plot.addMenu('Clear')
        self.clear_action = self.clear_menu.addAction('Clear All')
        self.clear_single_action = self.clear_menu.addAction('Clear Graph')
        self.clear_all_graphs_action = self.clear_menu.addAction('Clear All Graphs')
        self.save_menu = self.context_menu_plot.addMenu('Save')
        self.actionSave_To_CSV = self.save_menu.addAction('Save To CSV')
        self.graph_menu = self.context_menu_plot.addMenu(' Graphs')
        self.removeplot_action = self.graph_menu.addAction('Remove Line')
        self.save_figure_action = self.save_menu.addAction('Save Figure')
        self.annotation_action = self.context_menu_plot.addAction('Annotate')
        self.sns_settings_action = self.graph_menu.addAction('Seaborn Settings')
        self.send_to_cf_action = self.context_menu_plot.addAction('Send to CF')
        self.open_fig_action = self.context_menu_plot.addAction('Open Fig')
        self.axis_colors_action = self.graph_menu.addAction('Axis Colors')
        # self.axis_setup_action = self.graph_menu.addAction('Change Axis Setup')
        # self.axis_setup_action2 = self.graph_menu.addAction('Change Axis Setup 2')
        # self.axis_setup_action3 = self.graph_menu.addAction('Change Axis Setup 3')
        # self.axis_setup_action4 = self.graph_menu.addAction('Change Axis Setup 4')

        self.clear_single_action.triggered.connect(lambda: self.clear_single_graph())
        self.clear_all_graphs_action.triggered.connect(lambda: self.clear_all_graphs())
        self.clear_action.triggered.connect(lambda: self.cleargraph())
        self.removeplot_action.triggered.connect(lambda: remove_line(self))
        self.actionSave_To_CSV.triggered.connect(lambda: Save_All_Plotted(self))
        self.save_figure_action.triggered.connect(lambda: save_fig(self))
        self.annotation_action.triggered.connect(lambda: plot_annotation(self))
        self.sns_settings_action.triggered.connect(lambda: self.sns_settings())
        self.send_to_cf_action.triggered.connect(lambda: send_to_cf(self))
        self.open_fig_action.triggered.connect(lambda: show_pickled_fig(self))
        self.axis_colors_action.triggered.connect(lambda: spine_color_fun(self))
        # self.axis_setup_action.triggered.connect(lambda: axis_setup_function(self))
        self.ui.actionAxis1.triggered.connect(lambda: change_axis(self, 'axis1'))
        self.ui.actionAxis2.triggered.connect(lambda: change_axis(self, 'axis2'))
        self.ui.actionAxis3.triggered.connect(lambda: change_axis(self, 'axis3'))
        self.ui.actionAxis4.triggered.connect(lambda: change_axis(self, 'axis4'))

        self.axis_setup_action = QtWidgets.QShortcut(QtGui.QKeySequence('Ctrl+1'), self)
        self.axis_setup_action.activated.connect(lambda: axis_setup_fun(self, 1))
        self.axis_setup_action2 = QtWidgets.QShortcut(QtGui.QKeySequence('Ctrl+2'), self)
        self.axis_setup_action2.activated.connect(lambda: axis_setup_fun(self, 2))
        self.axis_setup_action3 = QtWidgets.QShortcut(QtGui.QKeySequence('Ctrl+3'), self)
        self.axis_setup_action3.activated.connect(lambda: axis_setup_fun(self, 3))
        self.axis_setup_action4 = QtWidgets.QShortcut(QtGui.QKeySequence('Ctrl+4'), self)
        self.axis_setup_action4.activated.connect(lambda: axis_setup_fun(self, 4))

    def memory_usage(self):
        # !/usr/bin/env python
        import psutil
        # gives a single float value
        print(psutil.cpu_percent())
        # gives an object with many fields
        print(psutil.virtual_memory())
        num = gc.collect()
        print('gc_collect')
        print(num)
        # you can convert that object to a dictionary
        # dict(psutil.virtual_memory()._asdict())

    def start(self, dock_widget):
        self.addDockWidget(QtCore.Qt.RightDockWidgetArea, dock_widget)


    def lims_change(self, event_ax):
        ApplicationSettings.C_X_LIM = list(event_ax.get_xlim())

    def eventFilter(self, object, event):
        # For right click events
        if event.type() == QtCore.QEvent.ContextMenu:
            self.context_menu_plot.exec_(self.mapToGlobal(QtCore.QPoint(event.pos())))
        return False

    def sns_settings(self):
        def sns_set_fun():
            self.style = ui.style_cb.currentText()
            self.context = ui.context_cb.currentText()
            self.fs = int(ui.fontscale_sb.value())
            self.c_palette = ui.palette_cb.currentText()
            self.font=ui.fonts_cb.currentText()
            self.fig_facecolor = ui.fig_facecolor_le.text()
            self.axes_facecolor = ui.axes_facecolor_le.text()
            sns.set(self.context, self.style, self.c_palette, self.font, self.fs, True,
                    {"axes.facecolor": self.axes_facecolor, 'figure.facecolor': self.fig_facecolor})
            self.ax_2 = 1
            self.cleargraph()
            self.fig.delaxes(self.ax)
            self.ax = self.fig.add_subplot(111)
            self.ax.spines['bottom'].set_color(self.settings.value('bottom_spine_color'))
            self.ax.spines['top'].set_color(self.settings.value('top_spine_color'))
            self.ax.spines['right'].set_color(self.settings.value('right_spine_color'))
            self.ax.spines['left'].set_color(self.settings.value('left_spine_color'))
            self.ax.xaxis.label.set_color(self.settings.value('bottom_spine_color'))
            self.ax.yaxis.label.set_color(self.settings.value('left_spine_color'))
            self.ax.tick_params(axis='x', colors=self.settings.value('bottom_spine_color'))
            self.ax.tick_params(axis='y', colors=self.settings.value('left_spine_color'))
            self.canvas.draw()

        d = QtWidgets.QDialog()
        ui = Ui_sns_Dialog()
        ui.setupUi(d)
        palette_options = ['Accent', 'Accent_r', 'Blues', 'Blues_r', 'BrBG', 'BrBG_r', 'BuGn', 'BuGn_r', 'BuPu',
                           'BuPu_r', 'CMRmap', 'CMRmap_r', 'Dark2', 'Dark2_r', 'GnBu', 'GnBu_r', 'Greens', 'Greens_r',
                           'Greys', 'Greys_r', 'OrRd', 'OrRd_r', 'Oranges', 'Oranges_r', 'PRGn', 'PRGn_r', 'Paired',
                           'Paired_r', 'Pastel1', 'Pastel1_r', 'Pastel2', 'Pastel2_r', 'PiYG', 'PiYG_r', 'PuBu',
                           'PuBuGn', 'PuBuGn_r', 'PuBu_r', 'PuOr', 'PuOr_r', 'PuRd', 'PuRd_r', 'Purples', 'Purples_r',
                           'RdBu', 'RdBu_r', 'RdGy', 'RdGy_r', 'RdPu', 'RdPu_r', 'RdYlBu', 'RdYlBu_r', 'RdYlGn',
                           'RdYlGn_r', 'Reds', 'Reds_r', 'Set1', 'Set1_r', 'Set2', 'Set2_r', 'Set3', 'Set3_r',
                           'Spectral', 'Spectral_r', 'Wistia', 'Wistia_r', 'YlGn', 'YlGnBu', 'YlGnBu_r', 'YlGn_r',
                           'YlOrBr', 'YlOrBr_r', 'YlOrRd', 'YlOrRd_r', 'afmhot', 'afmhot_r', 'autumn', 'autumn_r',
                           'binary', 'binary_r', 'bone', 'bone_r', 'brg', 'brg_r', 'bwr', 'bwr_r', 'cividis',
                           'cividis_r', 'cool', 'cool_r', 'coolwarm', 'coolwarm_r', 'copper', 'copper_r', 'cubehelix',
                           'cubehelix_r', 'flag', 'flag_r', 'gist_earth', 'gist_earth_r', 'gist_gray', 'gist_gray_r',
                           'gist_heat', 'gist_heat_r', 'gist_ncar', 'gist_ncar_r', 'gist_rainbow', 'gist_rainbow_r',
                           'gist_stern', 'gist_stern_r', 'gist_yarg', 'gist_yarg_r', 'gnuplot', 'gnuplot2','gnuplot2_r',
                           'gnuplot_r', 'gray', 'gray_r', 'hot', 'hot_r', 'hsv', 'hsv_r', 'icefire', 'icefire_r',
                           'inferno', 'inferno_r', 'jet', 'jet_r', 'magma', 'magma_r', 'mako', 'mako_r','nipy_spectral',
                           'nipy_spectral_r', 'ocean', 'ocean_r', 'pink', 'pink_r', 'plasma', 'plasma_r', 'prism',
                           'prism_r', 'rainbow', 'rainbow_r', 'rocket', 'rocket_r', 'seismic', 'seismic_r', 'spring',
                           'spring_r', 'summer', 'summer_r', 'tab10', 'tab10_r', 'tab20', 'tab20_r', 'tab20b',
                           'tab20b_r', 'tab20c', 'tab20c_r', 'terrain', 'terrain_r', 'twilight', 'twilight_r',
                           'twilight_shifted', 'twilight_shifted_r', 'viridis', 'viridis_r', 'vlag', 'vlag_r',
                           'winter', 'winter_r']
        font_options = ['Al Nile', 'Al Tarikh', 'AlBayan', 'AmericanTypewriter', 'Andale Mono', 'Apple Braille',
                        'Apple Braille Outline 6 Dot', 'Apple Braille Outline 8 Dot', 'Apple Braille Pinpoint 6 Dot',
                        'Apple Braille Pinpoint 8 Dot', 'Apple Chancery', 'Apple Color Emoji', 'Apple Symbols',
                        'AppleGothic', 'AppleMyungjo', 'AppleSDGothicNeo', 'AquaKana', 'ArabicUIDisplay',
                        'ArabicUIText', 'Arial', 'Arial Black', 'Arial Bold', 'Arial Bold Italic', 'Arial Italic',
                        'Arial Narrow', 'Arial Narrow Bold', 'Arial Narrow Bold Italic', 'Arial Narrow Italic',
                        'Arial Rounded Bold', 'Arial Unicode', 'ArialHB', 'Artifakt Element Bold',
                        'Artifakt Element Bold Italic', 'Artifakt Element Italic', 'Artifakt Element Regular',
                        'Athelas', 'Avenir', 'Avenir Next', 'Avenir Next Condensed', 'Ayuthaya', 'Baghdad', 'Bangla MN',
                        'Bangla Sangam MN', 'Baskerville', 'Beirut', 'BigCaslon', 'Bodoni 72', 'Bodoni 72 OS',
                        'Bodoni 72 Smallcaps Book', 'Bodoni Ornaments', 'Bradley Hand Bold', 'Brush Script',
                        'Chalkboard', 'ChalkboardSE', 'Chalkduster', 'Charter', 'Cochin', 'Comic Sans MS',
                        'Comic Sans MS Bold', 'Copperplate', 'Corsiva', 'Courier New', 'Courier New Bold',
                        'Courier New Bold Italic', 'Courier New Italic', 'DIN Alternate Bold', 'DIN Condensed Bold',
                        'Damascus', 'DecoTypeNaskh', 'Devanagari Sangam MN', 'DevanagariMT', 'Didot', 'Diwan Kufi',
                        'Diwan Thuluth', 'EuphemiaCAS', 'Farah', 'Farisi', 'Futura', 'GeezaPro', 'Georgia',
                        'Georgia Bold', 'Georgia Bold Italic', 'Georgia Italic', 'GillSans', 'Gujarati Sangam MN',
                        'GujaratiMT', 'Gurmukhi', 'Gurmukhi MN', 'Gurmukhi Sangam MN', 'Helvetica', 'HelveticaNeue',
                        'HelveticaNeueDeskInterface', 'Herculanum', 'Hiragino Sans GB', 'Hoefler Text',
                        'Hoefler Text Ornaments', 'ITFDevanagari', 'Impact', 'InaiMathi-MN', 'Iowan Old Style',
                        'Kailasa', 'Kannada MN', 'Kannada Sangam MN', 'Kefa', 'Keyboard', 'Khmer MN', 'Khmer Sangam MN',
                        'Kohinoor', 'KohinoorBangla', 'KohinoorTelugu', 'Kokonor', 'Krungthep', 'KufiStandardGK',
                        'Lao MN', 'Lao Sangam MN', 'LastResort', 'LucidaGrande', 'Luminari', 'Malayalam MN',
                        'Malayalam Sangam MN', 'Marion', 'MarkerFelt', 'Menlo', 'Microsoft Sans Serif', 'Mishafi',
                        'Mishafi Gold', 'Mshtakan', 'Muna', 'Myanmar MN', 'Myanmar Sangam MN', 'NISC18030', 'Nadeem',
                        'NewPeninimMT', 'Noteworthy', 'NotoNastaliq', 'Optima', 'Oriya MN', 'Oriya Sangam MN', 'PTMono',
                        'PTSans', 'PTSerif', 'PTSerifCaption', 'Palatino', 'Papyrus', 'Phosphate', 'PingFang',
                        'PlantagenetCherokee', 'Raanana', 'Rockwell', 'SFCompactDisplay-Black', 'SFCompactDisplay-Bold',
                        'SFCompactDisplay-Heavy', 'SFCompactDisplay-Light', 'SFCompactDisplay-Medium',
                        'SFCompactDisplay-Regular', 'SFCompactDisplay-Semibold', 'SFCompactDisplay-Thin',
                        'SFCompactDisplay-Ultralight', 'SFCompactRounded-Black', 'SFCompactRounded-Bold',
                        'SFCompactRounded-Heavy', 'SFCompactRounded-Light', 'SFCompactRounded-Medium',
                        'SFCompactRounded-Regular', 'SFCompactRounded-Semibold', 'SFCompactRounded-Thin',
                        'SFCompactRounded-Ultralight', 'SFCompactText-Bold', 'SFCompactText-BoldItalic',
                        'SFCompactText-Heavy', 'SFCompactText-HeavyItalic', 'SFCompactText-Light',
                        'SFCompactText-LightItalic', 'SFCompactText-Medium', 'SFCompactText-MediumItalic',
                        'SFCompactText-Regular', 'SFCompactText-RegularItalic', 'SFCompactText-Semibold',
                        'SFCompactText-SemiboldItalic', 'SFNSDisplay', 'SFNSDisplay-BlackItalic',
                        'SFNSDisplay-BoldItalic', 'SFNSDisplay-HeavyItalic', 'SFNSDisplay-LightItalic',
                        'SFNSDisplay-MediumItalic', 'SFNSDisplay-RegularItalic', 'SFNSDisplay-SemiboldItalic',
                        'SFNSDisplay-ThinG1', 'SFNSDisplay-ThinG2', 'SFNSDisplay-ThinG3', 'SFNSDisplay-ThinG4',
                        'SFNSDisplay-ThinItalic', 'SFNSDisplay-UltralightItalic', 'SFNSDisplayCondensed-Black',
                        'SFNSDisplayCondensed-Bold', 'SFNSDisplayCondensed-Heavy', 'SFNSDisplayCondensed-Light',
                        'SFNSDisplayCondensed-Medium', 'SFNSDisplayCondensed-Regular', 'SFNSDisplayCondensed-Semibold',
                        'SFNSDisplayCondensed-Thin', 'SFNSDisplayCondensed-Ultralight', 'SFNSRounded',
                        'SFNSSymbols-Black', 'SFNSSymbols-Bold', 'SFNSSymbols-Heavy', 'SFNSSymbols-Light',
                        'SFNSSymbols-Medium', 'SFNSSymbols-Regular', 'SFNSSymbols-Semibold', 'SFNSSymbols-Thin',
                        'SFNSSymbols-Ultralight', 'SFNSText', 'SFNSTextCondensed-Bold', 'SFNSTextCondensed-Heavy',
                        'SFNSTextCondensed-Light', 'SFNSTextCondensed-Medium', 'SFNSTextCondensed-Regular',
                        'SFNSTextCondensed-Semibold', 'SFNSTextItalic', 'STHeiti Light', 'STHeiti Medium','STIXGeneral',
                        'STIXGeneralBol', 'STIXGeneralBolIta', 'STIXGeneralItalic', 'STIXIntDBol', 'STIXIntDReg',
                        'STIXIntSmBol', 'STIXIntSmReg', 'STIXIntUpBol', 'STIXIntUpDBol', 'STIXIntUpDReg','STIXIntUpReg',
                        'STIXIntUpSmBol', 'STIXIntUpSmReg', 'STIXNonUni', 'STIXNonUniBol', 'STIXNonUniBolIta',
                        'STIXNonUniIta', 'STIXSizFiveSymReg','STIXSizFourSymBol','STIXSizFourSymReg','STIXSizOneSymBol',
                        'STIXSizOneSymReg', 'STIXSizThreeSymBol', 'STIXSizThreeSymReg', 'STIXSizTwoSymBol',
                        'STIXSizTwoSymReg', 'STIXVar', 'STIXVarBol', 'Sana', 'Sathu', 'Savoye LET', 'Seravek',
                        'Shree714', 'SignPainter', 'Silom', 'Sinhala MN', 'Sinhala Sangam MN', 'Skia', 'SnellRoundhand',
                        'Songti', 'SukhumvitSet', 'SuperClarendon', 'Symbol', 'Tahoma', 'Tahoma Bold', 'Tamil MN',
                        'Tamil Sangam MN', 'Telugu MN', 'Telugu Sangam MN', 'Thonburi', 'Times', 'Times New Roman',
                        'Times New Roman Bold', 'Times New Roman Bold Italic', 'Times New Roman Italic', 'Trattatello',
                        'Trebuchet MS', 'Trebuchet MS Bold', 'Trebuchet MS Bold Italic', 'Trebuchet MS Italic',
                        'Verdana', 'Verdana Bold', 'Verdana Bold Italic', 'Verdana Italic', 'Waseem', 'Webdings',
                        'Wingdings', 'Wingdings 2', 'Wingdings 3', 'ZapfDingbats', 'Zapfino', 'ヒラギノ丸ゴ ProN W4',
                        'ヒラギノ明朝 ProN', 'ヒラギノ角ゴシック W0', 'ヒラギノ角ゴシック W1', 'ヒラギノ角ゴシック W2',
                        'ヒラギノ角ゴシック W3', 'ヒラギノ角ゴシック W4', 'ヒラギノ角ゴシック W5', 'ヒラギノ角ゴシック W6',
                        'ヒラギノ角ゴシック W7', 'ヒラギノ角ゴシック W8', 'ヒラギノ角ゴシック W9']

        ui.palette_cb.addItems(palette_options)
        ui.fonts_cb.addItems(font_options)

        ui.buttonBox.accepted.connect(lambda: sns_set_fun())
        ui.context_cb.setCurrentText(self.context)
        ui.style_cb.setCurrentText(self.style)
        ui.palette_cb.setCurrentText(self.c_palette)
        ui.fontscale_sb.setValue(self.fs)
        ui.fonts_cb.setCurrentText(self.font)
        ui.axes_facecolor_le.setText(self.axes_facecolor)
        ui.fig_facecolor_le.setText(self.fig_facecolor)
        d.exec_()

        self.settings.setValue('sns_context',self.context)
        self.settings.setValue('sns_style', self.style)
        self.settings.setValue('sns_c_palette', self.c_palette)
        self.settings.setValue('sns_fontscale', self.fs)
        self.settings.setValue('sns_font',self.font)
        self.settings.setValue('sns_axesfacecolor', self.axes_facecolor)
        self.settings.setValue('sns_figfacecolor', self.fig_facecolor)

    def se_help_function(self):
        print('the best color is: #b63841ff')

    def clear_single_graph(self):
        self.ax.clear()
        self.fig.tight_layout()
        self.dragh = DragHandler(self, figure=self.fig)
        self.canvas.draw()

    def clear_all_graphs(self):
        self.ax_1.clear()
        if self.ax_2 is not None:
            self.ax_2.clear()
        if self.ax_3 is not None:
            self.ax_3.clear()
        if self.ax_4 is not None:
            self.ax_4.clear()
        ApplicationSettings.ALL_DATA_PLOTTED = {}
        self.ax.callbacks.connect('xlim_changed', self.lims_change)
        self.dragh = DragHandler(self, figure=self.fig)
        self.fig.tight_layout()
        self.canvas.draw()

    def cleargraph(self):
        self.dw_XPS.ui.fit_range_cb.clear()
        self.dw_XPS.fit_obj.clear()
        self.ax.clear()
        self.fig.clf()
        del self.fig
        self.ui.verticalLayout.removeWidget(self.toolbar)
        self.ui.verticalLayout.removeWidget(self.canvas)
        self.toolbar.close()
        self.canvas.close()
        self.fig = figure(num=None, figsize=(8, 6), dpi=80)
        self.canvas = FigureCanvas(self.fig)
        self.toolbar = NavigationToolbar(self.canvas, self.canvas, coordinates=True)
        self.ui.verticalLayout.addWidget(self.toolbar)
        self.ui.verticalLayout.addWidget(self.canvas)
        self.ax = self.fig.add_subplot(111)
        self.canvas.installEventFilter(self)
        self.ax.callbacks.connect('xlim_changed', self.lims_change)
        self.ax.callbacks.connect('ylim_changed', self.lims_change)
        ApplicationSettings.ALL_DATA_PLOTTED = {}
        self.fig.tight_layout()
        self.canvas.draw()
        self.ax_2 = None
        self.ax_3 = None
        self.ax_4 = None
        self.dragh = DragHandler(self, figure=self.fig)

    def import_fitted_parameters(self):
        pass

    def closeEvent(self, e):
        # Write window size and position to config file
        self.settings.setValue("size", self.size())
        # self.settings.setValue("pos", self.pos())
        e.accept()

# class DragHandler(object):
#     """ A simple class to handle Drag n Drop.
#
#     This is a simple example, which works for Text objects only
#     """
#     def __init__(self,main_window, figure=None):
#         """ Create a new drag handler and connect it to the figure's event system.
#         If the figure handler is not given, the current figure is used instead
#         """
#         if figure is None : figure = matplotlib.pyplot.gcf()
#         # simple attibute to store the dragged text object
#         self.dragged = None
#         self.main_window = main_window
#         # Connect events and callbacks
#         figure.canvas.mpl_connect("pick_event", self.on_pick_event)
#         figure.canvas.mpl_connect("button_release_event", self.on_release_event)
#         # figure.canvas.mpl_connect("button_release_event", self.on_release)
#
#     def on_pick_event(self, event):
#         " Store which text object was picked and were the pick event occurs."
#         if isinstance(event.artist, Text):
#             self.dragged = event.artist
#             self.pick_pos = (event.mouseevent.xdata, event.mouseevent.ydata)
#         return True
#
#     def on_release_event(self, event):
#         " Update text position and redraw"
#         if self.dragged is not None :
#             old_pos = self.dragged.get_position()
#             new_pos = (old_pos[0] + event.xdata - self.pick_pos[0],
#                        old_pos[1] + event.ydata - self.pick_pos[1])
#             self.dragged.set_position(new_pos)
#             self.dragged = None
#             self.main_window.canvas.draw()
#         return True
