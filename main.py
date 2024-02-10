import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

from texture_map_handler import *
from MapGeneration import *

SCREEN_DIMENTIONS = "756x512"

FONT_XL = ("Courier ", 14, "bold", 'underline')
FONT_LARGE = ("Courier ", 14)
FONT_MEDIUM = ("Courier", 12)
FONT_SMALL = ("Courier", 10)

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

def update_canvas_widget(root, canvas: tk.Canvas, size: int, tile_size: int, parameter_maps: dict, wetness: float):
    canvas.pack_forget()
    for y in range(size):
        for x in range(size):
            texture_name = get_file_name_from_noise_values(parameter_maps['temperature'][x][y], parameter_maps['humidity'][x][y])
            canvas.create_image(x * tile_size, y * tile_size, image=ImageTk.PhotoImage(file=texture_name), anchor="center")
            
    canvas.place(relx=0.34, rely=0)

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
        'wetness' : generate_parameter_slider(root, "Wetness:"),
    }
    
    lambda_update_canvas_widget = lambda: update_canvas_widget(root, canvas, size=10, tile_size=8, parameter_maps={
        'height' : generateTerrain(int(climate_variables['height_extremeness'].get()) / 10),
        'temperature' : generateTerrain(int(climate_variables['temperature'].get()) / 10),
        'humidity' : generateTerrain(int(climate_variables['humidity'].get()) / 10)
        }, wetness=int(climate_variables['wetness'].get()))
    
    # Default canvas
    canvas = tk.Canvas(root, width= 100, height=100)
    canvas.place(relx=0.34, rely=0)

    # "Generate" button
    generate_button = tk.Button(root, text='Generate!', width=25, command=lambda_update_canvas_widget)
    generate_button.config(font =FONT_LARGE)
    generate_button.pack(side= tk.BOTTOM, anchor="w", padx=5, pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
