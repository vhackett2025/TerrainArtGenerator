import math

def get_file_name_from_noise_values(humidity: float, temperature: float):
    
    # make sure parameters are <0 and >1
    
    if humidity < 0:
        humidity = 0
    elif humidity > 1:
        humidity = 1
        
    if temperature < 0:
        temperature = 0
    elif temperature > 1:
        temperature = 1
    
    return "textures/groundTileSet/" + str(math.floor(humidity * 2.99)) + "_" + str(math.floor(temperature * 3.99)) + ".png"
    
