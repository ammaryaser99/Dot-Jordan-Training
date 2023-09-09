from Assigment_1_Q1 import *
#Question 4:
image = plt.imread('testimg.jpg')
def ConvToGray(image):
    r, g, b = image[:,:,0], image[:,:,1], image[:,:,2]
    grayAvg=0.2989 * r + 0.5870 * g + 0.1140 * b
    grayImage = image.copy()

    for i in range(3):
        grayImage[:,:,i] = grayAvg
           
    return grayImage 
plt.imshow(ConvToGray(image))
plt.show()