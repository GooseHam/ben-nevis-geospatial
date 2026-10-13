import geopandas as gpd
import matplotlib.pyplot as plt

countries = gpd.read_file("ne_110m_admin_0_countries")
cities = gpd.read_file("ne_110m_populated_places")

cities_small = cities[["FEATURECLA", "NAME", "POP_MAX", "SOV0NAME", "geometry"]]

megacities = cities_small[cities_small["POP_MAX"] > 1000000]

ax = countries.plot(color="lightgrey")
megacities.plot(ax=ax, column = "POP_MAX", legend=True, cmap = "viridis")

plt.show()