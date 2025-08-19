import cv2
import matplotlib.pyplot as plt

# Read image
img = cv2.imread("coolie disco.jpeg")

# Apply Gaussian blur
gaussian = cv2.GaussianBlur(img, (5, 15), 5)

# Convert to grayscale
gray = cv2.cvtColor(gaussian, cv2.COLOR_BGR2GRAY)  # Use blurred image for grayscale

# Apply Canny edge detection
edges = cv2.Canny(gray, 100, 300)

# Apply Otsu's thresholding
threshold, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Display edges image using matplotlib with gray colormap
plt.imshow(edges, cmap='gray')
plt.axis("off")
plt.show()
