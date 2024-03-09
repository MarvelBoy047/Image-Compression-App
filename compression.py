from PIL import Image
import os
import io


def compress_image(input_path, output_path, target_size):
    # Open the image
    img = Image.open(input_path)

    # Convert RGBA images to RGB
    if img.mode == 'RGBA':
        img = img.convert('RGB')

    # Resize the image to reduce processing time
    img.thumbnail((800, 800))  # Adjust size as needed

    # Compress the image with a faster compression algorithm
    while True:
        # Save image to a bytes buffer
        buf = io.BytesIO()
        img.save(buf, format='JPEG', optimize=True, quality=95)
        buf.seek(0)

        # If size is acceptable, save the image to disk
        if buf.getbuffer().nbytes <= target_size * 1024:
            with open(output_path, 'wb') as f_out:
                f_out.write(buf.getbuffer())
            break
        else:
            # Decrease quality and try again
            target_size -= 10
            if target_size <= 10:
                # If size goes below 10KB, break the loop to avoid extreme compression
                break


def main():
    # Create directories if they don't exist
    os.makedirs("input_images", exist_ok=True)
    os.makedirs("compressed_images", exist_ok=True)

    # User input
    input_file = input("Enter the name of the image file (with extension): ")
    target_size = int(input("Enter the target size in KB: "))

    # Load input and output paths
    input_path = os.path.join("input_images", input_file)
    output_path = os.path.join("compressed_images", "compressed_" + input_file)

    # Move input image to input_images folder
    os.replace(input_file, input_path)

    # Compress the image
    compress_image(input_path, output_path, target_size)

    print("Image compression successful!")


if __name__ == "__main__":
    main()
