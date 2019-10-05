# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 15:30:36 2019

@author: Petronium

It was necessary to create a function which will partly open the raster and
transfer slice to the list because of the memory issue
"""

import rasterio
import numpy as np
import matplotlib.pyplot as plt
from rasterio.windows import Window

# Filepath
fp = r"Data_Corine\CLC2018_CLC2012_V2018_20.tif"

# Opening a file
raster = rasterio.open(fp)

# Functions
def saving_metadata(some_raster):
    """
    A function that print and save metada from the raster
    
    Args:
        some_raster (raster): raster to read metadata from
        
    Return:
        .txt file
    """
    
    with open('metadata.txt', 'w') as f:
        for k, v in some_raster.meta.items():
            meta = '{} : {} \n'.format(k,v)
            print(meta)
            f.write(meta)


def slicing_raster(some_raster, col_row=2):
    """
    A function that divides the raster into smaller equal parts
    
    Args:
        some_raster (raster): raster to divide
        col_row (int): number of columns and rows
    Returns:
        The list of numpy arrays
    """
    width = some_raster.width
    height = some_raster.height
    col_width = width/col_row
    row_height = height/col_row
    
    # Create list of offset widths
    offset_of_width = np.linspace(0, width, col_row+1)
    list_offset_width = list(offset_of_width)[:-1]
    final_width_offset_list = []
    for i in range(0, col_row):
        for j in list_offset_width:
            final_width_offset_list.append(j)
    
    # Create list of offset heights
    offset_of_height = np.linspace(0, height, col_row+1)
    list_offset_height = list(offset_of_height)[:-1]
    final_height_offset_list = [val for val in list_offset_height for _ in range(col_row)]
    
    # Create a slices
    list_of_slices = []
    for i in range(0, col_row*col_row):
        raster_slice = Window(final_width_offset_list[i], final_height_offset_list[i], col_width, row_height)
        list_of_slices.append(some_raster.read(1, window=raster_slice))    

    return list_of_slices


# Creating a chart from one slice
saving_metadata(raster)  

raster_sliced = slicing_raster(raster)

plt.figure(figsize=(6,6))
plt.imshow(raster_sliced[0], cmap='Reds')
plt.title("Corine Map by Piotr Michalak")
plt.xticks([])
plt.yticks([])
plt.savefig('Map.png')
plt.show()