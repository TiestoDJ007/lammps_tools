import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d

# make up data points
np.random.seed(1234)
points = np.random.rand(15,2)

# add 4 distant dummy points
points = np.append(points, [[9,9], [-9,9], [9,-9], [-9,-9]], axis = 0)

# compute Voronoi tesselation
vor = Voronoi(points)

# plot
voronoi_plot_2d(vor)

# colorize
#plt.figure(figsize=(4,4))
for region in vor.regions:
    if not -1 in region:
        polygon = [vor.vertices[i] for i in region]
        plt.fill(*zip(*polygon))

# fix the range of axes
plt.axis('equal')
plt.xlim([-5,5]), plt.ylim([-5,5])


plt.show()