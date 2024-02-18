import tkinter as tk
from tkinter import ttk, IntVar, Checkbutton
from PIL import Image, ImageTk, ImageEnhance

import os

import random
from pygame import mixer

from texture_map_handler import *
from MapGeneration import *
from heightGeneration import *

SIZE = 64
TILE_SIZE = 8

ROOT = os.path.dirname(os.path.abspath(__file__))

SCREEN_DIMENTIONS = "756x512"



FONT_XL = ("Courier ", 14, "bold", 'underline')
FONT_LARGE = ("Courier ", 14)
FONT_MEDIUM = ("Courier", 12)
FONT_SMALL = ("Courier", 10)

image_cache = {}

# Creates a label and slider for a specified parameter, returns the slider's variable
def generate_parameter_slider(root, label_name: str):
    
    var=tk.StringVar()
    label = tk.Label(root, text = label_name)
    label.config(font = FONT_MEDIUM)
    label.pack(side= tk.TOP, anchor="w", padx=5, pady = (10, 0))
    slider = tk.Scale(root, variable=var, from_=1, to=100, orient=tk.HORIZONTAL, sliderlength=20, length=270)
    slider.set(50)
    slider.pack(side= tk.TOP, anchor="w", padx=10)
    return var
            
def update_canvas_widget(canvas: tk.Canvas, parameter_maps: dict, climate_variables):
    
    # Set loading screen
    loading_screen_img = Image.open(os.path.dirname(os.path.abspath(__file__))+"\loading_screen.png")
    image_cache[(-1, -1)] = ImageTk.PhotoImage(loading_screen_img)
    canvas.create_image(257, 257, image=image_cache[(-1, -1)])
    canvas.update_idletasks()
    
    for x in range(SIZE):
        for y in range(SIZE):
            
            tileset =  ROOT+"/textures/groundTileSet/"
            if random.randrange(100) in range(math.ceil(int(climate_variables['tree_density'].get())/1.5)):
                tileset =  ROOT+"/textures/decalTileSet/"
                
            # check for water
            if parameter_maps['height'][x][y] < (int(climate_variables['sea_level'].get())/222):
                texture_filepath =  ROOT+"/textures/waterTileSet/0.png"
                if parameter_maps['temperature'][x][y] < 0.25:
                    texture_filepath = ROOT+"/textures/groundTileSet/1_0.png"
            else:
                texture_filepath = tileset + get_file_name_from_noise_values(parameter_maps['humidity'][x][y], parameter_maps['temperature'][x][y] * 1.2)
                
            img = Image.open(texture_filepath)
            
            
            #vivi changes 
            #img_enhancer = ImageEnhance.Brightness(img)
            
            #if "water" not in texture_filepath:
            #    img = img_enhancer.enhance(((parameter_maps['height'][x][y] - 0.5) * (int(climate_variables['height_extremeness'].get())/50) + 1))
            img = img.resize((16,16))
            
            if "ground" in texture_filepath:
                
                img = img.rotate(90 * random.randrange(4), expand=1)
            #show main thingy
            image_cache[(x, y)] = ImageTk.PhotoImage(img)
            canvas.create_image(x * TILE_SIZE, y * TILE_SIZE, image=image_cache[(x, y)])
            
    #show height
    generateHeight(math.ceil(int(climate_variables['octaves'].get()) / 3.33), math.ceil(int(climate_variables['height_extremeness'].get())))
    heightMap = Image.open(ROOT+"/tempHeightNew.png")
    
   # heightMap=heightMap.resize((2,2))
    
    image_cache[(-1, -1)] = ImageTk.PhotoImage(heightMap)
    canvas.create_image(257, 257, image=image_cache[(-1, -1)])
    #canvas.update_idletasks()
            
    mixer.init()
    mixer.music.load(ROOT+"\ding.mp3")
    mixer.music.set_volume(0.7)
    mixer.music.play()
            
def main():
    
    # Setup window + root
    root = tk.Tk()
    root.title('Terrain Art Generator')
    root.geometry("900x600")
    root.iconbitmap(os.path.dirname(os.path.abspath(__file__))+"\icon.ico")
    
    # Vertical UI seperator line
    
    separator = ttk.Separator(root, orient='vertical')
    separator.place(x=300, rely=0, relwidth=1, relheight=1)

    # Big Parameter Label
    parameter_label = tk.Label(root, text = "Parameters")
    parameter_label.config(font =FONT_XL)
    parameter_label.pack(side= tk.TOP, anchor="w", padx=5, pady=5)
    
    # Parameter Sliders
    climate_variables = {
        'temperature' : generate_parameter_slider(root, "Temperature:"),
        'humidity' : generate_parameter_slider(root, "Humidity:"),
        'sea_level' : generate_parameter_slider(root, "Sea Level:"),
        'octaves' : generate_parameter_slider(root, "Detail:"),
        'height_extremeness' : generate_parameter_slider(root, "Height Extremeness:"),
        'tree_density' : generate_parameter_slider(root, "Tree Density:"),
    }
    
    lambda_update_canvas_widget = lambda: update_canvas_widget(canvas, parameter_maps={
        'height' : generateTerrain(math.ceil(int(climate_variables['octaves'].get()) / 3.33), 50),
        'temperature' : generateTerrain(math.ceil(int(climate_variables['octaves'].get()) / 3.33), int(climate_variables['temperature'].get())),
        'humidity' : generateTerrain(math.ceil(int(climate_variables['octaves'].get()) / 3.33), int(climate_variables['humidity'].get()))
        }, climate_variables = climate_variables)
    
    # Default canvas
    canvas = tk.Canvas(root, width= 510, height=510)
    canvas.place(x=500, rely=0.12)
    canvas.configure(bg='grey12')

    # "Generate" button
    generate_button = tk.Button(root, text='Generate!', width=25, command=lambda_update_canvas_widget)
    generate_button.config(font =FONT_LARGE, bg="grey50", fg="white")
    generate_button.pack(side= tk.BOTTOM, anchor="w", padx=5, pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
