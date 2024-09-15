import numpy as np 
import cv2 as cv2 
import os 

import matplotlib.pyplot as plt
#well use this file for shift invariance example  linearity chap 3 .

input_path = os.path.join("resources", "input1.jpg")

output_path = os.path.join(os.getcwd(), "results")
os.makedirs(output_path, exist_ok=True)


def getImage():
    image =  cv2.imread(input_path , cv2.IMREAD_GRAYSCALE)
    return image

def shiftInVariance():
    image = getImage()

    # Apply a Gaussian filter (kernel size 5x5, sigma = 1)
    gaussianFiltered =  cv2.GaussianBlur(image,(5,5),1)

    # Shift the original image by 50 pixels to the right
    rows, cols =  image.shape
    M =np.float32([[1,0,50],[0,1,0]]) # Affine transformation matrix for shifting right
    shiftImg = cv2.warpAffine(image, M , (cols,rows))

    # Apply the Gaussian filter to the shifted image
    gaussianBluredFirstTOShiftedImg = cv2.GaussianBlur(shiftImg , (5,5),1)

    # Shift the filtered image by 50 pixels
    shiftedFilteredImg  = cv2.warpAffine(gaussianFiltered , M , (cols,rows) )

    # Display the results
    plt.figure(figsize=(12, 8))

    plt.subplot(2, 3, 1)
    plt.title('Original Image')
    plt.imshow(image, cmap='gray')

    plt.subplot(2, 3, 2)
    plt.title('Gaussian Filtered Image')
    plt.imshow(gaussianFiltered, cmap='gray')

    plt.subplot(2, 3, 3)
    plt.title('Shifted Original Image')
    plt.imshow(shiftImg, cmap='gray')

    plt.subplot(2, 3, 4)
    plt.title('Shifted Filtered Image')
    plt.imshow(shiftedFilteredImg, cmap='gray')

    plt.subplot(2, 3, 5)
    plt.title('Gaussian blured first then Shifted Image')
    plt.imshow(gaussianBluredFirstTOShiftedImg, cmap='gray')

    plt.tight_layout()
    plt.show()

shiftInVariance()    
#So this shows us linearity dosent matter if we shift first or apply gaussian filter first 