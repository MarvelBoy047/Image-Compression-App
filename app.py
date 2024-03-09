import streamlit as st
from PIL import Image
import os
import base64
import io


def compress_image(img, output_path, target_size):
    # Convert the image to RGB mode if it has an alpha channel
    if img.mode == "RGBA":
        img = img.convert("RGB")

    # Set initial quality
    quality = 95

    # Compress the image with a faster compression algorithm
    while True:
        # Save image to a bytes buffer
        buf = io.BytesIO()
        img.save(buf, format='JPEG', optimize=True, quality=quality)
        buf.seek(0)

        # If size is acceptable, save the image to disk
        if buf.getbuffer().nbytes <= target_size * 1024:
            with open(output_path, 'wb') as f_out:
                f_out.write(buf.getbuffer())
            break
        else:
            # Decrease quality and try again
            quality -= 5
            if quality <= 5:
                # If quality goes below 5, break the loop to avoid extreme compression
                break


def main():
    # Create directories if they don't exist
    os.makedirs("input_images", exist_ok=True)
    os.makedirs("compressed_images", exist_ok=True)

    st.title("Image Compression App")

    # User input for image file
    uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Save the input image to the input_images folder
        input_image_path = os.path.join("input_images", uploaded_file.name)
        with open(input_image_path, "wb") as f:
            f.write(uploaded_file.getvalue())

        # Display the uploaded image
        img = Image.open(uploaded_file)
        st.image(img, caption="Uploaded Image", use_column_width=True)

        # User input for target size
        target_size = st.number_input("Target size (KB)", min_value=1, step=1, value=100)

        if st.button("Compress", key="compress_button"):
            # Compress the image
            output_path = "compressed_images/compressed_" + os.path.splitext(uploaded_file.name)[0] + ".jpg"
            compress_image(img, output_path, target_size)

            # Display the compressed image
            compressed_img = Image.open(output_path)
            st.image(compressed_img, caption="Compressed Image", use_column_width=True)

            st.success("Image compression successful!")

            # Add download button for the compressed image
            download_button = st.download_button(label="Download Compressed Image", data=open(output_path, "rb").read(), file_name=os.path.basename(output_path))


if __name__ == "__main__":
    main()
