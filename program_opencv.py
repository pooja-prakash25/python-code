from multiprocessing.connection import wait
from tkinter import PhotoImage
import cv2

img=cv2.imread('BRIDAL.jpg', 0)
print(img)

cv2.imshow('Photos',img)

cv2.waitKey(0)

cv2.destroyAllWindows()

cv2.imwrite('photoshoot.png',img)

