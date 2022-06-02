import numpy as np
import random
import matplotlib.pyplot as plt

def main():
    x = np.arange(0,3,0.01)
    y = np.sin(x)

    y_dev = []
    for i in range(len(y)):
        y_dev.append(
            ((y[i] + (random.randint(0,10)-5)/50))
            )

    plt.plot(x,y_dev)
    plt.show()

if __name__ == "__main__":
    main()