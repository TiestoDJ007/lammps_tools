#!/usr/bin/env python
# -*- coding=utf-8 -*-
import numpy as np
from linecache import getline
import matplotlib.pyplot as plt

#Dir_data = '/mnt/c/Users/a/OneDrive/Calculation_Data/Molecular_Dynamics/Cu_Al_Diffusion/Strain_data/'
#Temp = [600,650,700,750,800]
#Pressure = 150

data_z_ideal, data_z_Cu,data_z_Al,data_z_diffusion= [],[],[],[]
for i in range(2, 301):
    line = getline('{}'.format('Cu_Al_ideal_strain.data'), i).split(" ")
    data_z_ideal.append(np.array((float(line[2]), float(line[5]))))
data_z_ideal = np.array(data_z_ideal)
initial_z_ideal = data_z_ideal[0][0]

for i in range(2, 301):
    line = getline('{}'.format('Cu_monocrystal_strain.data'), i).split(" ")
    data_z_Cu.append(np.array((float(line[2]), float(line[5]))))
data_z_Cu= np.array(data_z_Cu)
initial_z_Cu = data_z_Cu[0][0]

for i in range(2, 301):
    line = getline('{}'.format('Cu_Al_strain_750K_50MPa'), i).split(" ")
    data_z_diffusion.append(np.array((float(line[2]), float(line[5]))))
data_z_diffusion = np.array(data_z_diffusion)
initial_z_diffusion = data_z_diffusion[0][0]

for i in range(2, 301):
    line = getline('{}'.format('Al_monocrystal_strain.data'), i).split(" ")
    data_z_Al.append(np.array((float(line[2]), float(line[5]))))
data_z_Al = np.array(data_z_Al)
initial_z_Al = data_z_Al[0][0]


plt.figure(figsize=(10,4))
#plt.plot((-initial_z_ideal+data_z_ideal[:,0])/initial_z_ideal,data_z_ideal[:,1],label='Ideal contact Cu/Al')
#plt.plot((-initial_z_Cu+data_z_Cu[:,0])/initial_z_Cu,data_z_Cu[:,1],label='Cu')
#plt.plot((-initial_z_Al+data_z_Al[:,0])/initial_z_Al,data_z_Al[:,1],label='Al')
plt.plot((-initial_z_diffusion+data_z_diffusion[:,0])/initial_z_diffusion,data_z_diffusion[:,1],label='Diffusion Cu/Al')
#plt.plot(np.arange(299),data_z[:,1])
plt.legend(loc='upper left',fontsize=14,fancybox=False,shadow=False,frameon=False)

plt.xlim(0,0.3)
plt.ylim(0,4.5)
#plt.xticks(fontsize=16)
plt.ylabel('Stress (GPa)',fontsize=16)
plt.xlabel('Strain (%)',fontsize=16)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.title('{}'.format('Tensile stress–strain curves '),fontsize=16)
plt.savefig('{}'.format('/mnt/d/'+'MPa.png'))
plt.show()
