#!/usr/bin/env python
# -*- coding=utf-8 -*-

import numpy as np

lattice_parameter = 3.597
cell_basis = np.array([[1, 0, 0],
                       [0, 1, 0],
                       [0, 0, 1]]) * lattice_parameter
atom_basis = np.array([[0, 0, 0],
                       [0.5, 0.5, 0],
                       [0.5, 0, 0.5],
                       [0, 0.5, 0.5]]) * lattice_parameter

upper_layer = [20, 20, 10]
upper_position = []
for i in range(upper_layer[0]):
    for j in range(upper_layer[1]):
        for k in range(upper_layer[2]):
            base_position = [i, j, k]
            cart_position = np.inner(cell_basis.T, base_position)
            for atom in atom_basis:
                upper_position.append(cart_position + atom)

under_layer = [20, 20, -40]
under_position = []
for i in range(under_layer[0]):
    for j in range(under_layer[1]):
        for k in range(-9,0,1):
            base_position = [i, j, k]
            cart_position = np.inner(cell_basis.T, base_position)
            for atom in atom_basis:
                under_position.append(cart_position + atom)

position = np.array(under_position+upper_position)

# 输出reading文件
fdata = open('/mnt/d/tempdata/bc_ps.dat', 'w')
fdata.write('Crystalline Cu atoms\n\n')
# 原子个数
fdata.write('{} atoms\n'.format((len(position))))
# 原子种类
fdata.write('{} atom types\n'.format(2))
# Simulation Box Size
fdata.write('{:.6f} {:.6f} xlo xhi\n'.format(position.min(axis=0)[0], position.max(axis=0)[0]+lattice_parameter/2))
fdata.write('{:.6f} {:.6f} ylo yhi\n'.format(position.min(axis=0)[1], position.max(axis=0)[1]+lattice_parameter/2))
fdata.write('{:.6f} {:.6f} zlo zhi\n\n'.format(position.min(axis=0)[2], position.max(axis=0)[2]+lattice_parameter/2))
fdata.write('\n')
fdata.write('Atoms\n\n')
# Atom Position
for i, pos in enumerate(position):
    if pos[2]>=0:
        fdata.write('{} 1 {:.6f} {:.6f} {:.6f}\n'.format(i + 1, *pos))
    else:
        fdata.write('{} 2 {:.6f} {:.6f} {:.6f}\n'.format(i + 1, *pos))
fdata.close()
