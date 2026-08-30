import matplotlib.pyplot as plt
import rasterio
import osmnx as ox
import numpy as np

dataset = rasterio.open("NN17.asc")
elevation = dataset.read(1)

def hillshade(array, azimuth=315, angle_altitude=45):
    x, y = np.gradient(array)
    slope = np.pi/2. - np.arctan(np.sqrt(x*x + y*y))
    aspect = np.arctan2(-x, y)
    azimuthrad = (360.0 - azimuth) * np.pi / 180.
    altituderad = angle_altitude * np.pi / 180.

    shaded = np.sin(altituderad) * np.sin(slope) \
        + np.cos(altituderad) * np.cos(slope) \
        * np.cos((azimuthrad - np.pi/2.) - aspect)

    return 255 * (shaded + 1) / 2


hs = hillshade(elevation)

bn_roads = ox.graph_from_point((56.7969, -5.0036), dist=9000, network_type='all', simplify=True, retain_all=False, truncate_by_edge=False,custom_filter=None)
edges = ox.graph_to_gdfs(bn_roads, nodes=False, edges=True)
edges_bng = edges.to_crs(epsg=27700)

fig, ax = plt.subplots()
ax.imshow(hs, cmap="gray", extent=[dataset.bounds.left, dataset.bounds.right, dataset.bounds.bottom, dataset.bounds.top])
edges_bng.plot(ax=ax, color="red", linewidth=1)

ax.set_xlim(dataset.bounds.left, dataset.bounds.right)
ax.set_ylim(dataset.bounds.bottom, dataset.bounds.top)
ax.set_aspect("equal")

plt.savefig("ben_nevis_map.png", dpi=150)
plt.show()