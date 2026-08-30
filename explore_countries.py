import geopandas as gpd
import matplotlib.pyplot as plt
countries = gpd.read_file("ne_110m_admin_0_countries")

countries_small = countries[["NAME", "POP_EST", "CONTINENT", "geometry"]]

countries_small["pop_millions"] = countries_small["POP_EST"] / 1000000

africa = countries_small[countries_small["CONTINENT"] == "Africa"]
asia = countries_small[countries_small["CONTINENT"] == "Asia"]

is_europe = countries_small["CONTINENT"] == "Europe"
is_large = countries_small["POP_EST"] > 30000000

euro_large = countries_small[is_europe & is_large]

countries_small.plot(column = "CONTINENT", legend=True, cmap = "viridis")
plt.show()