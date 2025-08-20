import cv2
import matplotlib.pyplot as plt
img = cv2.imread("coolie disco.jpeg")
blur = cv2.blur(img,(7,7))
plt.imshow(cv2.cvtColor(blur,cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()
