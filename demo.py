import os
import cv2
import numpy as np

imgl=('image1.png','image2.png',)
boxl=([10,10,128,128,3],[10,10,128,128,3]
   )

o1='./1/'
o2='./2/'

for x in os.listdir(o1):
    if not os.path.isdir(o2+x):
        os.mkdir(o2+x)
    for y,z in zip(imgl,boxl):
        w,h,r,_,hhh=z
        w2,h2,r2=w,h,r
        w3,h3,r3=w*4//3,h*4//3,r*4//3
        if hhh==1:
            w3, h3, r3 = w * 1, h * 1, r * 1
        if hhh==2:
            w3, h3, r3 = w * 2, h * 2, r * 2
        if hhh == 3:
            w3, h3, r3 = w * 3, h * 3, r * 3
        if hhh == 4:
            w3, h3, r3 = w * 4, h * 4, r * 4
        if os.path.isfile(o1+x+'/'+y):
            img=cv2.imread(o1+x+'/'+y)
            cv2.rectangle(img, (w2, h2), (w2+r2, h2+r2), (0, 0, 255), 3)
            imgp=img[h2:h2+r2,w2:w2+r2]
            imgp=cv2.resize(imgp,(r3,r3),interpolation=cv2.INTER_LANCZOS4)
            b=cv2.resize(img,(0,0),fx=1,fy=1,interpolation=cv2.INTER_LANCZOS4)
            b[-r3:,0:r3]=imgp
            cv2.imwrite(o2+x+'/'+y[:-3]+'jpg',b)


