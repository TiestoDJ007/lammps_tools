#!/usr/bin/env python
# -*- coding=utf-8 -*-
import numpy as np

if __name__ == "__main__":
    file = open('/mnt/d/Tools/lammps_tools/grain_boundary_(430)_primitive_cell.dat', 'r')
    size_data = file.readlines()[4:7]
    cell_basis = np.array([[size_data[0].split()[1], 0, 0],
                           [0, size_data[1].split()[1], 0],
                           [0, 0, size_data[2].split()[1]]])

    initial_data = np.loadtxt('/mnt/d/Tools/lammps_tools/grain_boundary_(430)_primitive_cell.dat', skiprows=10)
    atom_basis = initial_data[:, 2:]

