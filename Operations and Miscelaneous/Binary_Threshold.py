#Umbral Binario
import numpy as np
import cv2
import matplotlib.pyplot as plot

ima_1 = cv2.imread("1.jpg")
ima_1_res = cv2.resize(ima_1,(500,500))
ima_1_res = np.array(ima_1_res , dtype= float)
M , N , L = ima_1_res.shape

#-------Umbral 255 si A<P1 & A>=P2------------------
umbral_pos = np.zeros((M,N), np.uint8)
conteo_1 = [0] * 256
for M2 in range(0,M,1):
    for N2 in range(0,N,1):
        valor_pixel = int((ima_1_res[M2, N2, 2] * 0.299) + (ima_1_res[M2, N2, 1] * 0.587) + (ima_1_res[M2, N2, 0] * 0.114))
        umbral_pos[M2,N2] = valor_pixel
        if(valor_pixel < 50) or (valor_pixel>=130):
            umbral_pos[M2,N2] = 255
            conteo_1[valor_pixel] += 1
#------------Graficar el umbral anterior-----------------
print(conteo_1)
fig, ax = plot.subplots()
ax.set(title= "255 si A<P1 & A>=P2")
ax.stem(conteo_1)
plot.show()


#++++++++++++Umbral 0 si A>P1 & A<P2+++++++++++++++++
umbral_neg = np.zeros((M,N), np.uint8)
conteo_2 = [0] * 256
for M2 in range(0,M,1):
    for N2 in range(0,N,1):
        valor_pixel = int((ima_1_res[M2, N2, 2] * 0.299) + (ima_1_res[M2, N2, 1] * 0.587) + (ima_1_res[M2, N2, 0] * 0.114))
        umbral_neg[M2,N2] = valor_pixel
        if(valor_pixel > 50) and (valor_pixel<130):
            umbral_neg[M2,N2] = 0
            conteo_2[valor_pixel] += 1
#++++++++++++Graficar el umbral anterior+++++++++++++++
print(conteo_2)
fig, ax = plot.subplots()
ax.set(title= "0 si A>P1 & A<P2")
ax.stem(conteo_2)
plot.show()


cv2.imshow("Umbral_1", umbral_pos)
cv2.waitKey(0) #Espera una tecla
cv2.imshow("Umbral_2", umbral_neg)
cv2.waitKey(0) #Espera una tecla
cv2.imwrite("Umbral_neg.jpg",umbral_neg)
cv2.destroyAllWindows() #Finaliza procesos