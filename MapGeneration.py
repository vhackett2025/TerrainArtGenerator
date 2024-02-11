import matplotlib.pyplot as plt
import random 
from perlin_noise import PerlinNoise

def generateTerrain(slider_value, showPlot):
    size=256

    #size is the square dimentions
    #octaves = thing we change!
    #seed is randomness its just random :P
    noise = PerlinNoise(octaves=15, seed=random.randrange(0,100))

    #go through each pixel choiceing moist/temp value and depending on the two, choice what biome it is(4 for now will work) and then (for now) choice a color for each biome and go through each pixel again and assigning ect ect
    pixels = []
    for i in range(size):
        row = []
        for j in range(size):
            value=noise([i/size, j/size]) 
            
            row.append(value+0.5)
        pixels.append(row)
    
    if (showPlot):
        plt.imshow(pixels, cmap='gray')
        plt.grid(False);plt.axis('off')
        plt.show()
    return pixels 
    #plt.imshow(pixels, cmap='gray')
    #plt.grid(False);plt.axis('off')
    #plt.show()
#generateTerrain(size,3)