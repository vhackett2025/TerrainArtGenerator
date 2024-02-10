import math

def get_file_name_from_noise_values(temperature: float, humidity: float):
    return "textures/groundTileSet/" + str(math.floor(humidity * 2.99)) + "_" + str(math.floor(temperature * 3.99)) + ".png"
    
