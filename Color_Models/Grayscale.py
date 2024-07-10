#Escala de grises
import numpy as np
import cv2

ima_1 = cv2.imread("1.jpg")
ima_1_res = cv2.resize(ima_1,(500,500))
M , N , L = ima_1_res.shape

E_D_G = np.zeros((M, N), np.uint8)
for M2 in range(M):
     for N2 in range(N):
          valor_pixel = int((ima_1_res[M2, N2, 2] * 0.299) + (ima_1_res[M2, N2, 1] * 0.587) + (ima_1_res[M2, N2, 0] * 0.114))
          E_D_G[M2,N2] = valor_pixel

cv2.imshow("E_D_G", E_D_G)
cv2.waitKey(0)
cv2.destroyAllWindows()