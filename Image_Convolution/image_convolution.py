import numpy as np
import cv2
import scipy.signal as sci

A = cv2.imread("uno.jpg")
A = cv2.resize(A, (700, 500))
M, N, L = A.shape

FC = np.zeros((M, N), np.uint8)

for M2 in range(M):
    for N2 in range(N):
        valor_pixel = int((A[M2, N2, 2] * 0.299) + (A[M2, N2, 1] * 0.587) + (A[M2, N2, 0] * 0.114))
        FC[M2, N2] = valor_pixel

g = np.ones((11, 11), np.float32) / 121 

B = sci.convolve2d(FC.astype(np.float32), g, mode='same', boundary='wrap')  

B = cv2.normalize(B, None, 0, 255, cv2.NORM_MINMAX)
B = B.astype(np.uint8)

cv2.imshow("Original", FC)
cv2.imshow("Convolucion", B)
cv2.waitKey(0)
cv2.destroyAllWindows()