import matplotlib.pyplot as plt
import random 
from perlin_noise import PerlinNoise
import math
from PIL import Image

import math
import os
def generateHeight(octaveVal, offsetVal,showPlot = False):
    size=512
    ROOT = os.path.dirname(os.path.abspath(__file__))

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
        
    #os.remove(ROOT+"/tempHeight.png")
    
    plt.imshow(pic, cmap='Grays')
    plt.grid(False);plt.axis('off')
    #plt.show() 
    plt.savefig(ROOT+"/tempHeight.png",dpi=300)
    
    img=Image.open(ROOT+"/tempHeight.png")
    if math.floor((255/(100/offsetVal)))-50<0:
        alphaVal=20
    else:
        alphaVal=math.floor((255/(100/offsetVal)))-50
    
    img.putalpha(alphaVal)
    
    #os.remove(ROOT+"/tempHeightNew.png")
    img.save(ROOT+"/tempHeightNew.png")
    #img.show()
    
    
#generateHeight(10, 100)