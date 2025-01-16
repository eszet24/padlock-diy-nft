import math
import numpy as np
import random as rnd
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageOps

# Design variables
tile_number = 9                       # Will be adjusted to lower square number (1=big, 4=medium, 9=small size)
frame_number = 12                     # Must be any number between 1 and 12
frame_line_width = 3

# frame_object = Image.open('/Downloads/DIT_NFT_Logo.png')   
frame_object = None                

tiles_per_row = math.floor(math.sqrt(tile_number))  # Calculate next smaller squared layout
tiles_per_column = tiles_per_row                    # Only squared wallpapers

# Create a basic tile image using Pillow
tile_size = (400, 400)
tile = Image.new("RGB", tile_size, "red")      # Initially a false color

# Design wallpaper by inner pattrern
def assemble_wallpaper(tile, rows=tiles_per_row, cols=tiles_per_column):  
    
    tile = Image.new("RGB", (tile_size[0] * cols, tile_size[1] * rows), "skyblue")

    for i in range(rows):
        for j in range(cols):
  
            # Patterm dimensions
            width, height = 300, 300             # Pattern square room
            nested_depth = frame_number          # Number of nested squares
            distance = 10                        # Distance between squares

            # Sizing of square pattern
            width, height = 360, 360
            pattern = Image.new('RGB', (width, height), 'skyblue')
            draw = ImageDraw.Draw(pattern)

            # Drawing nested rectangles
            for x in range(nested_depth):

                # Position and size of outer rectangle
                if x == 0:
                    start_x, start_y = distance, distance
                    rect_width = 340
                    rect_height = 340

                # Defining random RGB color per square
                red_value = round(rnd.random()*255)
                green_value = round(rnd.random()*255)
                blue_value = round(rnd.random()*255)
                random_color = (red_value, green_value, blue_value)
        
                # Draw frame
                draw.rectangle(
                    [start_x, start_y, start_x + rect_width, start_y + rect_height], 
                    outline=(random_color),
                    width=frame_line_width)
    
                # Adjust position an size for next smaller square
                start_x += distance
                start_y += distance
                rect_width -= 2 * distance
                rect_height -= 2 * distance

                # Fit in frame content
                if x == nested_depth:
                    pattern.paste(frame_object)
                    draw = ImageDraw.Draw(pattern)
            
            tile.paste(pattern, (j * tile_size[0] + (2*distance), i * tile_size[1] + (2*distance)))  
            draw = ImageDraw.Draw(tile)

    return tile

# Generate and display wallpaper pattern
wallpaper = assemble_wallpaper(tile)
plt.imshow(wallpaper)
plt.axis("off")
plt.show()