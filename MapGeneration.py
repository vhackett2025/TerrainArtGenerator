import matplotlib.pyplot as plt
from perlin_noise import PerlinNoise
size=32

noise = PerlinNoise(octaves=10, seed=1)

pic = [[noise([i/size, j/size]) for j in range(size)] for i in range(size)]

plt.imshow(pic, cmap='gray')

plt.grid(False);plt.axis('off')

plt.show()
print("ELLO")