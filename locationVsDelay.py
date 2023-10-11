import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import sklearn
import geopandas as gpd
import geoplot as gplt
import geoplot.crs as gcrs
import matplotlib.pyplot as plt
import os
from shapely.geometry import Point, Polygon

# Set SHAPE_RESTORE_SHX environment variable to YES
os.environ['SHAPE_RESTORE_SHX'] = 'YES'

# Load the shapefile for world countries
world = gpd.read_file("./data/ne_110m_admin_0_countries.shp")
flights = pd.read_csv("./data/flights.csv")
airports = pd.read_csv("./data/airports.csv", index_col="Orig")

pd.set_option('display.max_columns', None)
airports["MedianArrDelay"] = flights.groupby('Origin')['ArrDelay'].median()
airports.dropna(subset=['MedianArrDelay'], inplace=True)
sorted_airports = airports.sort_values(by='TotalSeats', ascending=False)

geometry=[Point(xy) for xy in zip(sorted_airports["Airport1Longitude"], sorted_airports["Airport1Latitude"])]
crs={'init':'epsg:4326'}
geodata = gpd.GeoDataFrame(sorted_airports,crs=crs, geometry=geometry)

# Plot TotalSeats on the map
ax = gplt.polyplot(world, projection=gcrs.PlateCarree(), figsize=(15, 10))
gplt.pointplot(geodata,
               ax=ax,
               hue='MedianArrDelay',
               legend=True,
               legend_var='hue',
               scale='TotalSeats',
               limits=(5, 100))
              #  legend_kwargs={'frameon': False}

# for x, y, label in zip(geodata.geometry.x, geodata.geometry.y, geodata.index):
#     plt.text(x, y, label, fontsize=8, ha='right')
    
plt.show()
