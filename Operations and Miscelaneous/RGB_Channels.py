#Imagene separada en canal RGB
import numpy as np
import cv2

ima_1 = cv2.imread("1.jpg")
ima_1_res = cv2.resize(ima_1,(500,500))
M , N , L = ima_1_res.shape

R = np.zeros((M , N , L),np.uint8)
for M2 in range(M):
    for N2 in range(N):
            R[M2,N2,2] = ima_1_res[M2,N2,2]

G = np.zeros((M , N , L),np.uint8)
for M2 in range(M):
    for N2 in range(N):
            G[M2,N2,1] = ima_1_res[M2,N2,2]

B = np.zeros((M , N , L),np.uint8)
for M2 in range(M):
    for N2 in range(N):
        B[M2,N2,0] = ima_1_res[M2,N2,2]

cv2.imshow("Canal R", R)
cv2.waitKey(0) #Espera una tecla
cv2.imshow("Canal G", G)
cv2.waitKey(0) #Espera una tecla
cv2.imshow("Canal B", B)
cv2.waitKey(0) #Espera una tecla
cv2.imwrite('r.jpg', R)
cv2.imwrite('g.jpg', G)
cv2.imwrite('b.jpg', B)
cv2.destroyAllWindows() #Finaliza procesos"""