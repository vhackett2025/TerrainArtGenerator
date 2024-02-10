import math

def get_texture_coords_from_noise_values(temperature: float, humidity: float):
    return (
        int(math.floor(temperature * 3.99)) * 8,
        int(math.floor(humidity * 2.99)) * 8
    )
