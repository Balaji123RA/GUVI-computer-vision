import cv2
import matplotlib.pyplot as plt
img = cv2.imread("GBU.jpeg")
blur=cv2.blur(img,(5,5))
gaussian = cv2.medianBlur(img,5)
median = cv2.medianBlur(img,5)
title = ["original","Blur","Gaussian","Median"]
images =[img,blur,gaussian,median]
for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i]),plt.title(title[i])
    plt.axis("off")
plt.show()