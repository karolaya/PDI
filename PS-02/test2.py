import numpy as np
import os
import cv2
import matplotlib.pyplot as mplt

# path prefix
pth = '../data/'

# files to be used as samples
# list *files* holds the names of the test images
files = sorted(os.listdir(pth))
print files

# Usefull function
def rg(img_path):
    return cv2.imread(pth+img_path, cv2.IMREAD_GRAYSCALE)

def meanFilter(img,n):
    """ Function that apply a mean filter to an image array
        Input arguments
        img: image array
        Output
        img: The image with mean filtering applied      
    """
    img = np.array(img)
    kernel = np.ones((n,n),np.float32)/(n*n)
    img = cv2.filter2D(img,-1,kernel)

    return img

img = rg(files[4])
img_mf = meanFilter(img,3)

mplt.subplot(121),mplt.imshow(img),mplt.title('Original')
mplt.xticks([]), mplt.yticks([])
mplt.subplot(122),mplt.imshow(img_mf),mplt.title('Averaging')
mplt.xticks([]), mplt.yticks([])
mplt.show()

