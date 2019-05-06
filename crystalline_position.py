#!/usr/bin/env python
# -*- coding=utf-8 -*-

import numpy as np

lattice_parameter = 3.597
cell_basis = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]]) * lattice_parameter
atom_basis = np.array([[0, 0, 0], [0.5, 0.5, 0], [0, 0.5, 0.5],
                       [0.5, 0, 0.5]]) * lattice_parameter
system_size = 20
position = []
for i in range(system_size):
    for j in range(system_size):
        for k in range(system_size):
            base_position = np.array([i, j, k])
            cart_position = np.inner(cell_basis.T, base_position)
            for atom in atom_basis:
                position.append(cart_position + atom)

# 输出reading文件
fdata = open('/mnt/d/tempdata/ps.dat', 'w')
fdata.write('Crystalline Cu atoms\n\n')
# 原子个数
fdata.write('{} atoms\n'.format((len(position))))
# 原子种类
fdata.write('{} atom types\n'.format(1))
# Simulation Box Size
fdata.write('{} {} xlo xhi\n'.format(0.0, system_size*lattice_parameter))
fdata.write('{} {} ylo yhi\n'.format(0.0, system_size*lattice_parameter))
fdata.write('{} {} zlo zhi\n\n'.format(0.0, system_size*lattice_parameter))
fdata.write('\n')
fdata.write('Atoms\n\n')
# Atom Position
for i, pos in enumerate(position):
    fdata.write('{} 1 {:.6f} {:.6f} {:.6f}\n'.format(i + 1, *pos))
fdata.close()
