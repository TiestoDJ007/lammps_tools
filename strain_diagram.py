#!/usr/bin/env python
# -*- coding=utf-8 -*-
import numpy as np
from linecache import getline
import matplotlib.pyplot as plt

DIR_data = '/mnt/c/Users/a/OneDrive/Calculation_Data/Cu_Al_Diffusion/Cooling_Stable/'
FILE_data = '600_50_10_final.cfg'
data_x,data_y,data_z = [],[],[]
for i in range(2,202):
    line = getline('Cu_Al_strain.data',i).split(" ")
    data_x.append(np.array((float(line[0]),float(line[3]))))
    data_y.append(np.array((float(line[1]),float(line[4]))))
    data_z.append(np.array((float(line[2]),float(line[5]))))
data_x = np.array(data_x)
data_y = np.array(data_y)
data_z = np.array(data_z)
initial_x = data_x[0][0]
initial_y = data_y[0][0]
initial_z = data_z[0][0]
plt.figure()
plt.plot((initial_x-data_x[:,0])/initial_x,-data_x[:,1])
#plt.plot((-initial_z+data_z[:,0])/initial_z,data_z[:,1])
plt.show()
