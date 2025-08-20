import cv2
import matplotlib.pyplot as plt
img1 = cv2.imread("GBU.jpeg")
img2 = cv2.imread("GBU2.jpeg")

orb = cv2.ORB_create()
Kp1, des1 = orb.detectAndCompute(img1,None)
Kp2, des2 = orb.detectAndCompute(img2,None)
Brute_force = cv2.BFMatcher(cv2.NORM_HAMMING,crossCheck=True) 
matches = Brute_force.match(des1,des2) 
matches = sorted(matches,key = lambda x:x.distance) 
result = cv2.drawMatches(img1,Kp1,img2,Kp2,matches[:30],None,flags=2) 
plt.imshow(cv2.cvtColor(result,cv2.COLOR_BGR2RGB)) 
plt.axis("off") 
plt.show()