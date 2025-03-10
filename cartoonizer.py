import cv2
import numpy as np
import argparse

def cartoonize_image(image_path, output_path="cartoonized.jpg"):
    # Load the image
    img = cv2.imread(image_path)

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Apply median blur
    gray_blurred = cv2.medianBlur(gray, 5)

    # Detect edges
    edges = cv2.adaptiveThreshold(
        gray_blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, 
        cv2.THRESH_BINARY, 9, 9
    )

    # Apply bilateral filter for smoothing
    color = cv2.bilateralFilter(img, 9, 300, 300)

    # Combine edge mask with smoothed image
    cartoon = cv2.bitwise_and(color, color, mask=edges)

    # Save output
    cv2.imwrite(output_path, cartoon)

    # Display the original and cartoonized image
    cv2.imshow("Original Image", img)
    cv2.imshow("Cartoonized Image", cartoon)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Cartoonize an image")
    parser.add_argument("--image", type=str, required=True, help="Path to input image")
    args = parser.parse_args()

    cartoonize_image(args.image)
