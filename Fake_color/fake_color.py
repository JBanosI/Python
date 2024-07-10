import numpy as np
import cv2
import math
import matplotlib.pyplot as plot
import random

ima_1 = cv2.imread("cielo.jpeg")
ima_1_res = cv2.resize(ima_1,(500,500))
ima_1_res = np.array(ima_1_res , dtype= float)
M , N , L = ima_1_res.shape

conteo = [0] * 256
FC = np.zeros((M, N, L), np.uint8)

for M2 in range(0,M,1):
     for N2 in range(0,N,1):
          valor_pixel = int((ima_1_res[M2, N2, 2] * 0.299) + (ima_1_res[M2, N2, 1] * 0.587) + (ima_1_res[M2, N2, 0] * 0.114))
          FC[M2, N2] = valor_pixel
          #cv2.imwrite("edg_satelite.jpg",FC)
          conteo[valor_pixel] += 1
          if valor_pixel <= 40:
               FC[M2, N2] = [100, 100, 180]
          elif valor_pixel <= 80:
               FC[M2, N2] = [102, 255, 102]
          elif valor_pixel <= 120:
               FC[M2, N2] = [0, 255, 255]
          elif valor_pixel <= 160:
               FC[M2, N2] = [0, 128, 255]
          elif valor_pixel <= 240:
               FC[M2, N2] = [0, 0, 255]
          elif valor_pixel <= 255:
               FC[M2, N2] = [255, 0, 139]
          

print(conteo)
fig, ax = plot.subplots()
#ax.hist(conteo)
ax.stem(conteo)
plot.show()


cv2.imshow("Falso color", FC)
cv2.waitKey(0) #Espera una tecla
cv2.imwrite("falso_color.jpg",FC)
cv2.destroyAllWindows() #Finaliza procesos