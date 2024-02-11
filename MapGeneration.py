import matplotlib.pyplot as plt
import random 
from perlin_noise import PerlinNoise

def generateTerrain(octaveVal,offsetVal,showPlot = False):
    size=256

    #size is the square dimentions
    #octaves = thing we change!
    #seed is randomness its just random :P
    noise = PerlinNoise(octaves=octaveVal, seed=random.randrange(0,100))

    #go through each pixel choiceing moist/temp value and depending on the two, choice what biome it is(4 for now will work) and then (for now) choice a color for each biome and go through each pixel again and assigning ect ect
    pic = []
    for i in range(size):
        row = []
        for j in range(size):
            val=noise([i/size, j/size])
        
            row.append(((val+0.5)) + (offsetVal - 50)/100)
            
        pic.append(row)
    
    if (showPlot):
        plt.imshow(pic, cmap='gray')
        plt.grid(False);plt.axis('off')
        plt.show()
    return pic 
    #plt.imshow(pic, cmap='gray')
    #plt.grid(False);plt.axis('off')
    #plt.show()
