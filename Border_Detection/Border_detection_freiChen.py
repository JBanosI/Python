#Deteccion de bordes FREI-CHEN
import numpy as np
import cv2
import math

ima_1 = cv2.imread("uno.jpg")
ima_1_res = cv2.resize(ima_1,(500,500))
ima_1_res = np.array(ima_1_res , dtype= float)
M , N , L = ima_1_res.shape

E_D_G = np.zeros((M,N), dtype= float)
for M2 in range(0,M,1):
    for N2 in range(0,N,1):
        valor_pixel = int((ima_1_res[M2, N2, 2] * 0.299) + (ima_1_res[M2, N2, 1] * 0.587) + (ima_1_res[M2, N2, 0] * 0.114))
        E_D_G[M2,N2] = valor_pixel

#----------F1------------
B_F1 = np.zeros((M,N),np.uint8)
for M2 in range(1, M-1):
    for N2 in range(1, N-1):
        border = int((1/(2*math.sqrt(2)))*(E_D_G[M2-1,N2-1] + math.sqrt(2)*E_D_G[M2-1,N2] + E_D_G[M2-1,N2+1] - E_D_G[M2+1,N2-1] - math.sqrt(2)*E_D_G[M2+1,N2] - E_D_G[M2+1,N2+1]))
        if(border < 0):
            B_F1[M2, N2] = 0
        else:
            B_F1[M2, N2] = border

#----------F2------------
B_F2 = np.zeros((M,N),np.uint8)
for M2 in range(1, M-1):
    for N2 in range(1, N-1):
        border = int((1/(2*math.sqrt(2)))*(E_D_G[M2-1,N2-1] - E_D_G[M2-1,N2+1] + math.sqrt(2)*E_D_G[M2,N2-1] - math.sqrt(2)*E_D_G[M2,N2+1] + E_D_G[M2+1,N2-1] - E_D_G[M2+1,N2+1]))
        if(border < 0):
            B_F2[M2, N2] = 0
        else:
            B_F2[M2, N2] = border

#----------F3------------
B_F3 = np.zeros((M,N),np.uint8)
for M2 in range(1, M-1):
    for N2 in range(1, N-1):
        border = int((1/(2*math.sqrt(2)))*(-E_D_G[M2-1,N2] - math.sqrt(2)*E_D_G[M2-1,N2+1] + E_D_G[M2,N2-1] - E_D_G[M2,N2+1] + math.sqrt(2)*E_D_G[M2+1,N2-1] + E_D_G[M2+1,N2]))
        if(border < 0):
            B_F3[M2, N2] = 0
        else:
            B_F3[M2, N2] = border

#----------F4------------
B_F4 = np.zeros((M,N),np.uint8)
for M2 in range(1, M-1):
    for N2 in range(1, N-1):
        border = int((1/(2*math.sqrt(2)))*(math.sqrt(2)*E_D_G[M2-1,N2-1] - E_D_G[M2-1,N2] - E_D_G[M2,N2-1] + E_D_G[M2,N2+1] + E_D_G[M2+1,N2] - math.sqrt(2)*E_D_G[M2+1,N2+1]))
        if(border < 0):
            B_F4[M2, N2] = 0
        else:
            B_F4[M2, N2] = border

#----------F5------------
B_F5 = np.zeros((M,N),np.uint8)
for M2 in range(1, M-1):
    for N2 in range(1, N-1):
        border = int(0.5*(E_D_G[M2-1,N2] - E_D_G[M2,N2-1] - E_D_G[M2,N2+1] + E_D_G[M2+1,N2]))
        if(border < 0):
            B_F5[M2, N2] = 0
        else:
            B_F5[M2, N2] = border


cv2.imshow('Bordes_F1', B_F1)
cv2.waitKey(0) #Espera una tecla
cv2.imwrite("freichen_1.jpg",B_F1)
cv2.imshow('Bordes_F2', B_F2)
cv2.waitKey(0) #Espera una tecla
cv2.imwrite("freichen_2.jpg",B_F2)
cv2.imshow('Bordes_F3', B_F3)
cv2.waitKey(0) #Espera una tecla
cv2.imwrite("freichen_3.jpg",B_F3)
cv2.imshow('Bordes_F4', B_F4)
cv2.waitKey(0) #Espera una tecla
cv2.imwrite("freichen_4.jpg",B_F4)
cv2.imshow('Bordes_F5', B_F5)
cv2.waitKey(0) #Espera una tecla
cv2.imwrite("freichen_5.jpg",B_F5)
cv2.destroyAllWindows() #Finaliza procesos"""