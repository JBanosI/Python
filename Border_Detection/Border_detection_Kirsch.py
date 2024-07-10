#Deteccion de bordes Kirsch
import numpy as np
import cv2
import math

ima_1 = cv2.imread("b.jpg")
ima_1_res = cv2.resize(ima_1,(500,500))
ima_1_res = np.array(ima_1_res , dtype= float)
M , N , L = ima_1_res.shape

E_D_G = np.zeros((M,N), dtype= float)
for M2 in range(0,M,1):
    for N2 in range(0,N,1):
        valor_pixel = int((ima_1_res[M2, N2, 2] * 0.299) + (ima_1_res[M2, N2, 1] * 0.587) + (ima_1_res[M2, N2, 0] * 0.114))
        E_D_G[M2,N2] = valor_pixel

#----------0° X------------
B_0 = np.zeros((M,N),np.uint8)
for M2 in range(1, M-1):
    for N2 in range(1, N-1):
        border = int(-3*E_D_G[M2-1,N2-1] - 3*E_D_G[M2-1,N2] + 5*E_D_G[M2-1,N2+1] - 3*E_D_G[M2,N2-1] + 5*E_D_G[M2,N2+1] - 3*E_D_G[M2+1,N2-1] - 3*E_D_G[M2+1,N2] + 5*E_D_G[M2+1,N2+1])
        if(border < 0):
            B_0[M2, N2] = 0
        else:
            B_0[M2, N2] = border

#----------45° X------------
B_45 = np.zeros((M,N),np.uint8)
for M2 in range(1, M-1):
    for N2 in range(1, N-1):
        border = int(-3*E_D_G[M2-1,N2-1] + 5*E_D_G[M2-1,N2] + 5*E_D_G[M2-1,N2+1] - 3*E_D_G[M2,N2-1] + 5*E_D_G[M2,N2+1] - 3*E_D_G[M2+1,N2-1] - 3*E_D_G[M2+1,N2] - 3*E_D_G[M2+1,N2+1])
        if(border < 0):
            B_45[M2, N2] = 0
        else:
            B_45[M2, N2] = border

#----------90° X------------
B_90 = np.zeros((M,N),np.uint8)
for M2 in range(1, M-1):
    for N2 in range(1, N-1):
        border = int(5*E_D_G[M2-1,N2-1] + 5*E_D_G[M2-1,N2] + 5*E_D_G[M2-1,N2+1] - 3*E_D_G[M2,N2-1] - 3*E_D_G[M2,N2+1] - 3*E_D_G[M2+1,N2-1] - 3*E_D_G[M2+1,N2] - 3*E_D_G[M2+1,N2+1])
        if(border < 0):
            B_90[M2, N2] = 0
        else:
            B_90[M2, N2] = border

#----------135° X------------
B_135 = np.zeros((M,N),np.uint8)
for M2 in range(1, M-1):
    for N2 in range(1, N-1):
        border = int(5*E_D_G[M2-1,N2-1] + 5*E_D_G[M2-1,N2] - 3*E_D_G[M2-1,N2+1] + 5*E_D_G[M2,N2-1] - 3*E_D_G[M2,N2+1] - 3*E_D_G[M2+1,N2-1] - 3*E_D_G[M2+1,N2] - 3*E_D_G[M2+1,N2+1])
        if(border < 0):
            B_135[M2, N2] = 0
        else:
            B_135[M2, N2] = border

#----------180° X------------
B_180 = np.zeros((M,N),np.uint8)
for M2 in range(1, M-1):
    for N2 in range(1, N-1):
        border = int(5*E_D_G[M2-1,N2-1] - 3*E_D_G[M2-1,N2] - 3*E_D_G[M2-1,N2+1] + 5*E_D_G[M2,N2-1] - 3*E_D_G[M2,N2+1] + 5*E_D_G[M2+1,N2-1] - 3*E_D_G[M2+1,N2] - 3*E_D_G[M2+1,N2+1])
        if(border < 0):
            B_180[M2, N2] = 0
        else:
            B_180[M2, N2] = border

#----------225° X------------
B_225 = np.zeros((M,N),np.uint8)
for M2 in range(1, M-1):
    for N2 in range(1, N-1):
        border = int(-3*E_D_G[M2-1,N2-1] - 3*E_D_G[M2-1,N2] - 3*E_D_G[M2-1,N2+1] + 5*E_D_G[M2,N2-1] - 3*E_D_G[M2,N2+1] + 5*E_D_G[M2+1,N2-1] + 5*E_D_G[M2+1,N2] - 3*E_D_G[M2+1,N2+1])
        if(border < 0):
            B_225[M2, N2] = 0
        else:
            B_225[M2, N2] = border

#----------270° X------------
B_270 = np.zeros((M,N),np.uint8)
for M2 in range(1, M-1):
    for N2 in range(1, N-1):
        border = int(-3*E_D_G[M2-1,N2-1] - 3*E_D_G[M2-1,N2] - 3*E_D_G[M2-1,N2+1] - 3*E_D_G[M2,N2-1] - 3*E_D_G[M2,N2+1] + 5*E_D_G[M2+1,N2-1] + 5*E_D_G[M2+1,N2] + 5*E_D_G[M2+1,N2+1])
        if(border < 0):
            B_270[M2, N2] = 0
        else:
            B_270[M2, N2] = border

#----------315° X------------
B_315 = np.zeros((M,N),np.uint8)
for M2 in range(1, M-1):
    for N2 in range(1, N-1):
        border = int(-3*E_D_G[M2-1,N2-1] - 3*E_D_G[M2-1,N2] - 3*E_D_G[M2-1,N2+1] - 3*E_D_G[M2,N2-1] + 5*E_D_G[M2,N2+1] - 3*E_D_G[M2+1,N2-1] + 5*E_D_G[M2+1,N2] + 5*E_D_G[M2+1,N2+1])
        if(border < 0):
            B_315[M2, N2] = 0
        else:
            B_315[M2, N2] = border

cv2.imshow('Bordes_0', B_0)
cv2.waitKey(0) #Espera una tecla
cv2.imwrite("kirsch_0.jpg",B_0)
cv2.imshow('Bordes_45', B_45)
cv2.waitKey(0) #Espera una tecla
cv2.imwrite("kirsch_45.jpg",B_45)
cv2.imshow('Bordes_90', B_90)
cv2.waitKey(0) #Espera una tecla
cv2.imwrite("kirsch_90.jpg",B_90)
cv2.imshow('Bordes_135', B_135)
cv2.waitKey(0) #Espera una tecla
cv2.imwrite("kirsch_135.jpg",B_135)
cv2.imshow('Bordes_180', B_180)
cv2.waitKey(0) #Espera una tecla
cv2.imwrite("kirsch_180.jpg",B_180)
cv2.imshow('Bordes_225', B_225)
cv2.waitKey(0) #Espera una tecla
cv2.imwrite("kirsch_225.jpg",B_225)
cv2.imshow('Bordes_270', B_270)
cv2.waitKey(0) #Espera una tecla
cv2.imwrite("kirsch_270.jpg",B_270)
cv2.imshow('Bordes_315', B_315)
cv2.waitKey(0) #Espera una tecla
cv2.imwrite("kirsch_315.jpg",B_315)
cv2.destroyAllWindows() #Finaliza procesos"""