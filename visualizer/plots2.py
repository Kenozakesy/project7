import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from numpy import ndarray
import array

labels = ['G1', 'G2', 'G3', 'G4', 'G5']

means = [1, 2, 3, 4, 5]

x = np.arange(len(labels))  # the label locations
width = 0.25  # the width of the bars

rects = ndarray((5,), int)

fig, ax = plt.subplots()
rects[0] = ax.bar(x - width / 2, means, width, label='Avans')
rects[1] = ax.bar(x + width / 2, means, width, label='HAS')
rects[2] = ax.bar(x + width * 1.5, means, width, label='Whatever Fontys is doing')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('performance index')
ax.set_title('Performance level of schools')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()

        if height < 0:
            vertical = -10
        else:
            vertical = 3

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
