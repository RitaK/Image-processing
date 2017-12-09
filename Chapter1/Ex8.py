import numpy as np
import cv2

#floy-steinberg

Iin1 = cv2.imread('lulu1.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('lulu', Iin1)


d1,d2 = Iin1.shape
print(d1,d2)


# Iout1 = np.zeros([d1, d2], np.uint8)

for i in range(d1):
    for j in range(d2):
        if 0 < i < d1-1 and 0 < j < d2-1:
            oldpixel = Iin1[i,j]
            newpixel = (Iin1[i,j] > 100).astype(int)
            if newpixel == 1:
                newpixel = 255
            Iin1[i,j] = newpixel
            quant_error = oldpixel - newpixel
            Iin1[i+1, j] = Iin1[i+1, j] + quant_error * 3 / 8
            Iin1[i, j+1] = Iin1[i, j+1] + quant_error * 3 / 8
            Iin1[i + 1, j+1] = Iin1[i + 1, j+1] + quant_error * 1/4


# print Iout2.size
Iin1 = Iin1.astype(np.uint8)
print Iin1
cv2.imshow("output1", Iin1)

cv2.waitKey(0)

print 'destroy all windows'
cv2.destroyAllWindows()