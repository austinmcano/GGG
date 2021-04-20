from src.Ui_Files.Dialogs.Save_To_CSV import Ui_Dialog as TW_ui
from PySide2 import QtWidgets
import numpy as np
from src.Ui_Files.Dialogs.Save_To_CSV import Ui_Dialog as STC_ui
from src.Ui_Files.Dialogs.app_settings import Ui_Dialog as app_settings
from src.Ui_Files.Dialogs.annotation_dialog import Ui_Dialog as annotation_ui
from src.Ui_Files.Dialogs.simple_text import Ui_Dialog as simple_text_ui
from src.Ui_Files.Dialogs.new_project_dialog import Ui_Dialog as new_project_dialog
from src.Ui_Files.Dialogs.simple_treeWidget_dialog import Ui_Dialog as simple_tw
from src.Ui_Files.Dialogs.bargraph_dialog import Ui_Dialog as bar_dialog
from src.Ui_Files.Dialogs.spine_color_dialog import Ui_Dialog as spine_color_dialog
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from PySide2 import QtCore,QtWidgets,QtGui
from src.gui_elements.settings import ApplicationSettings
from scipy import integrate
from scipy.linalg import norm
from scipy.signal import savgol_filter
from scipy import sparse
from scipy.sparse.linalg import spsolve

# def linear_plot_SE(self):
#     dialog = QtWidgets.QDialog()
#     ui = TW_ui()
#     ui.setupUi(dialog)
#     dict = ApplicationSettings.ALL_DATA_PLOTTED
#     Key_List = []
#     for i in dict.keys():
#         Key_List.append(QtWidgets.QTreeWidgetItem([i]))
#     ui.treeWidget.addTopLevelItems(Key_List)
#     dialog.exec_()
#     # save_csv = ui.treeWidget.indexOfTopLevelItem(ui.treeWidget.currentItem())
#     for ix in ui.treeWidget.selectedIndexes():
#         text = ix.data()  # or ix.data(),
#         data = ApplicationSettings.ALL_DATA_PLOTTED[text]
#
#     # trying to deal with nan elements in a list
#     new_data = [[], []]
#     for b in range(len(data)):
#         for c in range(len(data[b])):
#             if not np.isnan(data[b][c]):
#                 new_data[b].append(data[b][c])
#             else:
#                 pass
#     fit = np.polyfit(new_data[0], new_data[1], 1)
#     self.ax.plot(new_data[0], np.poly1d(fit)(new_data[0]))
#     self.canvas.draw()

def keycheck(dict, key):
    if key in dict.keys():
        return True
    else:
        return False

def addmpl(self,fig):
    self.main_window.canvas = FigureCanvas(fig)
    self.ui.verticalLayout.addWidget(self.main_window.canvas)
    self.main_window.canvas.draw()
    self.toolbar = NavigationToolbar(self.main_window.canvas,
                                     self, coordinates=True)
    self.ui.verticalLayout.addWidget(self.main_window.toolbar)

def rmmpl(self):
    self.ui.verticalLayout.removeWidget(self.main_window.canvas)
    self.main_window.canvas.close()
    self.ui.verticalLayout.removeWidget(self.main_window.toolbar)

def qcm_hc_mass(data, start_time=float, end_time=float, purge_time_a=float, purge_time_b=float, num_cycles=int):
    time = data[0]
    mass = data[2]
    exposure = []
    exposure_idx = []
    mass_hc_a = []
    mass_hc_b = []
    exp_length_idx = []
    # time_in_idx = find_nearest(time, end_time) - find_nearest(time, start_time)
    mass_process = mass[find_nearest(time, start_time): find_nearest(time, end_time)]
    time_process = time[find_nearest(time, start_time):find_nearest(time, end_time)]
    print(time_process)
    print(mass_process)
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


def plot_QCM(self, time,pressure,mass,a_exp=int,b_exp=int,ttp=float,threshold=float,from_time=int,to_time=int,
             wait_time=float, density = float):
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
        if QCM_P_Diff[num] >= threshold and time[num] - t > wait_time and time[num] > from_time and time[num] < to_time:
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
    mass_middle = np.zeros(len(Exposure_index)+2)
    mass_middle[0] = mass[Exposure_index[0] - int(Purge_Time_Index[0] * ttp)]
    # mass_middle.insert(0, mass[Exposure_index[0] - int(Purge_Time_Index[0] * ttp)])

    for num in range(len(Exposure_index)):
        # mass_middle.append(mass[int(Exposure_index[num] + int(Purge_Time_Index[num] * ttp))])
        mass_middle[num+1] = mass[int(Exposure_index[num] + int(Purge_Time_Index[num] * ttp))]
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

def find_nearest(array: object, value: object) -> object:
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return idx


def baseline_als(y, lam, p, niter=10):
    # where y is the data needed to be corrected, lam is lambda and is a smoothing
    # parameter and p is the asymmetry of the baseline, niter is the num of iterations
    L = len(y)
    D = sparse.diags([1,-2,1],[0,-1,-2], shape=(L,L-2))
    w = np.ones(L)
    for i in range(niter):
        W = sparse.spdiags(w, 0, L, L)
        Z = W + lam * D.dot(D.transpose())
        z = spsolve(Z, w*y)
        w = p * (y > z) + (1-p) * (y < z)