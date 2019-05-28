#!/usr/bin/env python
# -*- coding=utf-8 -*-

import numpy as np

lattice_parameter = 3.6149 
cell_basis = np.array([[1, 0, 0],
                       [0, 1, 0],
                       [0, 0, 1]]) * lattice_parameter
atom_basis = np.array([[0, 0, 0],
                       [0.5, 0.5, 0],
                       [0.5, 0, 0.5],
                       [0, 0.5, 0.5]]) * lattice_parameter

upper_layer = [16, 16, 20]
upper_position = []
for i in range(-8,8,1):
    for j in range(-8,8,1):
        for k in range(upper_layer[2]):
            base_position = [i, j, k + 0.5]
            cart_position = np.inner(cell_basis.T, base_position)
            for atom in atom_basis:
                upper_position.append(cart_position + atom)

under_layer = [15, 15, -20]
under_position = []
for i in range(-8,8,1):
    for j in range(-8,8,1):
        for k in range(under_layer[2],0,1):
            base_position = [i, j, k - 0.5]
            cart_position = np.inner(cell_basis.T, base_position)
            for atom in atom_basis:
                under_position.append(cart_position + atom)

position = np.array(under_position+upper_position)

# 输出reading文件
fdata = open('/mnt/d/Tools/lammps_tools/Cu_HCP.dat', 'w')
fdata.write('Crystalline Cu atoms\n\n')
# 原子个数
fdata.write('{} atoms\n'.format((len(position))))
# 原子种类
fdata.write('{} atom types\n'.format(4))
# Simulation Box Size
fdata.write('{:.6f} {:.6f} xlo xhi\n'.format(position.min(axis=0)[0], position.max(axis=0)[0]+lattice_parameter/2))
fdata.write('{:.6f} {:.6f} ylo yhi\n'.format(position.min(axis=0)[1], position.max(axis=0)[1]+lattice_parameter/2))
fdata.write('{:.6f} {:.6f} zlo zhi\n\n'.format(position.min(axis=0)[2], position.max(axis=0)[2]+lattice_parameter/2))
fdata.write('\n')
fdata.write('Atoms\n\n')
# Atom Position
for i, pos in enumerate(position):
    if 0<=pos[2]<64:
        fdata.write('{} 1 {:.6f} {:.6f} {:.6f}\n'.format(i + 1, *pos))
    elif 0>pos[2]>-66:
        fdata.write('{} 2 {:.6f} {:.6f} {:.6f}\n'.format(i + 1, *pos))
    elif pos[2]>=64:
        fdata.write('{} 3 {:.6f} {:.6f} {:.6f}\n'.format(i + 1, *pos))
    else:
        fdata.write('{} 4 {:.6f} {:.6f} {:.6f}\n'.format(i + 1, *pos))
fdata.close()
