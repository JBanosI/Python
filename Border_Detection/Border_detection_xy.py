#Deteccion de bordes (X e Y)
import numpy as np
import cv2

ima_1 = cv2.imread("uno.jpg")
ima_1_res = cv2.resize(ima_1,(500,500))
ima_1_res = np.array(ima_1_res , dtype= float)
M , N , L = ima_1_res.shape

E_D_G = np.zeros((M,N), dtype= float)
for M2 in range(0,M,1):
    for N2 in range(0,N,1):
        valor_pixel = int((ima_1_res[M2, N2, 2] * 0.299) + (ima_1_res[M2, N2, 1] * 0.587) + (ima_1_res[M2, N2, 0] * 0.114))
        E_D_G[M2,N2] = valor_pixel


B_X_Y = np.zeros((M,N),np.uint8)
for M2 in range(1, M-1):
    for N2 in range(1, N-1):
        border = int(E_D_G[M2-1,N2] + E_D_G[M2,N2-1] - 4*E_D_G[M2,N2] + E_D_G[M2,N2+1] + E_D_G[M2+1,N2])
        if(border < 0):
            B_X_Y[M2, N2] = 0
        else:
            B_X_Y[M2, N2] = border


cv2.imshow('Bordes_X_Y', B_X_Y)
cv2.waitKey(0) #Espera una tecla
cv2.imwrite("Bordes_x_y.jpg",B_X_Y)
cv2.destroyAllWindows() #Finaliza procesos"""