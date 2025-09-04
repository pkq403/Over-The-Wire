from PIL import Image

if __name__ == "__main__":
    img = Image.open("pixel.png")
    raw_bytes = img.tobytes()
    print("Raw pixel bytes: ", raw_bytes)
