#Inverso o Negativo
import numpy as np
import cv2

ima_1 = cv2.imread("dos.jpg")
ima_1_res = cv2.resize(ima_1,(500,500))
#ima_1_res = np.array(ima_1_res , dtype= float)
M , N , L = ima_1_res.shape

Identidad = np.zeros((M,N,L), np.uint8)
for M2 in range(M):
     for N2 in range(N):
            for L2 in range(L):
                Identidad[M2,N2,L2] = 255 - ima_1_res[M2,N2,L2]
          
cv2.imshow("Identidad", Identidad)
cv2.waitKey(0) #Espera una tecla
cv2.imwrite("Inverso.jpg", Identidad)
cv2.destroyAllWindows() #Finaliza procesos"""