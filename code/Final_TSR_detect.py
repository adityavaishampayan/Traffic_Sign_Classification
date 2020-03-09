# -*- coding: utf-8 -*-
"""
Created on Thu May 16 21:16:40 2019

@author: nakul
"""

import sys
try:
    sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
except:
    pass
import cv2
import numpy as np
import matplotlib.pyplot as plt
import glob
import pickle
from sklearn import datasets
from sklearn import svm



imgList = glob.glob("/media/nakul/DATA/Ubuntu_UMD_Courses/Perception/Project-6/TSR/input/*")
imgList.sort()
#imgList = imgList[80:]
hog = cv2.HOGDescriptor()
filename = open("SVM_Classifier.sav",'rb')
clf = pickle.load(filename)

for img in imgList:
    regions=[] 
    # ======== Traffic sign detection using HSV ===================== #
    image = cv2.imread(img)
    #image = cv2.fastNlMeansDenoisingColored(image,None,10,10,7,21)
    tmpl = glob.glob("/media/nakul/DATA/Ubuntu_UMD_Courses/Perception/Project-6/TSR/templates/*")
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # ======= Traffic sign detection using MSER Algorithm ============= #

    # ================================================================  #
    mask_r1 = cv2.inRange(hsv, np.array([0, 70, 100]), np.array([15, 255, 255]))
    mask_r2 = cv2.inRange(hsv, np.array([160, 70, 100]), np.array([180, 255, 255]))
    dst = cv2.addWeighted(mask_r1,1.0,mask_r2,1.0,0)
    blur = cv2.GaussianBlur(dst,(5,5),0)
    _,contours,hierarchy = cv2.findContours(blur, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    tmpl = cv2.imread('00615_00002.ppm')
    for cnt in contours:
        x,y,w,h = cv2.boundingRect(cnt)
        #print('ar', cv2.contourArea(cnt))
        if w/h >= 1.0 and w/h <= 2.0 and cv2.contourArea(cnt) >= 400 and cv2.contourArea(cnt) <= 3000:
            red1 = cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)

                        
            regions.append(image[y: y+h, x: x+w])
            resized = cv2.resize(regions, (64, 64)) 
            h = hog.compute(resized)
            h = h.reshape(1, -1)
            y_pred = loaded_model.predict(h)
            class_probabilities = loaded_model.predict_proba(h)
            if np.amax(class_probabilities) >= 0.75:
                
                template = cv2.imread(tmpl[y_pred])            
            
                tmpl = cv2.resize(template,(w,h))
                          
                
                if x > w:                
                        image[y: y+h, x-w: x] = tmpl                
                else:
                        image[y: y+h, x+w: x + (2*w)] = tmpl
                
            
    mask_b = cv2.inRange(hsv, np.array([100,45,50]), np.array([130,250,250]))       
    blur_b = cv2.GaussianBlur(mask_b,(5,5),0)
    _,contours,hierarchy = cv2.findContours(blur_b, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        x,y,w,h = cv2.boundingRect(cnt)
        #print('ar', w/h)
        if w/h >= 0.5 and w/h <= 1.5 and cv2.contourArea(cnt) >= 400 and cv2.contourArea(cnt) <= 4000:
            blue = cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
              regions.append(image[y: y+h, x: x+w])
            resized = cv2.resize(regions, (64, 64)) 
            h = hog.compute(resized)
            h = h.reshape(1, -1)
            y_pred = loaded_model.predict(h)
            class_probabilities = loaded_model.predict_proba(h)
            if np.amax(class_probabilities) >= 0.75:
                
                template = cv2.imread(tmpl[y_pred])            
            
                tmpl = cv2.resize(template,(w,h))
                          
                
                if x > w:                
                        image[y: y+h, x-w: x] = tmpl                
                else:
                        image[y: y+h, x+w: x + (2*w)] = tmpl
                  
    #cv2.imshow('Image',blur_b)
    cv2.imshow('conv',image)
    #cv2.imshow('result',blur)
    
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

#cv2.waitKey(0)
cv2.destroyAllWindows()







