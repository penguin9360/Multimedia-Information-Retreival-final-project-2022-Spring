import numpy as np
import matplotlib.pyplot as plt
from pylab import rcParams
rcParams['figure.figsize'] = 12, 6
from matplotlib.ticker import MaxNLocator
# References:
# https://www.geeksforgeeks.org/plotting-multiple-bar-charts-using-matplotlib-in-python/
# https://www.pythontutorial.net/python-basics/python-read-text-file/
N = 5
ind = np.arange(N)
width = 0.15
ORIGINAL = True
MODELS = ["darknet19", "densenet201", "extraction", "resnet50", "vgg-16"]
CLASSES = ["aircrafts", "labrador", "penguin", "wild_cat", "pizza"]

darknet_top_1 = [0, 0, 0, 0, 0]
densenet_top_1 = [0, 0, 0, 0, 0]
extraction_top_1 = [0, 0, 0, 0, 0]
resnet_top_1 = [0, 0, 0, 0, 0]
vgg_top_1 = [0, 0, 0, 0, 0]

for c in CLASSES:
    for m in MODELS:
        for ctr in range(1, 21):
            if ORIGINAL:
                result_path = "output/original/" + c + "/" + m + "/" + str(ctr) + ".txt"
            else:
                result_path = "output/noised/" + c + "/" + m + "/" + str(ctr) + ".txt"
            lines = []
            with open(result_path) as f:
                lines = f.readlines()

            if c == "aircrafts":
                if "airline" in lines[0] or "plane" in lines[0] or "jet" in lines[0]:
                    if m == "darknet19":
                        darknet_top_1[0] += 1
                    if m == "densenet201":
                        densenet_top_1[0] += 1
                    if m == "extraction":
                        extraction_top_1[0] += 1
                    if m == "resnet50":
                        resnet_top_1[0] += 1
                    if m == "vgg-16":
                        vgg_top_1[0] += 1

            if c == "labrador":
                if "Labrador" in lines[0]:
                    if m == "darknet19":
                        darknet_top_1[1] += 1
                    if m == "densenet201":
                        densenet_top_1[1] += 1
                    if m == "extraction":
                        extraction_top_1[1] += 1
                    if m == "resnet50":
                        resnet_top_1[1] += 1
                    if m == "vgg-16":
                        vgg_top_1[1] += 1

            if c == "penguin":
                if "penguin" in lines[0]:
                    if m == "darknet19":
                        darknet_top_1[2] += 1
                    if m == "densenet201":
                        densenet_top_1[2] += 1
                    if m == "extraction":
                        extraction_top_1[2] += 1
                    if m == "resnet50":
                        resnet_top_1[2] += 1
                    if m == "vgg-16":
                        vgg_top_1[2] += 1

            if c == "wild_cat":
                if "leopard" in lines[0] or "jaguar" in lines[0] or "cat" in lines[0] or "tabby" in lines[0]:
                    if m == "darknet19":
                        darknet_top_1[3] += 1
                    if m == "densenet201":
                        densenet_top_1[3] += 1
                    if m == "extraction":
                        extraction_top_1[3] += 1
                    if m == "resnet50":
                        resnet_top_1[3] += 1
                    if m == "vgg-16":
                        vgg_top_1[3] += 1

            if c == "pizza":
                if "pizza" in lines[0]:
                    if m == "darknet19":
                        darknet_top_1[4] += 1
                    if m == "densenet201":
                        densenet_top_1[4] += 1
                    if m == "extraction":
                        extraction_top_1[4] += 1
                    if m == "resnet50":
                        resnet_top_1[4] += 1
                    if m == "vgg-16":
                        vgg_top_1[4] += 1

print("darknet_top_1: ", darknet_top_1)
print("densenet_top_1: ", densenet_top_1)
print("extraction_top_1: ", extraction_top_1)
print("resnet_top_1: ", resnet_top_1)
print("vgg_top_1: ", vgg_top_1)


darknet_bar = plt.bar(ind, darknet_top_1, width, color='orangered')

densenet_bar = plt.bar(ind + width, densenet_top_1, width, color='orange')

extraction_bar = plt.bar(ind + width * 2, extraction_top_1, width, color='yellowgreen')

resnet_bar = plt.bar(ind + width * 3, resnet_top_1, width, color='deepskyblue')

vgg_bar = plt.bar(ind + width * 4, vgg_top_1, width, color='slateblue')

plt.xlabel("Classes")
plt.ylabel('Correct Top-1 Classifications')
if ORIGINAL:
    plt.title("Top-1 Classification Results with Original Images")
else:
    plt.title("Top-1 Classification Results with Noised Images")

plt.xticks(ind + width, ['Aircraft', 'Labrador', 'Penguin', 'Wild Cat', 'Pizza'])
plt.yticks(np.arange(0, 21, step=2))
plt.legend((darknet_bar, densenet_bar, extraction_bar, resnet_bar, vgg_bar), ('darknet19', 'densenet201', 'extraction', 'resnet50', 'vgg-16'))

plt.show()
