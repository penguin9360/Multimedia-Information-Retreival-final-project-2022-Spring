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
ORIGINAL = False
MODELS = ["darknet19", "densenet201", "extraction", "resnet50", "vgg-16"]
CLASSES = ["aircrafts", "labrador", "penguin", "wild_cat", "pizza"]

darknet_top_5 = [0, 0, 0, 0, 0]
densenet_top_5 = [0, 0, 0, 0, 0]
extraction_top_5 = [0, 0, 0, 0, 0]
resnet_top_5 = [0, 0, 0, 0, 0]
vgg_top_5 = [0, 0, 0, 0, 0]

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
            for line in lines:
                if c == "aircrafts":
                    if "airline" in line or "plane" in line or "jet" in line:
                        if m == "darknet19":
                            darknet_top_5[0] += 1
                        if m == "densenet201":
                            densenet_top_5[0] += 1
                        if m == "extraction":
                            extraction_top_5[0] += 1
                        if m == "resnet50":
                            resnet_top_5[0] += 1
                        if m == "vgg-16":
                            vgg_top_5[0] += 1
                        break

                if c == "labrador":
                    if "Labrador" in line:
                        if m == "darknet19":
                            darknet_top_5[1] += 1
                        if m == "densenet201":
                            densenet_top_5[1] += 1
                        if m == "extraction":
                            extraction_top_5[1] += 1
                        if m == "resnet50":
                            resnet_top_5[1] += 1
                        if m == "vgg-16":
                            vgg_top_5[1] += 1
                        break

                if c == "penguin":
                    if "penguin" in line:
                        if m == "darknet19":
                            darknet_top_5[2] += 1
                        if m == "densenet201":
                            densenet_top_5[2] += 1
                        if m == "extraction":
                            extraction_top_5[2] += 1
                        if m == "resnet50":
                            resnet_top_5[2] += 1
                        if m == "vgg-16":
                            vgg_top_5[2] += 1
                        break

                if c == "wild_cat":
                    if "leopard" in line or "jaguar" in line or "cat" in line or "tabby" in line:
                        if m == "darknet19":
                            darknet_top_5[3] += 1
                        if m == "densenet201":
                            densenet_top_5[3] += 1
                        if m == "extraction":
                            extraction_top_5[3] += 1
                        if m == "resnet50":
                            resnet_top_5[3] += 1
                        if m == "vgg-16":
                            vgg_top_5[3] += 1
                        break

                if c == "pizza":
                    if "pizza" in line:
                        if m == "darknet19":
                            darknet_top_5[4] += 1
                        if m == "densenet201":
                            densenet_top_5[4] += 1
                        if m == "extraction":
                            extraction_top_5[4] += 1
                        if m == "resnet50":
                            resnet_top_5[4] += 1
                        if m == "vgg-16":
                            vgg_top_5[4] += 1
                        break
print("darknet_top_5: ", darknet_top_5)
print("densenet_top_5: ", densenet_top_5)
print("extraction_top_5: ", extraction_top_5)
print("resnet_top_5: ", resnet_top_5)
print("vgg_top_5: ", vgg_top_5)


darknet_bar = plt.bar(ind, darknet_top_5, width, color='orangered')

densenet_bar = plt.bar(ind + width, densenet_top_5, width, color='orange')

extraction_bar = plt.bar(ind + width * 2, extraction_top_5, width, color='yellowgreen')

resnet_bar = plt.bar(ind + width * 3, resnet_top_5, width, color='deepskyblue')

vgg_bar = plt.bar(ind + width * 4, vgg_top_5, width, color='slateblue')

plt.xlabel("Classes")
plt.ylabel('Correct Top-5 Classifications')
if ORIGINAL:
    plt.title("Top-5 Classification Results with Original Images")
else:
    plt.title("Top-5 Classification Results with Noised Images")

plt.xticks(ind + width, ['Aircraft', 'Labrador', 'Penguin', 'Wild Cat', 'Pizza'])
plt.yticks(np.arange(0, 21, step=2))
plt.legend((darknet_bar, densenet_bar, extraction_bar, resnet_bar, vgg_bar), ('darknet19', 'densenet201', 'extraction', 'resnet50', 'vgg-16'))

plt.show()
