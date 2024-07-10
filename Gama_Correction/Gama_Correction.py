#RESALTARA
import numpy as np
import cv2
import math
import matplotlib.pyplot as plot

ima_1 = cv2.imread("uno.jpg")
ima_1_res = cv2.resize(ima_1,(500,500))
ima_1_res = np.array(ima_1_res , dtype= float)
M , N , L = ima_1_res.shape

conteo = [0] * 256
E_D_G = np.zeros((M, N), np.uint8)
for M2 in range(M):
     for N2 in range(N):
          valor_pixel = int((ima_1_res[M2, N2, 2] * 0.299) + (ima_1_res[M2, N2, 1] * 0.587) + (ima_1_res[M2, N2, 0] * 0.114))
          E_D_G[M2, N2] = valor_pixel
          conteo[valor_pixel] += 1
          
print(conteo)
fig, ax = plot.subplots()
#ax.hist(conteo)
ax.stem(conteo)
plot.show()




#Cuantas veces se repiten los valores del 0 al 255 en la imagen

Nueva = np.zeros((M,N), np.uint8)
Nueva = np.array(Nueva , dtype= float)
for M2 in range(M):
     for N2 in range(N):
          Nueva[M2,N2] = ((E_D_G[M2,N2]/255)**5)*255 #Funcion Gama


cv2.imshow("E_D_G", E_D_G)
cv2.waitKey(0) #Espera una tecla
cv2.imshow("Nueva", Nueva)
cv2.waitKey(0) #Espera una tecla
cv2.imwrite("gamma5.jpg",Nueva)
cv2.destroyAllWindows() #Finaliza procesos