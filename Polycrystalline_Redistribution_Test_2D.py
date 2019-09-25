import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import lognorm as lognorm
from scipy.spatial import Voronoi, voronoi_plot_2d


def Polygon_Area(points):
    vectors = []
    for i_point in range(len(points)):
        if i_point != 0:
            vectors.append(points[i_point] - points[0])
    area = 0
    for i_vector in range(len(vectors) - 1):
        area += np.abs(0.5 * np.cross(vectors[i_vector], vectors[i_vector + 1]))
    return area


def Normaliztion(area_array):
    val_internal = 0.05  # 已经将数据的x轴标准化，所以将0~1之间分割为20个间隙
    area_sort_val = area_array[np.argsort(area_array)]
    array_size_0 = np.size(area_sort_val, 0)
    array_median = np.array((int(array_size_0 / 2), area_sort_val[int(array_size_0 / 2)]))
    scale_x_val = 1 / array_median[1]
    scale_y_val = np.divide(1, np.multiply(488, val_internal))
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
        chi_square += np.square((lognorm.pdf(area_distribution[i_k][0],sigma)-np.multiply(delta,area_distribution[i_k][1])))
    return np.divide(chi_square,n_total)


points_number = 500
if __name__ == '__main__':
    seed = np.random.seed(1234)
    points = np.random.rand(points_number, 2) * 50
    voro = Voronoi(points)
    regions_currect = []
    for i in range(len(voro.regions)):
        region = voro.regions[i]
        if region:
            if -1 not in region:
                regions_currect.append(region)
    regions_points = []
    for i_regions in range(len(regions_currect)):
        vertex_points = np.zeros((len(regions_currect[i_regions]), 2))
        for i_points in range(len(regions_currect[i_regions])):
            vertex_points[i_points] = voro.vertices[regions_currect[i_regions][i_points]]
        regions_points.append(vertex_points)
    region_area = []
    for vertexes in regions_points:
        area = Polygon_Area(vertexes)
        region_area.append(area)
    region_area = np.array(region_area)
    ######拟合部分########

    # voronoi_plot_2d(voro)
    plt.hist(region_area, bins=200, range=(0, 20))
    plt.title("histogram")
    plt.show()
