from PIL import Image

def load_image(image_path):
    """Load and convert image to RGB"""
    try:
        image = Image.open(image_path).convert('RGB')
        return image
    except Exception as e:
        print(f"Error: Could not open image. {e}")
        return None