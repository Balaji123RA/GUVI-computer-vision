import cv2
import matplotlib.pyplot as plt
img = cv2.imread("GBU.jpeg")
cv2.rectangle(img,(160,160),(70,70),(0,0,255),3)
plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()