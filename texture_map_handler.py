import math
import os

def get_file_name_from_noise_values(temperature: float, humidity: float):
    return os.getcwd().replace('\\', '/') + "/textures/tileSet/" + str(math.floor(temperature * 3.99)) + "_" + str(math.floor(humidity * 2.99)) + ".png"
    
