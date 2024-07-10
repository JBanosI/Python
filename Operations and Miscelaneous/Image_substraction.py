#Resta de imagenes
import numpy as np
import cv2

ima_1 = cv2.imread("1.jpg")
ima_1 = np.array(ima_1, dtype=float)

ima_2 = cv2.imread("2.jpg")
ima_2 = np.array(ima_2, dtype=float)

M, N, L = ima_1.shape
ImagenRestada = np.zeros((M, N, L), np.uint8)

for M2 in range(M):
    for N2 in range(N):
        for L2 in range(L):
            valor_resta = ima_1[M2, N2, L2] - ima_2[M2, N2, L2]
            if valor_resta < 0:
                valor_resta = 0
            elif valor_resta > 255:
                valor_resta = 255
            
            ImagenRestada[M2, N2, L2] = valor_resta

cv2.imshow("ImagenRestada", ImagenRestada)
cv2.waitKey(0)  # Espera una tecla
cv2.imwrite('res_res.jpg', ImagenRestada)
cv2.destroyAllWindows()  # Finaliza procesos