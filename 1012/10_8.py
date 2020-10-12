import numpy as np
import cv2
import matplotlib.pyplot as plt
'''
img = cv2.imread(r'C:\Users\Administrator\Desktop\cat_img_1.jpg',0)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])
plt.show()
'''
img = cv2.imread(r'C:\Users\Administrator\Desktop\cat_img_1.jpg',0)
cv2.imshow(r'C:\Users\Administrator\Desktop\cat_img_1.jpg',img)
cv2.waitKey(0)
cv2.destroyAllWindows()