#!/usr/bin/env python
# -*- coding=utf-8 -*-

import numpy as np
from numpy import sqrt

if __name__ == "__main__":
    lattice_parameter = 3.597
    cell_basis = np.array([[1, 0, 0],
                           [0, sqrt(2) / 2, 0],
                           [0, 0, sqrt(2) / 2]]) * lattice_parameter
    atom_basis = np.array([[0, 0, 0],
                           [0.5, sqrt(2) / 4, sqrt(2) / 4]]) * lattice_parameter

    system_size = 3
    position = []
    for i in range(system_size):
        for j in range(system_size):
            for k in range(system_size):
                base_position = np.array([i, j, k])
                cart_position = np.inner(cell_basis, base_position)
                for atom in atom_basis:
                    position.append(cart_position + atom)

    fdata = open('temp_datatemp_1.dat', 'w')
    fdata.write('Crystalline Cu atoms\n\n')
    fdata.write('{} atoms\n'.format((len(position))))
    fdata.write('{} atom types\n'.format(1))
    fdata.write('{} {} xlo xhi\n'.format(0.0, system_size * np.linalg.norm(cell_basis[0], 2)))
    fdata.write('{} {} ylo yhi\n'.format(0.0, system_size * np.linalg.norm(cell_basis[1], 2)))
    fdata.write('{} {} zlo zhi\n\n'.format(0.0, system_size * np.linalg.norm(cell_basis[2], 2)))
    fdata.write('\n')
    fdata.write('Atoms\n\n')
    for i, pos in enumerate(position):
        fdata.write('{} 1 {:.6f} {:.6f} {:.6f}\n'.format(i + 1, *pos))
    fdata.close()
