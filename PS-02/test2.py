import numpy as np
import os
import cv2
import matplotlib.pyplot as mplt
import random

# path prefix
pth = '../data/'

# files to be used as samples
# list *files* holds the names of the test images
files = sorted(os.listdir(pth))
print files

# Usefull function
def rg(img_path):
    return cv2.imread(pth+img_path, cv2.IMREAD_GRAYSCALE)

def Filter(img,n,t=0):
    """ Function that apply a mean filter to an image array
        Input arguments
        img: image array
        n: kernel size(n*n)
        t: type of filter(0:mean,1:median)
        Output
        img: The image with mean filtering applied      
    """
    if t == 0 :
      print "mean filter"
      img = np.array(img)
      kernel = np.ones((n,n),np.float32)/(n*n)
      img = cv2.filter2D(img,-1,kernel)
    else:
      print "median filter"
      img = cv2.medianBlur(img,n)

    return img

def applySaPN(img):
    """ Function that apply Salt and Pepper Noise to an array image
        Input arguments
            img: image array
        Output
            img: The image with Salt and Pepper Noise     
    """
    N = img.shape[0]
    M = img.shape[1]
    for i in range(0,N):
        for j in range(0,M):
            a = random.randint(0,10)
            if a == 0:
                img[i][j]= 0
            if a == 10:
                img[i][j]= 255
                
    return img


img = rg(files[4])
img_mf = Filter(img,3,1)
mplt.subplot(121),mplt.imshow(img),mplt.title('Original')
mplt.xticks([]), mplt.yticks([])
mplt.subplot(122),mplt.imshow(img_mf),mplt.title('Filtered')
mplt.xticks([]), mplt.yticks([])
mplt.show(block = False)


k = 1
img = rg(files[k])
img = applySaPN(img)
img_mf = Filter(img,3,1)
mplt.figure()
mplt.subplot(131),mplt.imshow(rg(files[k])),mplt.title(files[k])
mplt.xticks([]), mplt.yticks([])
mplt.subplot(132),mplt.imshow(img),mplt.title('Image with SaPN')
mplt.xticks([]), mplt.yticks([])
mplt.subplot(133),mplt.imshow(img_mf),mplt.title('Median Blur')
mplt.xticks([]), mplt.yticks([])
mplt.show()

