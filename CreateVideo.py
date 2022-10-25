import os
import cv2

path = "Images/"
Images = []

list_of_files = os.listdir(path)

for file in list_of_files:
    name, ext = os.path.splitext(file)

    if ext in ['.gif','.png','.jpg','.jpeg','.jfif']:
        file_name = path + file
        print(file_name)

        Images.append(file)

count = len(Images)

frame = cv2.imread(Images[0])
height = frame.shape[0]
width = frame.shape[0]
channels = frame.shape[2]

size = (width,height)
print(size)

out = cv2.VideoWriter('Project.avi',cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size) 

for i in range(0,count-1):
    img = cv2.imread(Images[i])
    out.write(img)

print("Done!")
