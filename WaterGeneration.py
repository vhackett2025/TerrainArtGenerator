import random
import numpy as np
import matplotlib.pyplot as plt

def generateWater(waterVal):
    x=np.linespace(0,10,100)
    y = np.sin(x)
    fig, waterGraph = plt.subplots()
    waterGraph.plot(x,y,color="black")
    plt.show()