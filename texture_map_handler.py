import math

def get_file_name_from_noise_values(temperature: float, humidity: float):
    return "ground_texture_" + (math.floor(temperature * 3.99) * 8) + "_" + (math.floor(humidity * 2.99) * 8) + ".png"
    
