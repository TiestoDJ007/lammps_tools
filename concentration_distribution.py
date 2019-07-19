#!/usr/bin/env python
# -*- coding=utf-8 -*-

import numpy as np
from linecache import getline
import matplotlib.pyplot as plt

File_name = '600K'
Cu_position,Al_position = [],[]
for num_line in range(1,70721):
    line = getline('{}'.format(File_name), num_line).split(" ")
    if line[3] == 'Cu\n':
        Cu_position.append(np.array((float(line[0]),float(line[1]),float(line[2]))))
    else:
        Al_position.append(np.array((float(line[0]),float(line[1]),float(line[2]))))
Cu_position = np.array(Cu_position)
Al_position = np.array(Al_position)

Al_number ,Cu_number= [],[]
for position in np.arange(-60,60,0.5):
    number = 0
    for num_Al in range(len(Al_position)):
        if position<Al_position[num_Al][2]<=position+0.5:
            number=number+1
    Al_number.append(np.array((position,number)))
Cu_number = []
for position in np.arange(-60,60,0.5):
    number = 0
    for num_Cu in range(len(Cu_position)):
        if position<Cu_position[num_Cu][2]<=position+0.5:
            number=number+1
    Cu_number.append(np.array((position,number)))
Al_number = np.array(Al_number)
Cu_number = np.array(Cu_number)

percent = np.array((Al_number[:,0],Al_number[:,1]/(Al_number[:,1]+Cu_number[:,1]),Cu_number[:,1]/(Al_number[:,1]+Cu_number[:,1])))

plt.figure()
plt.xlabel('{}'.format('Z Direction Distance (')+r'$\AA$'+')',fontsize = 16)
plt.ylabel('Concentration (at%)',fontsize=16)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.xlim((-55,55))
plt.plot(percent[0],percent[1]*100,linewidth=3.5)
plt.plot(percent[0],percent[2]*100,linewidth=3.5)
plt.show()
