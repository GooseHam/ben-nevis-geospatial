import rasterio
import matplotlib.pyplot as plt
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

plt.imshow(hs, cmap="gray")
plt.show()