import numpy as np
import cv2
import matplotlib.pyplot as plot

ima_1 = cv2.imread("chicles4.jpg")
ima_1_res = cv2.resize(ima_1,(500,600))
ima_1_res = np.array(ima_1_res , dtype= float)
M , N , L = ima_1_res.shape

conteo = [0] * 256
E_D_G = np.zeros((M,N), np.uint8)
for M2 in range(M):
     for N2 in range(N):
        valor_pixel = int((ima_1_res[M2, N2, 2] * 0.299) + (ima_1_res[M2, N2, 1] * 0.587) + (ima_1_res[M2, N2, 0] * 0.114))
        if(valor_pixel >=145) and (valor_pixel <= 180):
            E_D_G[M2, N2] = valor_pixel
        else:
            E_D_G[M2, N2] = 0
        conteo[valor_pixel] += 1
          

print(conteo)
fig, ax = plot.subplots()
#ax.hist(conteo)
ax.stem(conteo)
plot.show()

cv2.imshow("Chicles", E_D_G)
cv2.waitKey(0) #Espera una tecla
cv2.destroyAllWindows() #Finaliza procesos