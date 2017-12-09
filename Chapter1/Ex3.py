import numpy as np
import cv2
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def mesh(pic):
    xx2, yy2 = np.mgrid[0:pic.shape[0], 0:pic.shape[1]]
    # create the figure
    fig2 = plt.figure()
    ax2 = fig2.gca(projection='3d')
    ax2.plot_surface(xx2, yy2, pic, rstride=1, cstride=1, cmap=plt.cm.gray,
                     linewidth=0)


def negative(I):
    d1, d2 = I.shape
    print(d1, d2)

    smooth_i = np.zeros([d1, d2], np.uint8)
    I2 = np.array(np.round(I), dtype=np.float)

    for i in range(d1):
        for j in range(d2):
            smooth_i[i, j] =255 - I[i,j]
    return smooth_i

I = cv2.imread('rsz_1rsz_lulu1.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('Lulu', I)

mesh(I)

# show it
plt.draw()

negPic = negative(I)

cv2.imshow("smooth lulu", negPic)

mesh(negPic)

# show it
plt.show()
cv2.waitKey(0)

print 'destroy all windows'
cv2.destroyAllWindows()


