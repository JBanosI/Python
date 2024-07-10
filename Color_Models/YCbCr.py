#YCbCr
import numpy as np
import cv2

ima_1 = cv2.imread("1.jpg")
ima_1_res = cv2.resize(ima_1,(500,500))
M , N , L = ima_1_res.shape

Y = np.zeros((M, N), np.uint8)
for M2 in range(M):
     for N2 in range(N):
          valor_pixel = int((ima_1_res[M2, N2, 2] * 0.299) + (ima_1_res[M2, N2, 1] * 0.587) + (ima_1_res[M2, N2, 0] * 0.114))
          Y[M2,N2] = valor_pixel

Cb = np.zeros((M, N), np.uint8)
for M2 in range(M):
     for N2 in range(N):
        valor_pixel = int(-(0.169 * ima_1_res[M2, N2, 2]) - (0.331 * ima_1_res[M2, N2, 1]) + (0.499 * ima_1_res[M2, N2, 0]))
        if(valor_pixel < 0):
            Cb[M2,N2] = 0
        else:
            Cb[M2,N2] = valor_pixel
            
Cr = np.zeros((M, N), np.uint8)
for M2 in range(M):
     for N2 in range(N):
        valor_pixel = int((0.449 * ima_1_res[M2, N2, 2]) - (0.418 * ima_1_res[M2, N2, 1]) - (0.0813 * ima_1_res[M2, N2, 0]))
        if(valor_pixel < 0):
            Cr[M2,N2] = 0
        else:
            Cr[M2,N2] = valor_pixel

cv2.imshow("Y", Y)
cv2.waitKey(0)
cv2.imwrite("Y2.jpg",Y)
cv2.imshow("Cb", Cb)
cv2.waitKey(0)
cv2.imwrite("Cb.jpg",Cb)
cv2.imshow("Cr", Cr)
cv2.waitKey(0)
cv2.imwrite("Cr.jpg",Cr)
cv2.destroyAllWindows()