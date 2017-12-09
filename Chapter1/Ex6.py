import numpy as np
import cv2


def thresholding(t):
    I = cv2.imread('lulu1.jpg', cv2.IMREAD_GRAYSCALE)
    print I.shape
    cv2.imshow('cameraman', I)
    binaryImg = np.zeros(I.shape , np.uint8)
    binaryImg = I > t
    return binaryImg.astype(np.uint8)


binaryPic = thresholding(160)

binaryPic[ binaryPic > 0] = 255

cv2.imshow("", binaryPic)
cv2.waitKey(0)
print 'destroy all windows'
cv2.destroyAllWindows()