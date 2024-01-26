import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('lesmis.jpeg', 1)

def box_kernel(size):
     k = np.ones((size,size),np.float32)/(size**2)
     return k

size=5
box_filter_img = cv2.filter2D(img,-1,box_kernel(size))

cv2.imwrite('blured-lesmis.jpeg', box_filter_img)

