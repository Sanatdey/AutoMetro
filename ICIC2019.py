# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 17:43:36 2019

@author: SANAT DEY
"""

import cv2
import numpy as np
import serial

def main():
     status_list = [None ,None ,None ,None]
     ser = serial.Serial("COM4" , 9600)
     cap = cv2.VideoCapture(0)
     
     
     if cap.isOpened():
         ret ,frame = cap.read()
     else:
         ret = False
         
         
         
     while True:            
         ret , frame = cap.read()
         status = 0
         
         vid2 = cv2.cvtColor(frame , cv2.COLOR_BGR2HSV)
        
         B_low = np.array([100 ,150 ,100])
         B_high = np.array([140,  250, 250])
         B_hsv = cv2.inRange(vid2 , B_low ,B_high)
         B_col = cv2.bitwise_and(frame , frame , mask = B_hsv)
         no_blue = cv2.countNonZero(B_hsv)
     
         R_low = np.array([140 ,150 ,0])
         R_high = np.array([180,  255, 255])
         R_hsv = cv2.inRange(vid2 , R_low ,R_high)
         R_col = cv2.bitwise_and(frame , frame , mask = R_hsv)
         no_red = cv2.countNonZero(R_hsv)
         
         G_low = np.array([20 ,130 ,50])
         G_high = np.array([90,  255, 255])
         G_hsv = cv2.inRange(vid2 , G_low ,G_high)
         G_col = cv2.bitwise_and(frame , frame , mask = G_hsv)
         no_green = cv2.countNonZero(G_hsv)

      
         
         
         cv2.imshow("Sanat" , frame)
      
         
         if no_blue > 20: 
             #print('The number of blue pixels is: ' + str(no_blue))
             status = 1
             status_list.append(status)
             cv2.imshow("B" , B_col)
         else:
             status = 0
             status_list.append(status)
             
         if no_green > 2000:
#             print('The number of green pixels is: ' + str(no_green))
             status = 1
             status_list.append(status)
             cv2.imshow("G" , G_col)
         else:
             status = 0
             status_list.append(status)
         if no_red >20:
 #            print('The number of red pixels is: ' + str(no_red))
             status = 1
             cv2.imshow("R" , R_col)
             status_list.append(status)
         else:
             status = 0
             status_list.append(status)
        # print("Status : "+ str(status))
         
         status_list = status_list[-4:]
         print(status_list)
         if status_list[-2] == 1 :
             print("forword")
             ser.write('1'.encode())
         if status_list[-1] == 0 and status_list[-2] == 0 and status_list[-3] == 0 and status_list[-4] == 0:
             print("Forword")
             ser.write('1'.encode())
         if status_list[-1] == 1:
             print("Stop")
             ser.write('0'.encode())
         if status_list[-3] == 1:
             print("slow")
             ser.write('3'.encode())
        #
         if cv2.waitKey(1) ==  27:
             break
        
            
     cv2.destroyAllWindows()
     cap.release()
    
     
if __name__ ==  "__main__":
    main()