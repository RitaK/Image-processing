import numpy as np
import cv2
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def mysmooth(I):
    d1, d2 = I.shape
    print(d1, d2)

    smooth_i = np.zeros([d1, d2], np.uint8)
    I2 = np.array(np.round(I), dtype=np.float)

    for i in range(d1):
        for j in range(d2):
            if i > 0 and j > 0 and i < d1-1 and j < d2-2:
                sum = I2[i, j]+ I2[i-1, j-1] + I2[i-1, j+1] + I2[i, j-1]+ I2[i-1,j]+ I2[i, j+1]+ I2[i+1, j-1]+ I2[i+1, j] +I2[i+1, j+1]
                smooth_i[i,j] = sum/9
    return smooth_i

I = cv2.imread('rsz_1rsz_lulu1.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('Lulu', I)

xx, yy = np.mgrid[0:I.shape[0], 0:I.shape[1]]

# create the figure
fig = plt.figure()
ax = fig.gca(projection='3d')
#creating the mesh plot
ax.plot_surface(xx, yy, I ,rstride=1, cstride=1, cmap=plt.cm.gray,
        linewidth=0)

# show it
plt.draw()

Ismt = mysmooth(I)
Ismt = mysmooth(Ismt)

xx2, yy2 = np.mgrid[0:Ismt.shape[0], 0:Ismt.shape[1]]
# create the figure
fig2 = plt.figure()
ax2 = fig2.gca(projection='3d')
ax2.plot_surface(xx2, yy2, Ismt ,rstride=1, cstride=1, cmap=plt.cm.gray,
        linewidth=0)


cv2.imshow("smooth lulu", Ismt)

# show it
plt.show()
cv2.waitKey(0)

print 'destroy all windows'
cv2.destroyAllWindows()


