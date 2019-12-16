import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from random import randint
import namegenerator
from numpy import ndarray
import array

labels = ['2017', '2018', '2019', '2020', '2021']

x = np.arange(len(labels))  # the label locations
size = 10

width = 1 / (size * 1.3)  # the width of the bars

rects = []
fig, ax = plt.subplots()

even = None
if (size % 2) == 0:
    even = True
else:
    even = False

means = []
# multiplier = size
for i in range(size):
    for t in range(5):
        means.append(randint(1, 9))
    rects.append(ax.bar(x - ((size - 1) * width / 2) + (width * i), means, width, label=(namegenerator.gen())))
    means = []

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('performance index')
ax.set_title('Performance level of schools')
ax.set_xticks(x)
ax.set_xticklabels(labels)
# ax.legend() #turn on legend


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()

        if height < 0:
            vertical = -10
        else:
            vertical = 2

        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, vertical),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


for x in rects:
    autolabel(x)

fig.tight_layout()

plt.show()

# how to set fixed array size python
