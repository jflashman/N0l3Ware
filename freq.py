from collections import Counter
from matplotlib import pyplot as plt


def freq(input):
    c = Counter(input)
    keys = []
    values = []
    for item in c.keys():
        keys.append(str(item))

    for item in c.values():
        values.append(int(item))

    plt.yticks(range(len(values)))
    plt.bar(keys, values, align='center')
    plt.show()