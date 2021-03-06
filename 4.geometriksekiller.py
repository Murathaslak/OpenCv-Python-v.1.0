# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 14:52:38 2021

@author: OSMAN MURAT HAŞLAK
"""

import cv2
import numpy as np

image = np.zeros((512,512,3),np.uint8)



# ===================YAZI YAZMAK======================================================
# font = cv2.FONT_HERSHEY_COMPLEX
# cv2.putText(image,"OpenCv",(10,150),font,4,(0,155,255),2,cv2.LINE_AA)
#============================================================================

# ==================ÇOKGEN ÇİZMEK=================================================
# pts = np.array([[20,30],[100,120],[255,255],[10,400]],np.int32)
# pts2 = pts.reshape(-1,1,2)
# cv2.polylines(image,[pts],True,(255,255,255),3)
# #cv2.polylines(image,[pts],False,(255,255,255),3)
# =============================================================================

# ==================ELİPS ÇİZMEK===============================================
# cv2.ellipse(image,(256,256),(100,50),0,0,180,(255,100,0),3)
# cv2.ellipse(image,(100,100),(100,50),0,0,180,(255,100,0),-1)
# =============================================================================

# ===================DAİRE ÇİZMEK====================================================
# cv2.circle(image, (255,255),60,(120,120,120),2)
# cv2.circle(image, (100,100),90,(255,50,120),-1)
# =============================================================================

# ================ÇİZGİ ÇEKMEK=========================================================
# cv2.line(image,(0,0),(511,511),(255,0,0),5)
# cv2.line(image,(50,400),(400,50),(0,255,0),10)
# =============================================================================

# ==================DİKDÖRTGEN ÇİZMEK======================================================
# cv2.rectangle(image,(50,50),(300,300),(0,0,255),5)
# cv2.rectangle(image,(300,300),(511,511),(0,0,255),-1)
# =============================================================================

cv2.imshow('resim',image)
cv2.waitKey(0)
cv2.destroyAllWindows()