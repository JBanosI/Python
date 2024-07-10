#Promedio de pixeles
import numpy as np
import cv2

ima_1 = cv2.imread("1.jpg")
ima_1_res = cv2.resize(ima_1,(500,500))
ima_1_res = np.array(ima_1_res , dtype= float)
M , N , L = ima_1_res.shape


#---------Promedio---------------------
B = np.zeros((M,N),np.uint8)
for M2 in range(1, M-2):
    for N2 in range(1, N-2):
        prom = int(E_D_G[M2-1, N2-1] + E_D_G[M2-1, N2] + E_D_G[M2-1, N2+1] + E_D_G[M2, N2-1] + E_D_G[M2, N2] + E_D_G[M2, N2+1]  + E_D_G[M2+1, N2] + E_D_G[M2+1, N2] + E_D_G[M2+1, N2+1])/9 
        B[M2, N2] = prom

cv2.imshow('otro_2', B)
cv2.waitKey(0) #Espera una tecla
cv2.destroyAllWindows() #Finaliza procesos"""