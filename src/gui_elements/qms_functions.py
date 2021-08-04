import pandas as pd
# import matplotlib.pyplot as plt
import numpy as np
# import seaborn as sns

def meshything(masses, operator):
    if len(masses) == 1:
        mesh = np.array(np.meshgrid(masses[0]))
    elif len(masses) == 2:
        mesh = np.array(np.meshgrid(masses[0],masses[1]))
    elif len(masses) == 3:
        mesh = np.array(np.meshgrid(masses[0],masses[1],masses[2]))
    elif len(masses) == 4:
        mesh = np.array(np.meshgrid(masses[0],masses[1],masses[2],masses[3]))
    elif len(masses) == 5:
        mesh = np.array(np.meshgrid(masses[0],masses[1],masses[2],masses[3],masses[4]))
    elif len(masses) == 6:
        mesh = np.array(np.meshgrid(masses[0],masses[1],masses[2],masses[3],masses[4],masses[5]))
    elif len(masses) == 7:
        mesh = np.array(np.meshgrid(masses[0],masses[1],masses[2],masses[3],masses[4],masses[5],masses[6]))
    elif len(masses) == 8:
        mesh = np.array(np.meshgrid(masses[0],masses[1],masses[2],masses[3],masses[4],masses[5],masses[6],masses[7]))
    elif len(masses) == 9:
        mesh = np.array(np.meshgrid(masses[0],masses[1],masses[2],masses[3],masses[4],masses[5],masses[6],masses[7],
                                    masses[8]))
    elif len(masses) == 10:
        mesh = np.array(np.meshgrid(masses[0],masses[1],masses[2],masses[3],masses[4],masses[5],masses[6],masses[7],
                                    masses[8],masses[9]))
    elif len(masses) == 11:
        mesh = np.array(np.meshgrid(masses[0],masses[1],masses[2],masses[3],masses[4],masses[5],masses[6],masses[7],
                                    masses[8],masses[9],masses[10]))
    elif len(masses) == 12:
        mesh = np.array(np.meshgrid(masses[0],masses[1],masses[2],masses[3],masses[4],masses[5],masses[6],masses[7],
                                    masses[8],masses[9],masses[10],masses[11]))
    combinations = mesh.T.reshape(-1, len(masses))
    temp = []
    if operator == 'sum':
        for i in combinations:
            temp.append(np.sum(i))
    elif operator == 'product':
        for i in combinations:
            temp.append(np.prod(i))
    return temp

def isotopic_prediction(name,round=int):
    i = 0
    splitted = list(name)
    while i < len(splitted):
        try:
            splitted[i] = int(splitted[i])
        except ValueError:
            pass
        if type(splitted[i]) is str:
            if type(splitted[i - 1]) is str and i != 0:
                splitted[i] = splitted[i - 1] + splitted[i]
                del splitted[i - 1]
                i = i - 1
        elif type(splitted[i]) is int and i != 0:
            if type(splitted[i - 1]) is int:
                splitted[i] = int(str(splitted[i]) + str(splitted[i - 1]))
                del splitted[i - 1]
                i = i - 1
        i = i + 1
    iso = pd.read_csv(r'C:\Users\austi\Desktop\GGG\src\Resources\Isotopes.csv', delimiter=',')
    masses = []
    abund = []
    for i in range(len(splitted)):
        if type(splitted[i]) == str:
            for j in range(splitted[i + 1]):
                h = iso.loc[iso['Name'] == splitted[i]]
                masses.append(h['Mass'].to_numpy())
                abund.append(h['Abundance'].to_numpy())
    newlist_mass = np.array(meshything(masses, 'sum'))
    newlist_abun = np.array(meshything(abund, 'product'))
    for i in range(len(newlist_mass)):
        newlist_mass[i] = np.round(newlist_mass[i], round)
        newlist_abun[i] = np.round(newlist_abun[i], 1)
    k = 0
    j = 0
    while k < len(newlist_mass):
        while j < len(newlist_mass):
            if newlist_mass[k] == newlist_mass[j] and k != j:
                newlist_abun[k] = newlist_abun[k]+newlist_abun[j]
                newlist_abun = np.delete(newlist_abun, j)
                newlist_mass = np.delete(newlist_mass, j)
            j = j+1
        k = k+1
        j=0
    final_abund = newlist_abun / newlist_abun.max(axis=0) * 100
    return newlist_mass, final_abund

# sns.set(context='notebook',style='ticks',font_scale=2)
# #
# fig, ax = plt.subplots()

# mass, abund = isotopic_prediction('Al2Cl6')
#
# print('The mass list is:')
# print(mass)
# print('The abundance list is:')
# print(abund)
# for i in range(len(mass)):
#     ax.vlines(mass[i], 0, abund[i],label=str(mass[i]))
# plt.show()
