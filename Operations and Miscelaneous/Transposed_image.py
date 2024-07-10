#Imagen transpuesta
import cv2
import numpy as np

A = cv2.imread("1.jpg")
res = cv2.resize(A,(500,500)) #rezise(imagen, tamaño)

cv2.imshow("ImagenOriginal",res)
cv2.waitKey(0) #Espera una tecla

M , N, L = res.shape
B = np.zeros((M , N , L),np.uint8)
for M2 in range(M):
        for N2 in range(N):
             B[N2,M2] = res[M2,N2]

cv2.imshow("ImagenTranspuesta", B)
cv2.waitKey(0) #Espera una tecla
cv2.imwrite('trans.jpg', B)
cv2.destroyAllWindows() #Finaliza procesos