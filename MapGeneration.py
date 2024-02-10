import matplotlib.pyplot as plt
import random 
from perlin_noise import PerlinNoise
size=128

moisture = 8

tempature = 6

#size is the square dimentions
#octaves = thing we change!
#seed is randomness
moistNoise = PerlinNoise(octaves=moisture, seed=random.randrange(0,100))
tempNoise = PerlinNoise(octaves=tempature, seed=random.randrange(0,100))

#moistPic = [[moistNoise([i/size, j/size]) for j in range(size)] for i in range(size)]
#moistPic = [[tempNoise([i/size, j/size]) for j in range(size)] for i in range(size)]

pic = []
for i in range(size):
    row = []
    for j in range(size):
        noiseVal=0
        noiseVal += moistNoise([i/size, j/size])
        noiseVal += moistNoise([i/size, j/size])
        row.append(noiseVal)
    pic.append(row)
    
    
plt.imshow(pic, cmap='gray')

plt.grid(False);plt.axis('off')

plt.show()
