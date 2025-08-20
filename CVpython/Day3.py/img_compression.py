import cv2
img = cv2.imread("GBU.jpeg")
cv2.imwrite("compressed_image_100.jpeg",img,[int(cv2.IMWRITE_JPEG_QUALITY),100])
cv2.imwrite("compressed_image_70.jpeg",img,[int(cv2.IMWRITE_JPEG_QUALITY),70])
