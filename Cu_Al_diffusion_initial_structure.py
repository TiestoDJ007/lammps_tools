#!/usr/bin/env python
# -*- coding=utf-8 -*-

import numpy as np

if __name__ == "__main__":
    Cu_lattice_constant = 3.6150
    Al_lattice_constant = 4.0500
    cell_basis = np.array([[1, 0, 0],
                           [0, 1, 0],
                           [0, 0, 1]])
    atom_basis = np.array([[0, 0, 0],
                           [0.5, 0.5, 0],
                           [0.5, 0, 0.5],
                           [0, 0.5, 0.5]])
    Cu_layer = [22, 22, 20]
    Cu_position = []
    for i in range(-10,12,1):
        for j in range(-10,12,1):
            for k in range(20):
                base_position = [i, j, k]
                cart_position = np.inner(cell_basis.T, base_position)
                for atom in atom_basis:
                    Cu_position.append(cart_position + atom)
    Cu_layer_position = np.array(Cu_position)*Cu_lattice_constant

    Al_layer = [18, 18, -20]
    Al_position = []
    for i in range(-9, 11, 1):
        for j in range(-9, 11, 1):
            for k in range(Al_layer[2], 0, 1):
                base_position = [i, j, k]
                cart_position = np.inner(cell_basis.T, base_position)
                for atom in atom_basis:
                    Al_position.append(cart_position + atom)
    Al_layer_position = np.array(Al_position)*Al_lattice_constant

    position = np.concatenate((Cu_layer_position,Al_layer_position),axis=0)

    # 输出reading文件
    fdata = open('/mnt/d/Tools/lammps_tools/Cu_Al_Bilayer.dat', 'w')
    fdata.write('Crystalline Cu atoms\n\n')
    # 原子个数
    fdata.write('{} atoms\n'.format((len(position))))
    # 原子种类
    fdata.write('{} atom types\n'.format(4))
    # Simulation Box Size
    fdata.write(
        '{:.6f} {:.6f} xlo xhi\n'.format(position.min(axis=0)[0], position.max(axis=0)[0] + Al_lattice_constant / 2))
    fdata.write(
        '{:.6f} {:.6f} ylo yhi\n'.format(position.min(axis=0)[1], position.max(axis=0)[1] + Al_lattice_constant / 2))
    fdata.write(
        '{:.6f} {:.6f} zlo zhi\n\n'.format(position.min(axis=0)[2], position.max(axis=0)[2] + Al_lattice_constant / 2))
    fdata.write('\n')
    fdata.write('Atoms\n\n')
    # Atom Position
    for i, pos in enumerate(position):
        if 0 <= pos[2] < 64:
            fdata.write('{} 1 {:.6f} {:.6f} {:.6f}\n'.format(i + 1, *pos))
        elif 0 > pos[2] > -72:
            fdata.write('{} 2 {:.6f} {:.6f} {:.6f}\n'.format(i + 1, *pos))
        elif pos[2] >= 64:
            fdata.write('{} 3 {:.6f} {:.6f} {:.6f}\n'.format(i + 1, *pos))
        else:
            fdata.write('{} 4 {:.6f} {:.6f} {:.6f}\n'.format(i + 1, *pos))
    fdata.close()