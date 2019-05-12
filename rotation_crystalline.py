#!/usr/bin/env python
# -*- coding=utf-8 -*-

import numpy as np
from numpy import sin, cos,sqrt


def rotation_x(position_array, phi):
    rotation_matrix_x = np.array([[1, 0, 0],
                                  [0, cos(phi), -sin(phi)],
                                  [0, sin(phi), cos(phi)]])
    return np.dot(position_array, rotation_matrix_x)


def rotation_y(position_array, theta):
    rotation_matrix_y = np.array([[cos(theta), 0, sin(theta)],
                                  [0, 1, 0],
                                  [-sin(theta), 0, cos(theta)]])
    return np.dot(position_array, rotation_matrix_y)


def rotation_z(position_array, psi):
    rotation_matrix_z = np.array([[cos(psi), -sin(psi), 0],
                                  [sin(psi), cos(psi), 0],
                                  [0, 0, 1]])
    return np.dot(position_array, rotation_matrix_z)


def rotation_3d(position_array, phi, theta, psi):
    rotation_matrix_3d = np.array([[cos(theta) * cos(psi), -cos(phi) * sin(psi) + sin(phi) * sin(theta) * cos(psi),
                                    sin(theta) * sin(psi) + cos(phi) * sin(theta) * cos(psi)],
                                   [cos(theta) * sin(psi), cos(phi) * cos(psi) + sin(phi) * sin(theta) * sin(psi),
                                    -sin(theta) * cos(psi) + cos(phi) * sin(theta) * sin(psi)],
                                   [-sin(theta), sin(phi) * cos(theta), cos(phi) * cos(theta)]])
    return np.dot(position_array, rotation_matrix_3d)


def grain_boundary(position_array, direction_x, direction_y):
    return 0


if __name__ == "__main__":
    lattice_parameter = 3.597
    cell_basis = np.array([[1, 0, 0],
                           [0, 1, 0],
                           [0, 0, 1]]) * lattice_parameter
    fcc_basis = np.array([[0, 0, 0],
                          [0.5, 0.5, 0],
                          [0, 0.5, 0.5],
                          [0.5, 0, 0.5]]) * lattice_parameter

    rotation_basis = rotation_x(cell_basis,np.pi/4)
    system_size = 2
    system_box = cell_basis * system_size
    inv_rotation_basis = np.linalg.inv(rotation_basis)
    rotation_system_box = np.matmul(system_box,inv_rotation_basis)


    position = []
    for i in range(system_size):
        for j in range(system_size):
            for k in range(system_size):
                base_position = np.array([i, j, k])
                cart_position = np.inner(cell_basis.T, base_position)
                for atom in fcc_basis:
                    position.append(rotation_x(cart_position + atom,np.pi/4))


    fdata = open('temp_datatemp_0.dat', 'w')
    fdata.write('Crystalline Cu atoms\n\n')
    fdata.write('{} atoms\n'.format((len(position))))
    fdata.write('{} atom types\n'.format(1))
    fdata.write('{} {} xlo xhi\n'.format(0.0, system_size * lattice_parameter))
    fdata.write('{} {} ylo yhi\n'.format(0.0, system_size * lattice_parameter))
    fdata.write('{} {} zlo zhi\n\n'.format(0.0, system_size * lattice_parameter))
    fdata.write('\n')
    fdata.write('Atoms\n\n')
    for i, pos in enumerate(position):
        fdata.write('{} 1 {:.6f} {:.6f} {:.6f}\n'.format(i + 1, *pos))
    fdata.close()
