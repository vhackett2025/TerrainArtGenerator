import matplotlib.pyplot as plt
import random 
from perlin_noise import PerlinNoise
size=16

moisture = 8

tempature = 8

def generateTerrain(size,moisture,tempature):


    #size is the square dimentions
    #octaves = thing we change!
    #seed is randomness its just random :P
    moistNoise = PerlinNoise(octaves=moisture, seed=random.randrange(0,100))
    tempNoise = PerlinNoise(octaves=tempature, seed=random.randrange(0,100))

    #moistPic = [[moistNoise([i/size, j/size]) for j in range(size)] for i in range(size)]
    #moistPic = [[tempNoise([i/size, j/size]) for j in range(size)] for i in range(size)]
    #go through each pixel choiceing moist/temp value and depending on the two, choice what biome it is(4 for now will work) and then (for now) choice a color for each biome and go through each pixel again and assigning ect ect
    pic = []
    for i in range(size):
        row = []
        for j in range(size):
            moistVal=moistNoise([i/size, j/size])
            tempVal=tempNoise([i/size, j/size])
            
            if (moistVal>0) and (tempVal>0):
                if (moistVal>0.01) and (tempVal>0.01):
                    noiseVal=2
                else:
                    noiseVal=1
            else:
                noiseVal=0.89
            #noiseVal=0
            #noiseVal += moistNoise([i/size, j/size])
            #noiseVal += moistNoise([i/size, j/size])
            #print(moistVal)
            #print(tempVal)
            row.append(noiseVal)
        pic.append(row)
        
        
    plt.imshow(pic, cmap='gray')

    plt.grid(False);plt.axis('off')

    plt.show()
    print(pic)

generateTerrain(size,moisture,tempature)