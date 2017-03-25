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

def histo_eq(img):
    """ Function that runs histogram equalization in a image array
        Input arguments
        img: image array
        Output
        img: The image with histogram equalization      
    """
    
    hist,_ = np.histogram(img,256,[0,256])
    histl = list(hist.flatten())
    
    cdf = np.cumsum(filter(lambda a: a != 0, list(histl)))
    v = list(set(img.flatten()))
    v = sorted(v)
    cdf_v = {}
    for i in range(0,len(v)):
        cdf_v[v[i]] = cdf[i]
    N = img.shape[0]
    M = img.shape[1]
    cdf_min = min(cdf)
    img = np.array(img)
    for i in range(0,N):
        for j in range(0,M):
            img[i][j]= ((cdf_v.get(img[i][j])-cdf_min)*(255))/(M*N-1)
    return img
            
    
for i in [6,9,10,13,15,17]:
    print(files[i])
    img = rg(files[i])
    imgh = histo_eq(rg(files[i]))
    mplt.figure()
    mplt.subplot(221)
    mplt.imshow(rg(files[i]), cmap='gray')
    mplt.title(files[i])
    mplt.subplot(222)
    mplt.imshow(imgh, cmap='gray')
    mplt.title("histo_eq("+files[i]+")")
    mplt.subplot(223)
    hist, bins = np.histogram(img.flatten(),256,[0,256])
    width = 0.7 * (bins[1] - bins[0])
    center = (bins[:-1] + bins[1:]) / 2
    cdf = hist.cumsum()
    cdf_n = cdf*hist.max()/ cdf.max()
    mplt.bar(center, hist, align='center', width=width)
    p_cdf_n, = mplt.plot(cdf_n,color = 'r')
    mplt.legend([p_cdf_n], ['cdf'])
    mplt.xlim( (0, 255) )
    mplt.subplot(224)
    hist, bins = np.histogram(imgh.flatten(),256,[0,256])
    width = 0.7 * (bins[1] - bins[0])
    center = (bins[:-1] + bins[1:]) / 2
    mplt.bar(center, hist, align='center', width=width)
    mplt.xlim( (0, 255) )
    mplt.show(block = False)           