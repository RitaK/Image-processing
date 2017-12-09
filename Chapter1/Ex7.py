import numpy as np
import cv2

# half-toning. 4 bits instead of every 1
Iin1 = cv2.imread('lulu1.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('kidface', Iin1)


d1,d2 = Iin1.shape
print(d1,d2)


Iout2 = np.zeros([d1*2, d2*2], np.uint8)

for i in range(d1):
    for j in range(d2):
        k = 2*i
        m = 2*j
        num = Iin1[i, j]
        if 51 <=num <= 101:
            Iout2[k + 1, m] = 255
        else:
            if 102 <= num <= 152:
                Iout2[k+1, m] =255
                Iout2[k, m+1] = 255
            else:
                if 153 <= num <= 203:
                    Iout2[k+1, m+1] = 255
                    Iout2[k, m+1] = 255
                    Iout2[k+1, m] = 255
                else:
                    if 204 <= num <= 255:
                        Iout2[k, m] = 255
                        Iout2[k+1, m+1] = 255
                        Iout2[k+1, m] = 255
                        Iout2[k, m+1] = 255




# print Iout2.size

cv2.imshow("output2", Iout2)

cv2.waitKey(0)

print 'destroy all windows'
cv2.destroyAllWindows()