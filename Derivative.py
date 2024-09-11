import numpy as np 
import cv2 as cv2 

def inverse_fourier_transform(f_shift_filtered):
    """Apply the inverse Fourier transform to get the image back."""
    f_ishift = np.fft.ifftshift(f_shift_filtered)
    img_back = np.fft.ifft2(f_ishift)
    img_back = np.abs(img_back)
    return img_back
