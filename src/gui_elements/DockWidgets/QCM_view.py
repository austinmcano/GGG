from src.Ui_Files.DockWidgets.Py.dw_QCM import Ui_DockWidget
from src.gui_elements.RC_Fucntions import *
import pandas as pd
from PySide2 import QtCore
from src.gui_elements.general_functions import *
from src.gui_elements.plotting_functions import *

class QCM_view(QtWidgets.QDockWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.ui = Ui_DockWidget()
        self.ui.setupUi(self)

        self._init_vars()
        self._init_widgets()
        self._init_UI()

    def _init_vars(self):
        # self.ax = self.main_window.ax
        self.current_data_container = None
        self.time = None
        self.pressure = None
        self.mass = None
        self.data = None

    def _init_widgets(self):
        self.tree_view = self.ui.QCMtreeView
        self.context_menu = QtWidgets.QMenu(self)
        # Create context menu
        rc_browser_options(self)

    def _init_UI(self):
        self.model = QtWidgets.QFileSystemModel()
        # self.model.setRootPath(QtCore.QDir.currentPath())
        self.model.setRootPath('')

        self.tree_view.setModel(self.model)
        self.tree_view.setSortingEnabled(True)

        self.tree_view.sortByColumn(True)
        self.tree_view.setRootIndex(self.model.index(self.main_window.settings.value('QCM_PATH')))

        self.tree_view.setModel(self.model)
        self.tree_view.installEventFilter(self)
        self.tree_view.setColumnWidth(0, 100)
        self.model.sort(0, order=QtCore.Qt.SortOrder.AscendingOrder)

        self.ui.fill_cols_pb.clicked.connect(lambda: self.fill_colls())
        self.ui.cols_plot_pb.clicked.connect(lambda: self.qcm())
        self.ui.treeWidget_time.currentItemChanged.connect(lambda: self.load_data(self.ui.treeWidget_time))
        self.ui.treeWidget_pressure.currentItemChanged.connect(lambda: self.load_data(self.ui.treeWidget_pressure))
        self.ui.treeWidget_mass.currentItemChanged.connect(lambda: self.load_data(self.ui.treeWidget_mass))

    def time_change(self):
        if self.ui.time_option.currentText() == 'From:To Time':
            self.ui.From_Time.setText('0')
            self.ui.To_Time.setText('9999999')

    def eventFilter(self, object, event):
        # For right click events
        if event.type() == QtCore.QEvent.ContextMenu:
            self.context_menu.exec_(self.mapToGlobal(event.pos()))
        return False

    def qcm_basic(self):
        self.main_window.ax.set_xlabel('Cycles')
        self.main_window.ax.set_ylabel('Thickness Change (ng/cm$^2$ cycle)')
        leg = self.main_window.ax.legend(loc='best')
        leg.set_draggable(True)
        self.main_window.fig.tight_layout()
        self.main_window.canvas.draw()

    def fill_colls(self):
        self.time = None
        self.mass = None
        self.pressure = None
        self.ui.treeWidget_time.clear()
        self.ui.treeWidget_pressure.clear()
        self.ui.treeWidget_mass.clear()

        path = self.model.filePath(self.tree_view.currentIndex())
        filename, extension = os.path.splitext(path)
        if extension == '.CSV' or extension == '.csv':
            self.data = pd.read_csv(path,delimiter=',', skiprows=0)
        elif extension == '.xls' or extension == '.xlxs':
            excelfile = pd.ExcelFile(path)
            self.data = pd.read_excel(excelfile, "Sheet1")
        elif extension == '.X01':
            self.data = pd.read_csv(path, delimiter='   ', skiprows=48, engine='python')
        else:
            print(extension)
            self.data = pd.read_csv(path,sep='\t')
        strings = [col for col in self.data.columns]
        column_list_time = []
        column_list_pressure = []
        column_list_mass = []
        for i in strings:
            column_list_time.append(QtWidgets.QTreeWidgetItem([i]))
            column_list_pressure.append(QtWidgets.QTreeWidgetItem([i]))
            column_list_mass.append(QtWidgets.QTreeWidgetItem([i]))
            self.ui.treeWidget_time.addTopLevelItems(column_list_time)
            self.ui.treeWidget_pressure.addTopLevelItems(column_list_pressure)
            self.ui.treeWidget_mass.addTopLevelItems(column_list_mass)

    def load_data(self, widget):
        try:
            name = widget.currentIndex().data()
            if widget is self.ui.treeWidget_time:
                self.time = self.data[name].to_numpy()
            elif widget is self.ui.treeWidget_pressure:
                self.pressure = self.data[name].to_numpy()
                if type(self.pressure[0]) is str:
                    for i in range(len(self.pressure)):
                        self.pressure[i] = float(self.pressure[i].split(' ')[0])
            elif widget is self.ui.treeWidget_mass:
                self.mass = self.data[name].to_numpy()
        except KeyError:
            print('Change Came From Fill Columns')

    def qcm(self):
        if self.ui.ax_cb.currentText() == 'Left Ax':
            self.ax = self.main_window.ax
        elif self.ui.ax_cb.currentText() == 'Right Ax':
            if self.main_window.ax_2 is None:
                self.main_window.ax_2 = self.main_window.ax.twinx()
            self.ax = self.main_window.ax_2
        if self.ui.time_option.currentText()=='From:To Time':
            lims = [int(self.ui.From_Time.text()),int(self.ui.To_Time.text())]
        elif self.ui.time_option.currentText()=='Plot Limits':
            lims = ApplicationSettings.C_X_LIM
            self.ui.From_Time.setText(str(int(lims[0])))
            self.ui.To_Time.setText(str(int(lims[1])))
        if self.ui.plot_type_cb.currentText() == "Pressure":
            ApplicationSettings.ALL_DATA_PLOTTED['Pressure'] = self.ax.plot(self.time,self.pressure, label='Pressure')
        elif self.ui.plot_type_cb.currentText() == "Mass":
            ApplicationSettings.ALL_DATA_PLOTTED['Mass'] = self.ax.plot(self.time,self.mass, label='Mass (ng/cm$^2$)')
        elif self.ui.plot_type_cb.currentText() == "Mass Sub":
            ApplicationSettings.ALL_DATA_PLOTTED['Mass'] = self.ax.plot(self.time,self.mass-self.mass[0], label='Mass (ng/cm$^2$)')
        elif self.ui.plot_type_cb.currentText()=="Half+Full Cycle":
            mc_a, mc_b, mc_f, hcd_a, hcd_b, fc_d = self.qcm_anal(self.time, self.pressure, self.mass,
                                                            a_exp=int(self.ui.num_A.value()),
                                                            b_exp=int(self.ui.num_B.value()),
                                                            ttp=float(self.ui.time_through_purge.text()),
                                                            threshold=float(self.ui.P_Threshold.text()),
                                                            from_time=lims[0],
                                                            to_time=lims[1],
                                                            wait_time=float(self.ui.wait_LE.text()),
                                                            density=float(self.ui.Density.text()))
            ApplicationSettings.ALL_DATA_PLOTTED['MC_A'] = self.ax.plot(mc_a, label='Mass Change A')
            ApplicationSettings.ALL_DATA_PLOTTED['MC_B'] = self.ax.plot(mc_b, label='Mass Change B')
            ApplicationSettings.ALL_DATA_PLOTTED['MC_F'] = self.ax.plot(mc_f, label='Cycle Mass Change')
        elif self.ui.plot_type_cb.currentText() == "Half Cycle":
            mc_a, mc_b, mc_f, hcd_a, hcd_b, fc_d = \
                self.qcm_anal(self, self.time, self.pressure, self.mass,a_exp=int(self.ui.num_A.value()),
                              b_exp=int(self.ui.num_B.value()),ttp=float(self.ui.time_through_purge.text()),
                              threshold=float(self.ui.P_Threshold.text()),from_time=lims[0],to_time=lims[1],
                              wait_time=float(self.ui.wait_LE.text()),density=float(self.ui.Density.text()))
            ApplicationSettings.ALL_DATA_PLOTTED['MC_A'] = self.ax.plot(mc_a, label='Mass Change A')
            ApplicationSettings.ALL_DATA_PLOTTED['MC_B'] = self.ax.plot(mc_b, label='Mass Change B')
        elif self.ui.plot_type_cb.currentText() == "Half Cycle Density":
            pass
        elif self.ui.plot_type_cb.currentText() == 'Half+Full Cycle (Mass Only)':
            mc_a, mc_b, mc_f = self.mass_qcm_anal(self.time,self.mass,
                                                  float(self.ui.start_time_LE.text()),
                                                  float(self.ui.adp_time_LE.text()),
                                                  float(self.ui.bdp_time_LE.text()),
                                                  num_cycles=int(self.ui.num_exp_LE.text()))
            ApplicationSettings.ALL_DATA_PLOTTED['MC_A'] = self.ax.plot(mc_a, label='Mass Change A')
            ApplicationSettings.ALL_DATA_PLOTTED['MC_B'] = self.ax.plot(mc_b, label='Mass Change B')
            ApplicationSettings.ALL_DATA_PLOTTED['MC_F'] = self.ax.plot(mc_f, label='Cycle Mass Change')
        elif self.ui.plot_type_cb.currentText() == 'Half Cycle (Mass Only)':
            mc_a, mc_b, mc_f = self.mass_qcm_anal(self.time, self.mass,
                                                  float(self.ui.start_time_LE.text()),
                                                  float(self.ui.adp_time_LE.text()),
                                                  float(self.ui.bdp_time_LE.text()),
                                                  num_cycles=int(self.ui.num_exp_LE.text()))
            ApplicationSettings.ALL_DATA_PLOTTED['MC_A'] = self.ax.plot(mc_a, label='Mass Change A')
            ApplicationSettings.ALL_DATA_PLOTTED['MC_B'] = self.ax.plot(mc_b, label='Mass Change B')
        self.main_window.fig.tight_layout()
        self.main_window.canvas.draw()

    def qcm_anal(self, time, pressure, mass, a_exp=int, b_exp=int, ttp=float, threshold=float, from_time=int,
                 to_time=int,wait_time=float, density=float):
        #  Few more assignments Exposures is the time of each Exposure, the Index is just what index it
        #  shows up as. M_Diff and P_Diff are the mass and pressure difference at different exposures
        #  Purge Time Index is the number of data points between one exposure and the next, does not
        #  differentiate for the exposure time.
        Exposures = []
        A_Exposures = a_exp
        Exposure_index = []
        QCM_M_Diff = []
        QCM_P_Diff = []
        MC_A = []
        MC_B = []
        MC_P = []
        MC_N = []
        MC_Cycle = []

        t = 0
        #  Time through purge is the time to "wait" after there is an exposure to not overcount exposures
        #  Time is just a temp variable that gives the time of the last exposure

        # This for loop is just for appending the exposures to Exposures and Exposure_index nee
        for num in range(len(pressure) - 10):
            QCM_M_Diff.append(mass[num + 3] - mass[num])
            QCM_P_Diff.append(pressure[num + 3] - pressure[num])
            if QCM_P_Diff[num] >= threshold and time[num] - t > wait_time and time[num] > from_time and time[
                num] < to_time:
                Exposures.append(time[num])
                Exposure_index.append(num)
                t = time[num]

                # self.main_window.ax.axvline(time[num], color='gray', lw=1, alpha=0.5)
                # above line will add a line for each exposure if someone is uncertain about if its right

        # This for loop is knowing how long each purge time is (or time from one exposure to next)
        Purge_Time_Index = np.zeros(len(Exposure_index))

        for num in range(len(Exposure_index) - 1):
            if (Exposure_index[num + 1] - Exposure_index[num]) < 2000:
                Purge_Time_Index[num] = Exposure_index[num + 1] - Exposure_index[num]

        Purge_Time_Index[-1] = Purge_Time_Index[0]

        # print(Purge_Time_Index)

        #  for loop finds the mass at the: Exposure time + Purge_time*(time_through_purge) which takes the time
        #  of the last exposure and then adds something like 0.8*Time of purge... Insert is to do the last one
        #  if else says if Mass_Middle was bigger or smaller than the last one and sorts it into one of two lists
        #  Last if else sorts based on if num is odd or even... For A-B experiemtns.. Nothing for A BBB or some
        #  Thing like that
        mass_middle = np.zeros(len(Exposure_index) + 2)
        mass_middle[0] = mass[Exposure_index[0] - int(Purge_Time_Index[0] * ttp)]
        # mass_middle.insert(0, mass[Exposure_index[0] - int(Purge_Time_Index[0] * ttp)])

        for num in range(len(Exposure_index)):
            # mass_middle.append(mass[int(Exposure_index[num] + int(Purge_Time_Index[num] * ttp))])
            mass_middle[num + 1] = mass[int(Exposure_index[num] + int(Purge_Time_Index[num] * ttp))]
            # self.main_window.ax.axvline(time[num], color='gray', lw=1, alpha=0.5)
            # above line will add a line for each time if someone is uncertain about if its right

        # mass_middle.append(mass[Exposure_index[-1] + int(Purge_Time_Index[0] * ttp)])
        mass_middle[-1] = mass[Exposure_index[-1] + int(Purge_Time_Index[0] * ttp)]

        # print('There was ' + str(len(Exposures)) + '  Precursor Exposures')
        self.main_window.dw_QCM.ui.num_doses.setText(str(len(Exposures)))

        for num in range(len(Exposure_index)):
            if mass_middle[num + 1] - mass_middle[num] > 0:
                MC_P.append(mass_middle[num + 1] - mass_middle[num])
            elif mass_middle[num + 1] - mass_middle[num] < 0:
                MC_N.append(mass_middle[num + 1] - mass_middle[num])
            if num % (b_exp + A_Exposures) == 0:
                MC_Cycle.append(mass_middle[num + b_exp + A_Exposures] - mass_middle[num])
            if num == a_exp - 1:
                MC_A.append(mass_middle[num + 1] - mass_middle[num + 1 - A_Exposures])
            elif num == b_exp + a_exp - 1:
                MC_B.append(mass_middle[num + 1] - mass_middle[num + 1 - b_exp])
            elif num == a_exp + b_exp:
                a_exp = a_exp + A_Exposures + b_exp
                if num == a_exp - 1:
                    MC_A.append(mass_middle[num + 1] - mass_middle[
                        num + 1 - A_Exposures])

                # elif num == B_Doses + A_Doses:
                #     self.QCM_Dict['MC_B'].QCM_B.append(Mass_Middle[num] - Mass_Middle[num + 1 - int(B_Exposures.text())])
        half_cycle_density_A = np.zeros(len(MC_A))
        half_cycle_density_B = np.zeros(len(MC_B))
        full_cycle_density = np.zeros(len(MC_Cycle))
        for i in range(len(MC_A)):
            half_cycle_density_A[i] = MC_A[i] / (10.0 * density)
        for i in range(len(MC_B)):
            half_cycle_density_B[i] = MC_B[i] / (10.0 * density)
        for i in range(len(MC_Cycle)):
            full_cycle_density[i] = MC_Cycle[i] / (10 * density)

        return MC_A, MC_B, MC_Cycle, half_cycle_density_A, half_cycle_density_B, full_cycle_density

    def mass_qcm_anal(self,time,mass, start_time=float, purge_time_a=float, purge_time_b=float, num_cycles=int):
        # time = data[0]
        # mass = data[2]
        exposure = []
        exposure_idx = []
        mass_hc_a = []
        mass_hc_b = []
        exp_length_idx = []
        # time_in_idx = find_nearest(time, end_time) - find_nearest(time, start_time)
        # mass_process = mass[find_nearest(time, start_time): find_nearest(time, end_time)]
        # time_process = time[find_nearest(time, start_time):find_nearest(time, end_time)]
        mass_process = mass[find_nearest(time, start_time):]
        time_process = time[find_nearest(time, start_time):]
        for i in range(num_cycles):
            if i % 2 == 0:
                exposure.append(start_time + (purge_time_a * i))
                exposure_idx.append(find_nearest(time_process, start_time + (purge_time_a * i)))
            elif i % 2 == 1:
                exposure.append(start_time + (purge_time_b * i))
                exposure_idx.append(find_nearest(time_process, start_time + (purge_time_b * i)))
        for k in range(len(exposure_idx) - 1):
            exp_length_idx.append(exposure_idx[k + 1] - exposure_idx[k])
        for j in range(num_cycles - 1):
            if j % 2 == 0:
                mass_hc_a.append(
                    mass_process[int((exposure_idx[j + 1] - exposure_idx[j]) * .9 + exposure_idx[j])] - mass_process[
                        exposure_idx[j]])
            elif j % 2 == 1:
                mass_hc_b.append(
                    mass_process[int((exposure_idx[j + 1] - exposure_idx[j]) * .9 + exposure_idx[j])] - mass_process[
                        exposure_idx[j]])
        fc = np.zeros(len(mass_hc_b))
        for i in range(len(mass_hc_b)):
            fc[i] = mass_hc_a[i]+mass_hc_b[i]
        return mass_hc_a,mass_hc_b, fc

