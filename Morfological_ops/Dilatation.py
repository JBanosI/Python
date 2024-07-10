#Dilatacion
import numpy as np
import cv2
import matplotlib.pyplot as plot

ima_1 = cv2.imread("1.jpg",0)
ima_1_res = cv2.resize(ima_1,(500,500))
M , N = ima_1_res.shape
cv2.imshow("E_d_g",ima_1_res)
cv2.waitKey(0) #Espera una tecla

ee = np.ones((21,21),np.uint8)
dilatacion = cv2.dilate(ima_1_res,ee,iterations=1)
cv2.imshow("Dilatacion",dilatacion)
cv2.waitKey(0) #Espera una tecla

conteo = [0] * 256
umbral = np.zeros((M,N), np.uint8)
for M2 in range(M):
     for N2 in range(N):
        valor_pixel = int(dilatacion[M2,N2])
        if(valor_pixel >=130) and (valor_pixel <= 160):
            umbral[M2, N2] = valor_pixel
        else:
            umbral[M2, N2] = 0
        conteo[valor_pixel] += 1

print(conteo)
fig, ax = plot.subplots()
#ax.hist(conteo)
ax.stem(conteo)
plot.show()

cv2.imshow("umberal",umbral)
cv2.waitKey(0) #Espera una tecla
cv2.destroyAllWindows() #Finaliza procesos"""