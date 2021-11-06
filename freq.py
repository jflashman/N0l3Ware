import numpy as np
from collections import Counter
from matplotlib import pyplot as plt


def freq(input):
    c = Counter(input)
    keys = []
    values = []
    for item in c.keys():
        keys.append(str(item))

    for item in c.values():
        values.append(str(item))

    
  
    plt.hist(keys, values, color='g')
    plt.show()


if __name__ == "__main__":
    freq("Hello World!")
