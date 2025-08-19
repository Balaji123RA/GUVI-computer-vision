import cv2
import matplotlib.pyplot as plt
img = cv2.imread("coolie disco.jpeg")
circle = cv2.circle(img,(150,150),30,(0,0,255),10)
plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()
