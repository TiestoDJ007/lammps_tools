#!/usr/bin/env python
# -*- coding=utf-8 -*-
import numpy as np
from numpy import cos, sin, arctan
from matplotlib.path import Path


def rotation_z(position_array, psi):
    rotation_matrix_z = np.array([[cos(psi), -sin(psi), 0],
                                  [sin(psi), cos(psi), 0],
                                  [0, 0, 1]])
    return np.dot(position_array, rotation_matrix_z)


def isPointinPolygon(position_array, corner_list):
    return


if __name__ == "__main__":
    # 生成四个条边界
    lattice_parameter = 3.597
    direction_initial = np.array([4, 1, 0])
    points = [np.zeros(3)]
    for i in range(4):
        direction = rotation_z(direction_initial, -i * np.pi / 2)
        points.append(points[i] + direction)
    points = np.array(points, dtype=int)
    # 找到生成原胞的最小区域
    mins = np.array([min(points.min(axis=0)), min(points.min(axis=1))], dtype=int)
    maxs = np.array([max(points.max(axis=0)), max(points.max(axis=1))], dtype=int)
    # 生成原胞
    # lattice_parameter = 3.597
    cell_basis = np.array([[1, 0, 0],
                           [0, 1, 0],
                           [0, 0, 1]])
    atom_basis = np.array([[0, 0, 0],
                           [0.5, 0.5, 0],
                           [0, 0.5, 0.5],
                           [0.5, 0, 0.5]])
    position_initial = []
    for i in range((mins[0]), maxs[0], 1):
        for j in range(mins[1], maxs[1], 1):
            for k in range(1):
                base_position = np.array([i, j, k])
                cart_position = np.inner(cell_basis.T, base_position)
                for atom in atom_basis:
                    position_initial.append(cart_position + atom)

    points_2D = np.round(np.delete(points, -1, axis=1), decimals=1)
    pick = Path(points_2D)
    position = []
    for pos_nb in range(len(position_initial)):
        cart_2D = np.delete(position_initial[pos_nb], -1, axis=0)
        if pick.contains_point(cart_2D) == True:
            position.append(position_initial[pos_nb])
    position.append(points[0])
    position = np.array(position)

    inv_angle = arctan(direction_initial[1]/direction_initial[0])
    for pos_nb_inv in range(len(position)):
        position[pos_nb_inv] = np.round(rotation_z(position[pos_nb_inv], inv_angle), decimals=9)

    position_final =[]
    x_lim = max(np.array(position).max(axis=0))
    y_lim = max(np.array(position).max(axis=1))
    radius = 3
    for i_pos in range(len(position)):
        if position[i_pos][0] < x_lim  and position[i_pos][1] < y_lim :
            position_final.append(position[i_pos])
    position_final = np.array(position_final)

    fdata = open('grain_boundary_primitive_cell.dat', 'w')
    fdata.write('Crystalline Cu atoms\n\n')
    fdata.write('{} atoms\n'.format((len(position_final))))
    fdata.write('{} atom types\n'.format(1))
    fdata.write('{} {} xlo xhi\n'.format(0.0, max(position[:,0]) * lattice_parameter))
    fdata.write('{} {} ylo yhi\n'.format(0.0, max(position[:,1]) * lattice_parameter))
    fdata.write('{} {} zlo zhi\n\n'.format(0.0, 1 * lattice_parameter))
    fdata.write('\n')
    fdata.write('Atoms\n\n')
    for i, pos in enumerate(position_final):
        fdata.write('{} 1 {:.6f} {:.6f} {:.6f}\n'.format(i + 1, *pos * lattice_parameter))
    fdata.close()
