#HSI
import numpy as np
import cv2

ima_1 = cv2.imread("1.jpg")
ima_1_res = cv2.resize(ima_1, (500, 500))
M, N, L = ima_1_res.shape
ima_1_res = ima_1_res.astype(float)

I = np.zeros((M, N), dtype=np.uint8)
for M2 in range(M):
    for N2 in range(N):
        suma = ima_1_res[M2, N2, 0] + ima_1_res[M2, N2, 1] + ima_1_res[M2, N2, 2]
        I[M2, N2] = int(suma / 3)

S = np.zeros((M, N), dtype=np.uint8)
for M2 in range(M):
    for N2 in range(N):
        suma = ima_1_res[M2, N2, 0] + ima_1_res[M2, N2, 1] + ima_1_res[M2, N2, 2]
        num = 1 - (3 / suma)
        S[M2, N2] = int(num * 255)

H = np.zeros((M, N), dtype=np.uint8)
for M2 in range(M):
    for N2 in range(N):
        suma_rgb = ima_1_res[M2, N2, 2] + ima_1_res[M2, N2, 1] + ima_1_res[M2, N2, 0]
        num = 0.5 * ((ima_1_res[M2, N2, 2] - ima_1_res[M2, N2, 1]) + (ima_1_res[M2, N2, 2] - ima_1_res[M2, N2, 0]))
        denom = np.sqrt((ima_1_res[M2, N2, 2] - ima_1_res[M2, N2, 1])**2 + (ima_1_res[M2, N2, 2] - ima_1_res[M2, N2, 0]) * (ima_1_res[M2, N2, 1] - ima_1_res[M2, N2, 0]))
        if denom != 0:
            angulo = np.arccos(num / denom)
            H[M2, N2] = int((np.degrees(angulo) + 360) % 360)
        else:
            H[M2, N2] = 0

V = np.max(ima_1_res, axis=2).astype(np.uint8)

cv2.imshow('I', I)
cv2.waitKey(0)
cv2.imwrite("I.jpg",I)
cv2.imshow('S', S)
cv2.waitKey(0)
cv2.imwrite("S.jpg",S)
cv2.imshow('H', H)
cv2.waitKey(0)
cv2.imwrite("H.jpg",H)
cv2.imshow('V', V)
cv2.waitKey(0)
cv2.imwrite("V.jpg",V)
cv2.destroyAllWindows()
