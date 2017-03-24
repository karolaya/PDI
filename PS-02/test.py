import numpy as np
import os
import cv2
import matplotlib.pyplot as mplt

# path prefix
pth = '../data/'

# files to be used as samples
# list *files* holds the names of the test images
files = os.listdir(pth)
print files

# Usefull function
def rg(img_path):
    return cv2.imread(pth+img_path, cv2.IMREAD_GRAYSCALE)

def histo_eq(img,name):
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
    imgh = img.copy()
    #for i in range(0,N):
    #    for j in range(0,M):
    #        imgh[i][j]= round(((cdf_v[img[i][j]]-min(cdf))*(255))/(M*N-1))
    for row in imgh:
        for i in row:
            i = round(((cdf_v[i]-min(cdf))*(255))/(M*N-1))
    cdf_normalized = cdf *hist.max()/ cdf.max()
    print(str(N)+"x"+str(M))
    #print len(cdf)
    #print len(v)
    return imgh,cdf_normalized
            
    
#ftp = [2,4,7,8,11,17]
for i in [2]:
    img = rg(files[i])
    hist,_ = np.histogram(img.flatten(),256,[0,256])
    cdf = hist.cumsum()
    cdf_n = cdf*hist.max()/ cdf.max()
    imgh,cdf_nh = histo_eq(rg(files[i]),files[i])

    mplt.figure()

    mplt.subplot(151)
    mplt.imshow(rg(files[i]), cmap='gray')
    mplt.title(files[i])
    
    mplt.subplot(152)      
    mplt.hist(rg(files[i]),256,[0,256])
    mplt.xlim([0,256])
    mplt.show()    
    
    mplt.subplot(153)
    mplt.imshow(imgh, cmap='gray')
    mplt.title("histo_eq("+files[i]+")")
    
    mplt.subplot(154)      
    mplt.hist(imgh,256,[0,256])
    mplt.xlim([0,256])
    mplt.show() 
    
    mplt.subplot(155)
    mplt.plot(cdf_n)
    mplt.xlim([0,256])
    mplt.show()