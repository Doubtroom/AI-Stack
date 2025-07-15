import cv2 as cv
import numpy as np
import pytesseract
from PIL import Image, ImageOps, ImageEnhance
from transformers import TrOCRProcessor, VisionEncoderDecoderModel
import torch
import requests
from io import BytesIO
import os
import sys
from src.exception import CustomException

# Load TrOCR once
processor = TrOCRProcessor.from_pretrained("microsoft/trocr-base-handwritten")
model = VisionEncoderDecoderModel.from_pretrained("microsoft/trocr-base-handwritten")

def load_image(image_path):
    try:    
        """Load image from URL or local path and return PIL + OpenCV format."""
        if image_path.startswith("http"):
            response = requests.get(image_path)
            img_pil = Image.open(BytesIO(response.content)).convert("RGB")
        else:
            img_pil = Image.open(image_path).convert("RGB")
        img_cv = cv.cvtColor(np.array(img_pil), cv.COLOR_RGB2BGR)
        return img_pil, img_cv
    except Exception as e:
            raise CustomException(e,sys)

def preprocess_for_tesseract(img_pil):
    try:    
        """Preprocessing for Tesseract (printed text) using PIL."""
        gray = ImageOps.grayscale(img_pil)
        inverted = ImageOps.invert(gray)
        enhanced = ImageEnhance.Contrast(inverted).enhance(2.0)
        return enhanced
    except Exception as e:
            raise CustomException(e,sys)

def extract_text_tesseract(image):
    try:
        """Extract printed text using Tesseract."""
        preprocessed = preprocess_for_tesseract(image)
        custom_config = r'--oem 3 --psm 6'
        return pytesseract.image_to_string(preprocessed, config=custom_config).strip()
    except Exception as e:
            raise CustomException(e,sys)

def extract_text_trocr(image):
    try:    
        """Extract handwritten text using TrOCR."""
        pixel_values = processor(images=image, return_tensors="pt").pixel_values
        with torch.no_grad():
            generated_ids = model.generate(pixel_values)
        return processor.batch_decode(generated_ids, skip_special_tokens=True)[0].strip()
    except Exception as e:
            raise CustomException(e,sys)

def smart_ocr(image_path, mode="auto"):
    try:
        """
        Combined OCR engine.
        mode: "printed" | "handwritten" | "auto"
        """
        img_pil, img_cv = load_image(image_path)

        if mode == "printed":
            return extract_text_tesseract(img_pil)

        elif mode == "handwritten":
            return extract_text_trocr(img_pil)

        elif mode == "auto":
            # Heuristic: use printed if average pixel intensity is high (sharp B&W)
            gray = cv.cvtColor(img_cv, cv.COLOR_BGR2GRAY)
            mean_val = np.mean(gray)
            if mean_val > 100:
                print("[Auto Mode] Chose: Tesseract (Printed)")
                return extract_text_tesseract(img_pil)
            else:
                print("[Auto Mode] Chose: TrOCR (Handwritten)")
                return extract_text_trocr(img_pil)
        else:
            raise ValueError("mode must be 'printed', 'handwritten', or 'auto'")
    except Exception as e:
            raise CustomException(e,sys)



# #  Example usage
# if __name__ == "__main__":
#     image_path = "https://res.cloudinary.com/dmj8k5ze1/image/upload/v1752568596/m5iwop3xhgwkhv17qp9v.png"  # or a URL
#     text = smart_ocr(image_path, mode="auto")  # change to "printed"/"handwritten" if known
#     print("\n Extracted Text:\n", text)
