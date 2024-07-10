#Derivada B[M,N] = A[M+1,N]-A[M,N]
import numpy as np
import cv2
import matplotlib.pyplot as plot

ima_1 = cv2.imread("uno.jpg")
ima_1_res = cv2.resize(ima_1,(500,500))
ima_1_res = np.array(ima_1_res , dtype= float)
M , N , L = ima_1_res.shape

A = np.zeros((M,N), np.uint8)
for M2 in range(0,M,1):
    for N2 in range(0,N,1):
        valor_pixel = int((ima_1_res[M2, N2, 2] * 0.299) + (ima_1_res[M2, N2, 1] * 0.587) + (ima_1_res[M2, N2, 0] * 0.114))
        A[M2,N2] = valor_pixel

derivada_x = np.zeros((M,N), np.uint8)
#derivada = np.array(derivada , dtype= float)
for M2 in range(M):
    for N2 in range(N):
        if(M2+1 < M):
            valor_1 = A[M2+1,N2]
            valor_2 = A[M2,N2]
            resta = valor_1 - valor_2
            if(valor_2 > valor_1):
                derivada_x[M2,N2] = 0
            else:
                derivada_x[M2,N2] = resta

derivada_y = np.zeros((M,N), np.uint8)
#derivada = np.array(derivada , dtype= float)
for M2 in range(M):
    for N2 in range(N):
        if(N2+1 < N):
            valor_1 = A[M2,N2+1]
            valor_2 = A[M2,N2]
            resta = valor_1 - valor_2
            if(valor_2 > valor_1):
                derivada_y[M2,N2] = 0
            else:
                derivada_y[M2,N2] = resta
                
        

cv2.imshow("DERIVADA", derivada_x)
cv2.waitKey(0) #Espera una tecla
cv2.imwrite("der_1y.jpg",derivada_y)
cv2.imshow("DERIVADA_y", derivada_y)
cv2.waitKey(0) #Espera una tecla
cv2.destroyAllWindows() #Finaliza procesos