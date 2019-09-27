import datetime

starttime = datetime.datetime.now()
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import lognorm as lognorm
from scipy.spatial import Voronoi, voronoi_plot_2d


def regions_points_function(voro_data):
    regions_currect = []
    for i in range(len(voro_data.regions)):
        region = voro_data.regions[i]
        if region:
            if -1 not in region:
                regions_currect.append(region)
    regions_points = []
    for i_regions in range(len(regions_currect)):
        vertex_points = np.zeros((len(regions_currect[i_regions]), 2))
        for i_points in range(len(regions_currect[i_regions])):
            vertex_points[i_points] = voro_data.vertices[regions_currect[i_regions][i_points]]
        regions_points.append(vertex_points)
    return np.array(regions_points)


def Polygon_Area(points):
    vectors = []
    for i_point in range(len(points)):
        if i_point != 0:
            vectors.append(points[i_point] - points[0])
    area = 0
    for i_vector in range(len(vectors) - 1):
        area += np.abs(0.5 * np.cross(vectors[i_vector], vectors[i_vector + 1]))
    return area


def regions_area_function(regions_points):
    region_area = []
    for vertexes in regions_points:
        area = Polygon_Area(vertexes)
        region_area.append(area)
    return np.array(region_area)


def Normaliztion(area_array):
    val_internal = 0.05  # 已经将数据的x轴标准化，所以将0~1之间分割为20个间隙
    area_sort_val = area_array[np.argsort(area_array)]
    array_size_0 = np.size(area_sort_val, 0)
    array_median = np.array((int(array_size_0 / 2), area_sort_val[int(array_size_0 / 2)]))
    scale_x_val = 1 / array_median[1]
    scale_y_val = np.divide(1, np.multiply(len(area_array), val_internal))
    array_scale = area_sort_val * scale_x_val
    # 首先实验不去除过大值
    area_distribution = []
    for i_val in range(len(array_scale)):
        min = i_val * val_internal
        max = min + val_internal
        middle = min + 0.5 * val_internal
        index_val = np.where((max > array_scale) & (min < array_scale))[0]
        area_distribution.append(np.array((middle, np.multiply(np.size(index_val), scale_y_val))))
    return np.array(area_distribution)


def Penalty_Function(area_distribution, sigma):
    chi_square = 0
    delta = area_distribution[1][0] - area_distribution[0][0]
    n_total = len(area_distribution)
    for i_k in range(n_total):
        chi_square += np.square(
            (lognorm.pdf(area_distribution[i_k][0], sigma) - np.multiply(delta, area_distribution[i_k][1])))
    return np.divide(chi_square, n_total)


def Random_Walk(point_array):
    walk_size = np.random.rand(1, 2) * 2 - 1
    return np.add(point_array, walk_size)


def Scale_Function(Chi_square):
    return np.exp(-(np.divide(np.sqrt(Chi_square), 0.3)))


points_number = 500
if __name__ == '__main__':
    np.random.seed(1234)
    sigma = 0.3
    chi_limited = 0.01
    step_limited = 10
    step_current = 0
    points = np.random.rand(points_number, 2) * 50
    voro = Voronoi(points)
    regions_points = regions_points_function(voro)
    regions_area = regions_area_function(regions_points)
    region_normalization = Normaliztion(regions_area)
    chi_square = Penalty_Function(region_normalization, sigma)
    points_len = points.shape[0]
    new_points = points
    new_points[0] = Random_Walk(new_points[0])
    for i_step in range(step_limited):
        new_voro = Voronoi(new_points)
        new_region_points = regions_points_function(new_voro)
        new_region_area = regions_area_function(new_region_points)
        new_region_normalization = Normaliztion(new_region_area)
        new_chi_squre = Penalty_Function(new_region_normalization, sigma)
        if (new_chi_squre < chi_limited)or(chi_square < chi_limited):
            best_point = points
            break
        # elif (new_chi_squre <= chi_square)&(new_chi_squre>=chi_limited):
        #    new_points[i_step] = Random_Walk(new_points[i_step])
        #    continue
        # elif new_chi_squre>chi_square:
        #    rho = np.random.rand()
        #    if Scale_Function(new_chi_squre) < rho:
        #        new_points[i_step] = Random_Walk(new_points[i_step])
        #        continue
        #    else:
        #        continue
        # else:
        #    continue
    # voronoi_plot_2d(voro)
    # plt.hist(region_area, bins=200, range=(0, 20))
    # plt.title("histogram")
    # plt.show()
endtime = datetime.datetime.now()
print(endtime - starttime)
