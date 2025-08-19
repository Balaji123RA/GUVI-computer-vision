import cv2
import matplotlib.pyplot as plt
img = cv2.imread("coolie disco.jpeg")
(h,w) = img.shape[:2]
center = (w // 2,h // 5)
angle = 50
scale = 0.5
M = cv2.getRotationMatrix2D(center,angle,scale)
rotated = cv2.warpAffine(img,M,(w,h))
cv2.imshow("Rotated by 45 Degree",rotated)
plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()
