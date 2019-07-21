#!/usr/bin/env python
# -*- coding=utf-8 -*-

import numpy as np
import plotly
import plotly.graph_objects as go
from scipy.spatial import Voronoi
from numpy.random import rand

if __name__ == "__main__":
    # 输入待生成的晶体的基本参数，超胞大小，晶格常数，晶格类型
    # 超胞大小
    x_length = 100
    y_length = 100
    z_length = 100
    # 以Cu为例
    lattice_constant = 3.6150
    # 开始生成初始Voronoi 3D结构
    # 规定生成的多面体数量，同时也是输入点的数量
    np.random.seed(1234)
    point_number = 30
    point_cartesian = rand(point_number, 3) * 100
    # 生成初始点
    point_cartesian[:, 0] = point_cartesian[:, 0]
    point_cartesian[:, 1] = point_cartesian[:, 1]
    point_cartesian[:, 2] = point_cartesian[:, 2]
    # 生成初始Voronoi图
    vor = Voronoi(point_cartesian)
    # 解决维诺图上为无线延展区域
    new_region_multi = []
    new_vertice_multi = vor.vertices.tolist()
    # 取中心点
    center_point_multi = vor.points.mean(axis=0)
    # 建立所有ridge的地图,将每个区域的表面都与这个区域对应上。数据结构为字典，key为区域编号，value采用tuple.tuple中的第一个数字为与这个区域相连的区域，第二个数字为无限区域所对应的点，顺序可以组成一个封闭的凸平面。
    all_ridges = {}
    for num_point in range(0, vor.npoints):
        region_surface = []
        for num_ridge in range(len(vor.ridge_points)):
            # 判断点是否为无限
            if num_point == vor.ridge_points[num_ridge][0]:
                # 初始顺序
                vertices_initial = np.array(vor.ridge_vertices[num_ridge])
                vertices_length = len(vertices_initial)
                # 开始排列顺序
                # 判断是否为无限点
                if all(vertice_value >= 0 for vertice_value in vertices_initial):
                    vertices_array = vertices_initial
                    ridge_vertices = np.insert(np.array(vertices_array), 0, vor.ridge_points[num_ridge][1])
                    ridge_tuple = tuple(ridge_vertices)
                    region_surface.append(ridge_tuple)
                else:
                    for num_vertice in range(vertices_length):
                        if vertices_initial[num_vertice] < 0:
                            # 生成新的循序，默认无限点为第0个点
                            vertices_order = list(range(num_vertice, vertices_length)) + list(range(num_vertice))
                            vertices_array = [vertices_initial[i] for i in vertices_order]
                            ridge_vertices = np.insert(np.array(vertices_array), 0, vor.ridge_points[num_ridge][1])
                            ridge_tuple = tuple(ridge_vertices)
                            region_surface.append(ridge_tuple)
                            break
            #计算另一组数据，使区域所对应的面完整
            if num_point == vor.ridge_points[num_ridge][1]:
                vertices_initial = np.array(vor.ridge_vertices[num_ridge])
                vertices_length = len(vertices_initial)

                if all(vertice_value >= 0 for vertice_value in vertices_initial):
                    vertices_array = vertices_initial
                    ridge_vertices = np.insert(np.array(vertices_array), 0, vor.ridge_points[num_ridge][0])
                    ridge_tuple = tuple(ridge_vertices)
                    region_surface.append(ridge_tuple)
                else:
                    for num_vertice in range(vertices_length):
                        if vertices_initial[num_vertice] < 0:
                            vertices_order = list(range(num_vertice, vertices_length)) + list(range(num_vertice))
                            vertices_array = [vertices_initial[i] for i in vertices_order]
                            ridge_vertices = np.insert(np.array(vertices_array), 0, vor.ridge_points[num_ridge][0])
                            ridge_tuple = tuple(ridge_vertices)
                            region_surface.append(ridge_tuple)
                            break
            all_ridges.setdefault(num_point, region_surface)
    # 重建无限区域
    for point_0, region in enumerate(vor.point_region):
        vertice_couple = vor.regions[point_0]
        if all(vertice >= 0 for vertice in vertice_couple):
        # 判断是否为有限区域
            new_region_multi.append(vertice_couple)
            continue
    # 重新构建无限区域
        ridge_couple = all_ridges[point_0]
        new_region = [vertice for vertice in vertice_couple if vertice >= 0]

        for num_surface in range(len(ridge_couple)):
            if all(point_value >= 0 for point_value in ridge_couple[num_surface]):
                continue
        # 计算无限区域上的点
            point_1 = ridge_couple[num_surface][0]
            t = vor.points[point_1] - vor.points[point_0]
