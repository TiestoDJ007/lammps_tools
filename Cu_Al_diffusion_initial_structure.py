#!/usr/bin/env python
# -*- coding=utf-8 -*-

import numpy as np

if __name__ == "__main__":
    Cu_lattice_constant = 3.6149
    Al_lattice_constant = 4.0495
    cell_basis = np.array([[1, 0, 0],
                          [0, 1, 0],
                          [0, 0, 1]])
    atom_basis = np.array([[0, 0, 0],
                           [0.5, 0.5, 0],
                           [0.5, 0, 0.5],
                           [0, 0.5, 0.5]])