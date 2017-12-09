import numpy as np
import cv2

Iin1 = cv2.imread('lulu1.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('cameraman', Iin1)


d1,d2 = Iin1.shape
print(d1,d2)

Iout1 = Iin1[::2,::2]
print Iout1.size

cv2.imshow("output1", Iout1)

Iout2 = np.zeros([d1, d2], np.uint8)

for i in range(d1/2):
    for j in range(d2/2):
        k = 2*i
        m = 2*j
        num = Iout1[i, j]
        Iout2[k, m] = num
        Iout2[k, m+1] = num
        Iout2[k+1, m] = num
        Iout2[k + 1, m+1] = num

# print Iout2.size

cv2.imshow("output2", Iout2)

cv2.waitKey(0)

print 'destroy all windows'
cv2.destroyAllWindows()