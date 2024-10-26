import os
import subprocess
import sys
import pathlib
from playsound import playsound


MODELS = ["darknet19", "densenet201", "extraction", "resnet50", "vgg-16"]
CLASSES = ["aircrafts", "labrador", "penguin", "wild_cat", "pizza"]

# The execution could be long.
# So, if you would like to have some musics for notification when the execution is finished,
# simply put a "music.mp3" file (any mp3 files after being renamed to 'music') under the darknet root directory
# and change PLAY_MUSIC_AFTER_FINISHED = True
# :)
PLAY_MUSIC_AFTER_FINISHED = False
ORIGINAL = True

FILE_EXTENSION = ".jpg"
for c in CLASSES:
    for m in MODELS:
        for ctr in range(1, 21):
            # check extension
            if c == 'aircrafts' or c == 'penguin' or c == 'pizza':
                FILE_EXTENSION = '.jpeg'
            else:
                FILE_EXTENSION = '.jpg'

            if ORIGINAL:
                path = "output/original/" + c + "/" + m + "/"
                pathlib.Path(path).mkdir(parents=True, exist_ok=True)
                f = open(path + str(ctr) + ".txt", "w")
                p = subprocess.run(["./darknet", "classifier", "predict", "cfg/imagenet1k.data",
                                    "cfg/" + m + ".cfg",
                                    "weights/" + m + ".weights",
                                    "data/finalproj/original/" + c + "/" + str(ctr) + FILE_EXTENSION], stdout=f, text=True)
            else:
                path = "output/noised/" + c + "/" + m + "/"
                pathlib.Path(path).mkdir(parents=True, exist_ok=True)
                f = open(path + str(ctr) + ".txt", "w")
                p = subprocess.run(["./darknet", "classifier", "predict", "cfg/imagenet1k.data",
                                    "cfg/" + m + ".cfg",
                                    "weights/" + m + ".weights",
                                    "data/finalproj/noised/" + c + "/" + str(ctr) + FILE_EXTENSION], stdout=f,
                                   text=True)
            # print("stdout: ", p.stdout)
            # print("stderr: ", p.stderr)
            f.close()
if PLAY_MUSIC_AFTER_FINISHED:
    playsound("music.mp3")
