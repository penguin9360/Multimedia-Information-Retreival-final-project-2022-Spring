import cv2
import numpy as np
import pathlib
# reference: https://theailearner.com/2019/05/07/add-different-noise-to-an-image/

CLASSES = ["aircrafts", "labrador", "penguin", "wild_cat", "pizza"]
FILE_EXTENSION = ".jpg"
abnormal_files = []
for c in CLASSES:
    for ctr in range(1, 21):
        if c == 'aircrafts' or c == 'penguin' or c == 'pizza':
            FILE_EXTENSION = '.jpeg'
        else:
            FILE_EXTENSION = '.jpg'

        read_path = 'data/finalproj/original/' + c + "/" + str(ctr) + FILE_EXTENSION

        save_path = 'data/finalproj/noised/' + c + "/"
        pathlib.Path(save_path).mkdir(parents=True, exist_ok=True)
        save_img = save_path + str(ctr) + FILE_EXTENSION

        img = cv2.imread(read_path)
        # Generate Gaussian noise
        try:
            gauss = np.random.normal(0,1,img.size)
        except AttributeError:
            abnormal_files.append(read_path)
            continue

        gauss = gauss.reshape(img.shape[0],img.shape[1],img.shape[2]).astype('uint8')
        # Add the Gaussian noise to the image
        img_gauss = cv2.add(img,gauss)
        # Display the image
        cv2.imwrite(save_img,img_gauss)
        cv2.waitKey(0)

print("Abnormal files: ", abnormal_files)