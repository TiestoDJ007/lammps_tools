#!/usr/bin/env python
# -*- coding=utf-8 -*-
import numpy as np
from linecache import getline
import matplotlib.pyplot as plt

Dir_data = '/mnt/c/Users/jackx/OneDrive/Calculation_Data/Molecular_Dynamics/Cu_Al_Diffusion/Strain_data/'
Temp = 750
Pressure = [50]
data_base = []
for Loop_press in Pressure:
    Name_file = '{}'.format('Cu_Al_strain_' + str(Temp) + 'K_' + str(Loop_press) + 'MPa')
    data_z = []
    for i in range(2, 301):
        line = getline('{}'.format(Dir_data + Name_file), i).split(" ")
        data_z.append(np.array((float(line[2]), float(line[5]))))
    data_z = np.array(data_z)
    data_base.append(data_z)
plt.figure(figsize=(8,4))
for num_press in range(len(Pressure)):
    plt.plot((-data_base[num_press][0][0] + data_base[num_press][:, 0]) / data_base[num_press][0][0],
             data_base[num_press][:, 1], label='{}'.format(str(Pressure[num_press])+'MPa'))
    plt.legend(loc='upper left',fontsize=14,fancybox=True,shadow=False)
plt.xlim(0,0.3)
plt.ylim(0,5)
#plt.xticks(fontsize=16)
plt.xlabel('Strain GPa',fontsize=16)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.title('{}'.format('Tensile stress–strain curves '+str(Temp)+' K'),fontsize=16)
#plt.savefig('{}'.format('/mnt/d/'+str(Temp)+'K.png'))
plt.show()
