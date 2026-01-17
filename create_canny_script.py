import os
import numpy as np
import cv2

CATS_IMAGES_PATH = "cat"
OUTPUT_FOLDER = "Canny"
os.makedirs(OUTPUT_FOLDER,exist_ok=True)

files = os.listdir(CATS_IMAGES_PATH)

print(f"There are {len(files)}")

for file in files:
    img_path = os.path.join(CATS_IMAGES_PATH,file)

    img = cv2.imread(img_path)

    canny = cv2.Canny(img,100,200)

    # (H,W,3)
    canny_3_channels = np.stack([canny]*3,axis=2)

    save_path = os.path.join(OUTPUT_FOLDER,file)

    cv2.imwrite(save_path,canny_3_channels)

print("Print Finished")
print(f"Canny Shape : {canny.shape}")
print(f"Canny 3 Channels Shape : {canny_3_channels.shape}")