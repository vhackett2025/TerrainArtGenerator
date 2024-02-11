import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk, ImageEnhance

import random

from texture_map_handler import *
from MapGeneration import *

print(tk.TkVersion)

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
    slider.pack(side= tk.TOP, anchor="w", padx=5)
    return var
            
def update_canvas_widget(canvas: tk.Canvas, parameter_maps: dict, climate_variables):
    
    for x in range(32):
        for y in range(32):
            
            tileset = "textures/groundTileSet/"
            if random.randrange(100) in range(math.ceil(int(climate_variables['tree_density'].get())/1.5)):
                tileset = "textures/decalTileSet/"
                
            # check for water
            if parameter_maps['height'][x][y] < (int(climate_variables['sea_level'].get())/222):
                texture_filepath = "textures/waterTileSet/1.png"
            else:
                texture_filepath = tileset + get_file_name_from_noise_values(parameter_maps['humidity'][x][y], parameter_maps['temperature'][x][y])
            img = Image.open(texture_filepath)
            img_enhancer = ImageEnhance.Brightness(img)
            img = img_enhancer.enhance((parameter_maps['height'][x][y] + 0.5))
            img = img.resize((16,16))
            
            image_cache[(x, y)] = ImageTk.PhotoImage(img)
            canvas.create_image(x * 16, y * 16, image=image_cache[(x, y)])
            
def main():
    
    # Setup window + root
    root = tk.Tk()
    root.title('Terrain Art Generator')
    root.geometry("900x600")
    
    # Vertical UI seperator line
    
    separator = ttk.Separator(root, orient='vertical')
    separator.place(relx=0.33, rely=0, relwidth=1, relheight=1)

    # Big Parameter Label
    parameter_label = tk.Label(root, text = "Parameters")
    parameter_label.config(font =FONT_XL)
    parameter_label.pack(side= tk.TOP, anchor="w", padx=5, pady=5)
    
    # Parameter Sliders
    climate_variables = {
        'height_extremeness' : generate_parameter_slider(root, "Height Extremeness:"),
        'temperature' : generate_parameter_slider(root, "Temperature:"),
        'humidity' : generate_parameter_slider(root, "Humidity:"),
        'sea_level' : generate_parameter_slider(root, "Sea Level:"),
        'tree_density' : generate_parameter_slider(root, "Tree Density:"),
        'octaves' : generate_parameter_slider(root, "Detail:")
    }
    
    lambda_update_canvas_widget = lambda: update_canvas_widget(canvas, parameter_maps={
        'height' : generateTerrain(math.ceil(int(climate_variables['octaves'].get()) / 3.33), int(climate_variables['height_extremeness'].get())),
        'temperature' : generateTerrain(math.ceil(int(climate_variables['octaves'].get()) / 3.33), int(climate_variables['temperature'].get())),
        'humidity' : generateTerrain(math.ceil(int(climate_variables['octaves'].get()) / 3.33), int(climate_variables['humidity'].get()))
        }, climate_variables = climate_variables)
    
    # Default canvas
    canvas = tk.Canvas(root, width= 512, height=512)
    canvas.place(relx=0.34, rely=0.01)

    # "Generate" button
    generate_button = tk.Button(root, text='Generate!', width=25, command=lambda_update_canvas_widget)
    generate_button.config(font =FONT_LARGE)
    generate_button.pack(side= tk.BOTTOM, anchor="w", padx=5, pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
