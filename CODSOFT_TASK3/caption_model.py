import torch
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import random

class ImageCaptioner:
    def __init__(self):
        # Load BLIP model once
        print("Loading BLIP model... This takes 20-30 seconds first time")
        self.processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
        self.model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
        self.model.eval()
        print("Model Loaded Successfully!")

    def generate_caption(self, image, style="normal"):
        # Step 1: Get base caption from BLIP
        inputs = self.processor(image, return_tensors="pt")
        out = self.model.generate(**inputs, max_length=50, do_sample=True, num_beams=5)
        base_caption = self.processor.decode(out[0], skip_special_tokens=True)

        # Step 2: Modify based on style
        if style == "detailed":
            return f"A highly detailed photo of {base_caption}"

        elif style == "funny":
            funny_templates = [
                f"When you see {base_caption} and instantly want to flex",
                f"POV: {base_caption} pulls up to the car meet",
                f"Me: broke. Also me: {base_caption}",
                f"This {base_caption} has main character energy",
                f"My wallet: empty. My car: {base_caption}"
            ]
            return random.choice(funny_templates)

        elif style == "poetic":
            poetic_templates = [
                f"Behold, {base_caption}, a beauty that races with the wind",
                f"Like a dream on wheels, {base_caption} glides through time",
                f"In silver and speed, {base_caption} tells a story"
            ]
            return random.choice(poetic_templates)

        else: # normal
            return f"{base_caption}"