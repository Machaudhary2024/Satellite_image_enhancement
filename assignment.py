import sys
import cv2

import numpy as np
import matplotlib.pyplot as plt
import os


def logarithmic_transformation(img, c=1):
    # Formula: s = c * log(1 + r)
    img_float = img.astype(np.float32)
    log_img = c * np.log1p(img_float)
    log_img = cv2.normalize(log_img, None, 0, 255, cv2.NORM_MINMAX)
    return np.uint8(log_img)


def histogram_equalization(img):
    if len(img.shape) == 2:  # grayscale
        return cv2.equalizeHist(img)
    else:
        # Convert to YCrCb and equalize Y channel only
        ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
        ycrcb[:, :, 0] = cv2.equalizeHist(ycrcb[:, :, 0])
        return cv2.cvtColor(ycrcb, cv2.COLOR_YCrCb2BGR)


def plot_histogram(img, title):
    plt.hist(img.ravel(), 256, [0, 256])
    plt.title(title)
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Frequency")


def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <image_path>")
        sys.exit(1)

    image_path = sys.argv[1]
    img = cv2.imread(image_path, cv2.IMREAD_COLOR)

    if img is None:
        print("Error: Could not read image.")
        sys.exit(1)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply transformations
    log_img = logarithmic_transformation(
        gray, c=30)  # c chosen to balance brightness
    hist_eq_img = histogram_equalization(gray)

    # Save enhanced images
    base_name = os.path.splitext(os.path.basename(image_path))[0]
    cv2.imwrite(f"{base_name}_log.jpg", log_img)
    cv2.imwrite(f"{base_name}_hist_eq.jpg", hist_eq_img)

    # Display results
    plt.figure(figsize=(12, 10))

    # Original image + histogram
    plt.subplot(3, 2, 1), plt.imshow(
        gray, cmap='gray'), plt.title("Original Image")
    plt.subplot(3, 2, 2), plot_histogram(gray, "Original Histogram")

    # Logarithmic Transformation
    plt.subplot(3, 2, 3), plt.imshow(
        log_img, cmap='gray'), plt.title("Logarithmic Transformation")
    plt.subplot(3, 2, 4), plot_histogram(log_img, "Logarithmic Histogram")

    # Histogram Equalization
    plt.subplot(3, 2, 5), plt.imshow(
        hist_eq_img, cmap='gray'), plt.title("Histogram Equalization")
    plt.subplot(3, 2, 6), plot_histogram(hist_eq_img, "Equalized Histogram")

    plt.tight_layout()
    plt.show()

    # Print transformation functions used
    print("\nTransformation Functions:")
    print("1. Logarithmic Transformation: s = c * log(1 + r), with c = 30 (chosen to enhance dark regions).")
    print(
        "2. Histogram Equalization: redistributes pixel intensities to cover the full range [0, 255].")


if __name__ == "__main__":
    main()
