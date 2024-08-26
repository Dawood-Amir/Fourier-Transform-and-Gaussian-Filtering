import numpy as np
import os 
import cv2 as cv2
import matplotlib.pyplot as plt
input_path = os.path.join("resources", "input1.jpg")

output_path = os.path.join(os.getcwd(), "results")
os.makedirs(output_path, exist_ok=True)

image = cv2.imread(input_path ,0)



def fourier_transform(image):
    """Perform the Fourier transform on the image."""
    f_transform = np.fft.fft2(image)
    f_shift = np.fft.fftshift(f_transform)
    return f_shift

def apply_gaussian_filter(f_shift, sigma=30):
    """Apply a Gaussian filter to the Fourier-transformed image."""
    rows, cols = f_shift.shape
    crows, ccol = rows // 2, cols // 2
    
    # Create Gaussian Mask
    x = np.linspace(-ccol, ccol, cols)
    y = np.linspace(-crows, crows, rows)
    x, y = np.meshgrid(x, y)
    
    gaussian_filter = np.exp(-(x**2 + y**2) / (2 * sigma**2))
    
    # Apply Gaussian filter
    f_shift_filtered = f_shift * gaussian_filter
    return f_shift_filtered, gaussian_filter

def inverse_fourier_transform(f_shift_filtered):
    """Apply the inverse Fourier transform to get the image back."""
    f_ishift = np.fft.ifftshift(f_shift_filtered)
    img_back = np.fft.ifft2(f_ishift)
    img_back = np.abs(img_back)
    return img_back

def remove_gaussian_filter(f_shift_filtered, gaussian_filter):
    """Remove the Gaussian filter from the Fourier-transformed image."""
    epsilon = 1e-10
    f_shift_recovered = f_shift_filtered / (gaussian_filter + epsilon)
    return f_shift_recovered

def display_images(original, magnitude_spectrum, filtered_image, recovered_image):
    """Display the original, filtered, and recovered images."""
    plt.figure(figsize=(12, 6))

    # Original Image
    plt.subplot(131)
    plt.imshow(original, cmap='gray')
    plt.title('Original Image')
    plt.axis('off')

    # Magnitude Spectrum after applying Gaussian filter
    plt.subplot(132)
    plt.imshow(magnitude_spectrum, cmap='gray')
    plt.title('Filtered Magnitude Spectrum')
    plt.axis('off')

    # Image after applying inverse Fourier Transform
    plt.subplot(133)
    plt.imshow(filtered_image, cmap='gray')
    plt.title('Gaussian Filtered Image')
    plt.axis('off')

    plt.show()

    # Display the Recovered Image
    plt.figure(figsize=(6, 6))
    plt.imshow(recovered_image, cmap='gray')
    plt.title('Recovered Image')
    plt.axis('off')
    plt.show()
def save_images(output_path, original, magnitude_spectrum, filtered_image, recovered_image):
    """Save the original, filtered, and recovered images."""
    plt.imsave(os.path.join(output_path, 'original_image.png'), original, cmap='gray')
    plt.imsave(os.path.join(output_path, 'magnitude_spectrum.png'), magnitude_spectrum, cmap='gray')
    plt.imsave(os.path.join(output_path, 'filtered_image.png'), filtered_image, cmap='gray')
    plt.imsave(os.path.join(output_path, 'recovered_image.png'), recovered_image, cmap='gray')

def process_image(image, sigma=30):
    """Complete process from Fourier transform to Gaussian filtering and recovery."""
    

    # Step 1: Fourier Transform
    f_shift = fourier_transform(image)

    # Step 2: Apply Gaussian Filter
    f_shift_filtered, gaussian_filter = apply_gaussian_filter(f_shift, sigma)

    # Step 3: Inverse Fourier Transform (to see the filtered image)
    filtered_image = inverse_fourier_transform(f_shift_filtered)

    # Step 4: Remove Gaussian Filter
    f_shift_recovered = remove_gaussian_filter(f_shift_filtered, gaussian_filter)

    # Step 5: Inverse Fourier Transform (to see the recovered image)
    recovered_image = inverse_fourier_transform(f_shift_recovered)

    # Display the results
    magnitude_spectrum = 20 * np.log(np.abs(f_shift_filtered))
    display_images(image, magnitude_spectrum, filtered_image, recovered_image)
    save_images(output_path, image, magnitude_spectrum, filtered_image, recovered_image)

# Call the function with the image path and sigma value
process_image(image, sigma=30)

