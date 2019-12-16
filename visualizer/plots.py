import matplotlib
import matplotlib.pyplot as plt
import numpy as np

labels = ['G1', 'G2', 'G3', 'G4', 'G5']
avans_means = [20, 34, 30, 60, 27]
has_means = [25, 32, 34, 20, 25]
fontys_means = [2, 3, -5, 10, -10]

x = np.arange(len(labels))  # the label locations
width = 0.25  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width, avans_means, width, label='Avans')
rects2 = ax.bar(x + width, has_means, width, label='HAS')
rects3 = ax.bar(x, fontys_means, width, label='Whatever Fontys is doing')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Performance index')
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


autolabel(rects1)
autolabel(rects2)
autolabel(rects3)

fig.tight_layout()

plt.show()
