#!/usr/bin/env python
# -*- coding=utf-8 -*-
import numpy as np
from linecache import getline
import matplotlib.pyplot as plt

#Dir_data = '/mnt/c/Users/a/OneDrive/Calculation_Data/Molecular_Dynamics/Cu_Al_Diffusion/Strain_data/'
#Temp = [600,650,700,750,800]
#Pressure = 150
Name_file = 'Cu_monocrystal_strain.data'
data_z = []
for i in range(2, 301):
    line = getline('{}'.format(Name_file), i).split(" ")
    data_z.append(np.array((float(line[2]), float(line[5]))))
data_z = np.array(data_z)
plt.figure(figsize=(10,4))
#plt.plot((-data_z[0][0]+data_z[:,0])/data_z[:,0],data_z[:,1])
plt.plot(np.arange(299),data_z[:,1])
#plt.legend(loc='upper left',fontsize=14,fancybox=True,shadow=False)
#plt.xlim(0,0.3)
plt.ylim(0,9)
#plt.xticks(fontsize=16)
plt.xlabel('Strain GPa',fontsize=16)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.title('{}'.format('Tensile stress–strain curves '),fontsize=16)
plt.savefig('{}'.format('/mnt/d/'+'MPa.png'))
plt.show()
