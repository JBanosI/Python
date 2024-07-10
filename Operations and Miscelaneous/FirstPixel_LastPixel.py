#TEST PRIMER PIXEL- ULTIMO PIXEL
import cv2
import numpy as np
A = cv2.imread("1.jpg")
res = cv2.resize(A,(500,500)) #rezise(imagen, tamaño
M , N, L = res.shape
cv2.imshow("imagen",res)
cv2.waitKey(0) #Espera una tecla
B = np.zeros((M , N , L),np.uint8)
for N2 in range(N-1, 0, -1):
    for M2 in range(M-1, 0, -1):
        B[M-M2,N-N2] = res[M2,N2]
cv2.imshow("imagen2", B)
cv2.waitKey(0) #Espera una tecla
cv2.destroyAllWindows() #Finaliza procesos"""