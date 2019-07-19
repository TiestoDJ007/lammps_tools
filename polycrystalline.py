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
    point_number = 30
    point_cartesian = rand(point_number, 3) * 100
    # 生成初始点
    point_cartesian[:, 0] = point_cartesian[:, 0]
    point_cartesian[:, 1] = point_cartesian[:, 1]
    point_cartesian[:, 2] = point_cartesian[:, 2]
    # 生成初始Voronoi图
    initial_vor = Voronoi(point_cartesian)
    indices = initial_vor.ridge_points.tolist()
    # 画出三维维诺图 不填充
    plot_data=[]
    for index in indices:
        x_data = [initial_vor.vertices[index[0]][0], initial_vor.vertices[index[1]][0]]
        y_data = [initial_vor.vertices[index[0]][1], initial_vor.vertices[index[1]][1]]
        z_data = [initial_vor.vertices[index[0]][2], initial_vor.vertices[index[1]][2]]
        plot_data.append(go.Scatter3d(x=x_data,y=y_data,z=z_data,mode='lines'))

    layout = go.Layout(
        width=800,
        height=700,
        autosize=False,
        title='Volcano dataset',
        scene=dict(
            xaxis=dict(
                gridcolor='rgb(255, 255, 255)',
                zerolinecolor='rgb(255, 255, 255)',
                showbackground=True,
                backgroundcolor='rgb(230, 230,230)',
                #autorange=True
                range=[0, 100]
            ),
            yaxis=dict(
                gridcolor='rgb(255, 255, 255)',
                zerolinecolor='rgb(255, 255, 255)',
                showbackground=True,
                backgroundcolor='rgb(230, 230,230)',
                #autorange=True
                range=[0, 100]
            ),
            zaxis=dict(
                gridcolor='rgb(255, 255, 255)',
                zerolinecolor='rgb(255, 255, 255)',
                showbackground=True,
                backgroundcolor='rgb(230, 230,230)',
                #autorange=True
                range=[0, 100]
            ),
            aspectratio=dict(x=1, y=1, z=1),
            aspectmode='manual'
        )
    )
    fig = dict(data=plot_data,layout=layout)
    plotly.offline.plot(fig, filename='/mnt/d/voronoi.html')

