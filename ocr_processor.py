import cv2
import pytesseract
from PIL import Image
import numpy as np

# Tesseract path (change if different)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def preprocess_image(image):

    img = np.array(image)

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Increase contrast
    gray = cv2.convertScaleAbs(gray, alpha=2, beta=20)

    # Remove noise
    blur = cv2.GaussianBlur(gray, (5,5), 0)

    # Thresholding
    thresh = cv2.adaptiveThreshold(
        blur,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        11,
        2
    )

    return thresh


def extract_text(image):

    processed = preprocess_image(image)

    config = "--oem 3 --psm 6"

    text = pytesseract.image_to_string(processed, config=config)

    return text, processed