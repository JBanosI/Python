#CMYK
import numpy as np
import cv2

ima_1 = cv2.imread("1.jpg")
ima_1_res = cv2.resize(ima_1,(500,500))
#ima_1_res = np.array(ima_1_res , dtype= float)
M , N , L = ima_1_res.shape

#Se considera 0 = B , 1 = G y 2 = R

Magenta = np.zeros((M,N,L), np.uint8)
for M2 in range(M):
    for N2  in range(N):
        for L2 in range(0, 3 ,2):
            Magenta[M2,N2,L2] = ima_1_res[M2,N2,L2]

Cyan = np.zeros((M,N,L), np.uint8)
for M2 in range(M):
    for N2  in range(N):
        for L2 in range(0,2):
            Cyan[M2,N2,L2] = ima_1_res[M2,N2,L2]

Yellow = np.zeros((M,N,L), np.uint8)
for M2 in range(M):
    for N2  in range(N):
        for L2 in range(1,3):
            Yellow[M2,N2,L2] = ima_1_res[M2,N2,L2]
            
k = np.zeros((M,N), np.uint8)
for M2 in range(M):
    for N2  in range(N):
        k[M2,N2] = int(Cyan[M2,N2,0] + Magenta[M2,N2,1] + Yellow[M2,N2,2])


cv2.imshow('Cyan', Cyan)
cv2.waitKey(0) #Espera una tecla
cv2.imshow('Magenta', Magenta)
cv2.waitKey(0) #Espera una tecla
cv2.imshow('Yellow', Yellow)
cv2.waitKey(0) #Espera una tecla
cv2.imshow('K', k)
cv2.waitKey(0) #Espera una tecla
cv2.imwrite("K.jpg",k)
cv2.destroyAllWindows() #Finaliza procesos"""