import numpy as np
import cv2

img = np.zeros((600,600,3), np.uint8)
[M, N, L] = img.shape #Tamaño de imagen M, N y L para eje z
cv2.line(img,(0,N//2),(M,N//2),(255,255,255),2) #line(matriz, inicio linea, final linea, color, grosor)
cv2.line(img,(M//2,0),(M//2,N),(255,255,255),2) 
cv2.rectangle(img,((M//2)-50,(N//2)-50),((M//2)+50,(N//2)+50),(255,255,255),2)
cv2.circle(img, (M//2,N//2),50,(255,255,255),2) #Para que aparezca relleno se pasa -1 en el ultimo
font = cv2.FONT_HERSHEY_COMPLEX #Textos
cv2.putText(img,"JESUS ALBERTO",(M//2-70,N//2+75),font,0.6,(255,255,255)) #puttext(img, str, posicion, fuente, tamaño, color)
cv2.putText(img,"BANOS ISLAS",(M//2-65,N//2+100),font,0.6,(255,255,255))
cv2.imshow('Imagen',img) #Muestra la imagen
cv2.waitKey(0) #Espera una tecla
cv2.destroyAllWindows() #Finaliza procesos