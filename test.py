import cv2 as cv
import numpy as np
import laplacian_foveation as fv
from random import randint
#from matplotlib import pyplot as plt
#from bs4  import BeautifulSoup as bs
#from lxml import etree
#import urllib

#import requests
#import os
#from pycocotools.coco import COCO
import skimage.io

def main():
    rho=-0.5

    # fovea size
    sigma_xx=50
    sigma_yy=100
    #sigma_xy=int(np.floor(rho*sigma_xx*sigma_yy))
    sigma_xy=0

    # pyramid levels
    levels=5
    
    url_image = 'https://farm3.staticflickr.com/2794/4190008256_fb66764971_z.jpg'
    img = skimage.io.imread(url_image)
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    
    if img is not None:
        height, width, _ = img.shape
        print('Image dims (height, width): {}, {}'.format(height, width))
    else:
        raise ValueError
    
    # create the Laplacian blending object
    my_lap_obj=fv.LaplacianBlending(width,height,levels,sigma_xx,sigma_yy,sigma_xy)
    try:
        while True:

            sigma_x=sigma_xx
            sigma_y=sigma_yy

            #sigma_x=randint(1, sigma_xx)
            #sigma_y=randint(1, sigma_yy)

            # random fixation points
            center=np.array([randint(1,width), randint(1,height)])
            # fixation at image center
            #center=[int(width/2.0), int(height/2.0)]

            # update fovea location
            my_lap_obj.update_fovea(width,height,sigma_x,sigma_y,sigma_xy)
            
            foveated_img=my_lap_obj.Foveate(img,center)

            cv.waitKey(500)
            cv.ellipse(foveated_img, center=center, axes=(sigma_xx,sigma_yy), angle=0, startAngle=0, endAngle=360, color=(255,0,0), thickness=2)
            cv.drawMarker(foveated_img, position=center, color=(255,0,0), markerType=cv.MARKER_CROSS, markerSize=10, thickness=2)
            cv.imshow('image',foveated_img)

    except KeyboardInterrupt:
        print('interrupted!')
    
    cv.destroyAllWindows()


if __name__ == "__main__":
    main()

