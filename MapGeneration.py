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

    #go through each pixel choiceing moist/temp value and depending on the two, choice what biome it is(4 for now will work) and then (for now) choice a color for each biome and go through each pixel again and assigning ect ect
    pic = []
    moistLevel=0
    tempLevel=0
    for i in range(size):
        row = []
        for j in range(size):
            moistVal=moistNoise([i/size, j/size])
            tempVal=tempNoise([i/size, j/size])
            
            if (moistNoise([i/size, j/size])>-0.2):
                moistLevel="LL"
            elif (moistNoise([i/size, j/size])>-0.1):
                moistLevel="L"
            elif (moistNoise([i/size, j/size])<0.2):
                moistLevel="M"
            elif (moistNoise([i/size, j/size])<0.1):
                moistLevel="H"

            if (moistNoise([i/size, j/size])>-0.2):
                tempLevel="LL"
            elif (moistNoise([i/size, j/size])>-0.1):
                tempLevel="L"
            elif (moistNoise([i/size, j/size])<0.2):
                tempLevel="M"
            elif (moistNoise([i/size, j/size])<0.1):
                tempLevel="H"
                
            if (moistLevel=="M"and tempLevel=="LL"):
                noiseVal=3
                #Polar Ice
            if (moistLevel=="L"and tempLevel=="LL"):
                noiseVal=2.8
                #Polar Desert
            if (moistLevel=="M"and tempLevel=="L"):
                noiseVal=2.6
                #Tundra
            if (moistLevel=="L"and tempLevel=="LL"):
                noiseVal=2.4
                #Boreal
            if (moistLevel=="L"and tempLevel=="M"):
                noiseVal=2.2
                #Cool Desert Scrub
            if (moistLevel=="L"and tempLevel=="M"):
                noiseVal=2.2
                #Tempature fields
            if (moistLevel=="H"and tempLevel=="M"):
                noiseVal=2.0
                #Tempature Woods
            if (moistLevel=="L"and tempLevel=="H"):
                noiseVal=1.8
                #Savanna Shrubs
            if (moistLevel=="M"and tempLevel=="H"):
                noiseVal=1.6
                #Tropic Woods
            if (moistLevel=="H"and tempLevel=="H"):
                noiseVal=1.0
                
            
                
            noiseVal=0
            #noiseVal += moistNoise([i/size, j/size])
            #noiseVal += moistNoise([i/size, j/size])
            print(moistVal,tempVal)
            
            row.append(noiseVal)
        pic.append(row)
        
        
    plt.imshow(pic, cmap='gray')

    plt.grid(False);plt.axis('off')

    plt.show()
    #print(pic)

generateTerrain(size,moisture,tempature)