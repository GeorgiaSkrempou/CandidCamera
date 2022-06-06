import cv2
import glob
import os

# make an empty list
img_array = []

# loop through all files by filename in a sorted fashion
for filename in sorted(glob.glob('picamera_photos/*.jpeg')):
    # cerate an object with the images 
    img = cv2.imread(filename)
    # set the property shape of the img object
    height, width, layers = img.shape
    size = (width, height)
    # append the img to the img_array list
    img_array.append(img)

# construct the video
out = cv2.VideoWriter('timelapse.avi', cv2.VideoWriter_fourcc(*'DIVX'), 7, size)

# write images in the video
for i in range(len(img_array)):
    out.write(img_array[i])

# release video
out.release()

# remove images from local directory
file_list = glob.glob("picamera_photos/*.jpeg")
for file_path in file_list:
    os.remove(file_path)