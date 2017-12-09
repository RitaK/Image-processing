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

img = cv2.imread('lo.bmp', cv2.IMREAD_GRAYSCALE)
cv2.imwrite('lo.tiff', img)


cv2.waitKey(0)

print 'destroy all windows'
cv2.destroyAllWindows()


