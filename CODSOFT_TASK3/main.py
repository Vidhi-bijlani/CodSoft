from image_utils import load_image
from caption_model import ImageCaptioner

def main():
    print("🖼️ IMAGE CAPTIONING AI - CodSoft Task 3")
    captioner = ImageCaptioner()

    while True:
        img_path = input("\nEnter image path or 'exit': ")

        if img_path.lower() == 'exit':
            print("Goodbye!")
            break

        image = load_image(img_path)
        if image:
            caption = captioner.generate_caption(image)
            print(f"AI Caption: {caption}")

if __name__ == "__main__":
    main()