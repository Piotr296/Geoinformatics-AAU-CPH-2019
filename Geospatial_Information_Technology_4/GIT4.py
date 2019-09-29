# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 23:42:48 2019

@author: Petronium
"""

import geopandas as gpd 
import pandas as pd
import os
import shapely.speedups


# Let's enable speedups to make queries faster

shapely.speedups.enable()


# Working directory

cwd = os.chdir("Assignment\CPH_data")


# File paths
road_fp = 'roads_cph.shp'
railway_fp = 'railways_cph.shp'
points_fp = 'points_cph.shp'
buildings_fp = 'buildings_cph.shp'


# Import files

roads_network = gpd.read_file(road_fp)
railways = gpd.read_file(railway_fp)
points_cph = gpd.read_file(points_fp)


# Checking coordinate systems

assert roads_network.crs == railways.crs == points_cph.crs, "CRS differs between layers!"
if roads_network.crs == railways.crs == points_cph.crs:
    print('Yeah! CRS are correct')
    
    
# Making buffers
    
roads_network_buffer = roads_network.buffer(20)
railways_buffer = railways.buffer(50)
points_cph_buffer = points_cph.buffer(30)


# Merging

noise_map = gpd.GeoDataFrame(geometry = pd.concat([roads_network_buffer, railways_buffer, points_cph_buffer], 
                        ignore_index=True), crs=roads_network.crs)
noise_map_union = noise_map.unary_union
noise_map_gdf = gpd.GeoDataFrame(crs=roads_network.crs, geometry=[noise_map_union])
noise_map_gdf.to_file('noise_map_gdf.shp')


# Import buildings

buildings = gpd.read_file(buildings_fp)


# Checking and saving the files

noisy_buildings = buildings[buildings.within(noise_map_gdf.loc[0, 'geometry'])]
noisy_buildings.to_file('noise_buildings.shp')

quiet_buildings = pd.concat([noisy_buildings,buildings]).drop_duplicates(keep=False)
quiet_buildings.to_file('quiet_buildings.shp')