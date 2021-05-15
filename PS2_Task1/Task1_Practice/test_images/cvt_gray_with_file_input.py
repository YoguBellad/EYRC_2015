# Import OpenCV & numpy
import numpy
import cv2

def color_grayscale(filename,g):
'''
filename-- input color image stored as file(Test color image is in folder
“Task1_Practice/test_images”. Pick first image to perform the experiment.)
    g-- int 0 or 1
returnsimg-- grayscale of input image if g=1 else color image
    '''
    #imgt is image matrix that stores input image
        imgt = cv2.imread(filename)# filename is string passed 
            if g==1: #checks if g is equals to 1 so that its converted to grayscale
                img = cv2.cvtColor(imgt, cv2.COLOR_BGR2GRAY)
    #img is converted 
            else:
    #if g is not equal to 1 then it output matrix is the temporary matrix imgt
                img=imgt
    return(img)# gives the caller function the resultant image matrix
