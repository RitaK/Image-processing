import numpy as np
import cv2
import math

#Maman 13
#Exersice 1
#Author: Rita Kaufman

#The histogram function of the surrounding local neighborhood.
#In our case the neighborhood will be 3*3.
#Params: neiImg - the neighborhood that its histogram needs to be calculated
#Returns: an array that represents the histogram function.

def localHistogram(firstColHist, oldHist,  neiImg, leftCol, rightCol):
    #our histogram
    hist = np.zeros(256, int)
    #dimensions of the image
    d1, d2 = neiImg.shape

    #if this is the first column, we calculate the histogram regularly
    if firstColHist:
        for i in range (d1):
            for j in range (d2):
                intensity = neiImg[i, j]
                #increasing the number of pixels at this intensity level in our histogram
                hist[intensity] += 1
    #if this is not the first column
    else:
        for i in range (len(leftCol)):
            intensity = leftCol[i]
            #increasing the number of pixels at this intensity level in our histogram
            oldHist[intensity] -= 1

        for j in range (len(rightCol)):
            intensity = rightCol[j]
            #increasing the number of pixels at this intensity level in our histogram
            oldHist[intensity] += 1
        return oldHist

    return hist

#The function that will be used to transform each pixel color. This is an accumulation of the probabilities of each intensity level.
#The function is: for each intensity level g, it is a sum of all h(i)/N for all i= 1,....,g.
#Params: hist - a histogram that is needed for this function calculation
#Returns: an array that represents the accumulative histogram probability function, as described above. Accumulation of a density function

def accuDensities(hist):
    #our accumulative densities function
    accuDensity = np.zeros(256, int)

    for i in range (len(hist)):
        accuDensity[i] = accuDensity[i-1] + hist[i]

    return accuDensity


Iin1 = cv2.imread('embedded_squares.JPG', cv2.IMREAD_GRAYSCALE)
cv2.imshow('embedded_squares - old', Iin1)

#getting the dimensions of the old picture
d1,d2 = Iin1.shape
print(d1,d2)

#initializing the so called current histogram. We need to keep track of the last histogram we had because we are using
#a method to improve performance and trying to lessen histogram calculations
currHist = np.zeros(256, int)
#the accumulative densities function
acuDens = np.zeros(256, int)
#we need these to remember the last left column that is being erased every time we move a pixel to the right
#and the right column which is the new column we need for calculating the new histogram
leftCol = []
rightCol = []

#this will be the result image
Iout1 = np.zeros([d1, d2], np.uint8)

for i in range(d1):
    for j in range(d2):
        leftCol = []
        rightCol = []
        #if this is the first column, calculate the neighborhood histogram normally.
        if j == 0:
            #if it is the first row as well
            if i == 0:
                neighborhood = Iin1[0:2, 0: 2]
                rightCol = Iin1[0:2, 1]
            else:
                #if it is the last row
                if i == d2-1:
                    neighborhood = Iin1[i - 1: i + 1, 0: 2]
                    rightCol = Iin1[i - 1: i + 1, 1]
                else:
                    neighborhood = Iin1[i-1: i+2, 0: 2]
                    rightCol = Iin1[i-1: i+2, 1]
            #if it is the first column, there is no prior histogram
            currHist = np.zeros(256, int)
        else:
            #if this is the last column
            if j == d1-1:
                # if it is the first row
                if i==0:
                    neighborhood = Iin1[0:2, j-1:j+1]
                    if j > 1:
                        leftCol = Iin1[0:2, j-2]
                else:
                    if i == d2 - 1:
                        neighborhood = Iin1[i - 1: i + 1, j-1:j+1]
                        if j > 1:
                            leftCol = Iin1[i - 1: i + 1, j - 2]
                    else:
                        neighborhood = Iin1[i-1: i+2, j - 1:j + 1]
                        if j > 1:
                            leftCol = Iin1[i-1: i+2, j - 2]
            else: #not the first or the last column
                if i == 0:  #this is the first row somewhere between left and right edges
                    neighborhood = Iin1[0:2, j - 1:j + 2]
                    if j > 1:
                        leftCol = Iin1[0:2, j - 2]
                    rightCol = Iin1[0:2, j + 1]
                else:
                    if i == d2 -1:# this is the last row somewhere between left and right edges
                        neighborhood = Iin1[i-1:i+1, j - 1:j + 2]
                        if j > 1:
                            leftCol = Iin1[i-1:i+1, j - 2]
                        rightCol = Iin1[i-1:i+1, j + 1]
                    else: # the normal situation, with full 3*3 neighborhoods
                        neighborhood = Iin1[i-1: i+2, j-1:j+2]
                        if j > 1:
                            leftCol = Iin1[i-1: i+2, j - 2]
                        rightCol = Iin1[i-1: i+2, j + 1]

        currHist = localHistogram((j == 0), currHist, neighborhood, leftCol, rightCol)
        acuDens = accuDensities(currHist)
        Iout1[i,j] = math.floor((acuDens[Iin1[i,j]] * 255)/(neighborhood.shape[0]*neighborhood.shape[1]))



# print Iout2.size
Iout1 = Iout1.astype(np.uint8)

cv2.imshow("embedded_squares - new", Iout1)

cv2.waitKey(0)

print 'destroy all windows'
cv2.destroyAllWindows()