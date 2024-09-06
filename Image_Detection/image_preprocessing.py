import cv2

def preprocess_image(image_path):
    """Preprocess image for disease detection."""
    image = cv2.imread(image_path)
    image = cv2.resize(image, (224, 224))  # Example preprocessing
    image = image / 255.0  # Normalize image
    return image
