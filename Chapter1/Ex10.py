import numpy as np
import cv2

#Connectivity ingrediants (? rechivei kshiroot)
# returns how many Connectivity elemets with holes are there

Iin1 = cv2.imread('holes.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('holes', Iin1)

def searchNextSibling(lastPredec, i, j, OutputMat, counter):
    sibling = [-1,-1, 0] # next sibling and is hole or not. o- not, 1- hole.
    if i < OutputMat.shape[0] and j + 1 < OutputMat.shape[1]:
        sibling = helpFunc(lastPredec, i , j+1)
    if sibling[1] == -1 and sibling[0] == -1:
        if i + 1 < OutputMat.shape[0] and j  < OutputMat.shape[1]:
            sibling = helpFunc(lastPredec, i + 1, j )
    if sibling[1] == -1 and sibling[0] == -1:
        if i - 1 < OutputMat.shape[0] and j  < OutputMat.shape[1]:
            sibling = helpFunc(lastPredec, i - 1, j )
    if sibling[1] == -1 and sibling[0] == -1:
        if i < OutputMat.shape[0] and j - 1 < OutputMat.shape[1]:
            sibling = helpFunc(lastPredec, i, j - 1)
    return sibling

def helpFunc(lastPredec, i,j):
    sibling =  [-1,-1, 0]
    if (i != lastPredec[0] or j != lastPredec[1])  and Iin1[i, j] == 0:
        if Visited[i, j] == 0:
            sibling = [i , j, 0]
        else:
            if OutputMat[i, j] == counter:
                sibling = [-1, -1, 1]
            else:
                sibling = [-1, -1, 0]
    return sibling

d1,d2 = Iin1.shape
Visited = np.zeros([d1, d2], np.uint8)


d1,d2 = Iin1.shape
print(d1,d2)

OutputMat = np.zeros([d1, d2], np.uint8)

hole = 0;
holeCounter = 0;
counter = 1;
lastPredec = [0,0]
stack = []
for i in range(d1):
    for j in range(d2):
        #if we found  black one in the picture
        if Iin1[i,j] == 0  and Visited[i,j] == 0:
            stack.append([i,j])
            # lastPredec = [i, j]
            while (len(stack) > 0):
                stackTop = stack[-1]
                if len(stack) > 1:
                    last = stack[-2]
                else:
                    last = stack[-1]
                sib = searchNextSibling(last, stackTop[0], stackTop[1], OutputMat, counter)
                # lastPredec = [stackTop[0],stackTop[1]]
                if sib[0] > -1 and sib[1] > -1:
                    if sib[2] == 1 and hole == 0:
                        holeCounter += 1
                        hole = 1
                    nextSib = [sib[0], sib[1]];
                    OutputMat[stackTop[0], stackTop[1]] = counter
                    Visited[stackTop[0],stackTop[1]] = 255
                    stack.append(nextSib)
                else:
                    Visited[stackTop[0], stackTop[1]] = 255
                    OutputMat[stackTop[0], stackTop[1]] = counter
                    stack.pop();
            hole = 0;
            counter += 1;

# print Iout2.size
Iout1 = OutputMat.astype(np.uint8)
print Iout1
cv2.imshow("connectivity map", Iout1)

print "number of holes:"
print holeCounter

print "number of connectivity:"
print counter

Iout2 = Visited.astype(np.uint8)
print Iout1
cv2.imshow("visited map", Iout2)

cv2.waitKey(0)

print 'destroy all windows'
cv2.destroyAllWindows()