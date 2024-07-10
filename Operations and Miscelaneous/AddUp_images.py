#SUMAR IMAGENES
import numpy as np
import cv2

ima_1 = cv2.imread("Imagen_1.jpg")
ima_1_res = cv2.resize(ima_1,(500,500))
ima_2 = cv2.imread("imagen_2.jpg")
ima_2_res = cv2.resize(ima_2,(500,500))
M , N , L = ima_1_res.shape

alfa = 0.5
beta = 0.5
ImagenSuma = np.zeros((M,N,L), np.uint8)
for M2 in range(M):
    for N2 in range(N):
        for L2 in range(L):
            #valor = alfa * ima_1_res[M2, N2, L2] + beta * ima_2_res[M2, N2, L2]
            #valor = (ima_1_res[M2,N2,L2]+ima_2_res[M2,N2,L2])*alfa
            valor = ima_1_res[M2, N2, L2]/2 + ima_2_res[M2, N2, L2]/2
            if valor > 255:
                valor = 255
            else:
                int(valor)
            ImagenSuma[M2,N2,L2] = valor

cv2.imshow("ImagenSumada", ImagenSuma)
cv2.waitKey(0) #Espera una tecla
cv2.destroyAllWindows() #Finaliza procesos"""