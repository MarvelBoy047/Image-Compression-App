### Image Compression App

This project provides a simple web application and a command-line tool for compressing images efficiently.

---

### Features

- **Web Application**:
  - Upload an image in JPG, JPEG, or PNG format.
  - Choose a target size for compression.
  - Compress the image without quality loss.
  - Display the original and compressed images side by side.
  - Download the compressed image.

- **Command-Line Tool**:
  - Compress images from the command line interface.
  - Specify the target size and quality level for compression.
  - Automatically resize images to reduce processing time.
  - Supports JPG, JPEG, and PNG formats.

---

### How to Use

#### Web Application

1. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

3. Upload an image file.
4. Choose a target size for compression.
5. Click the "Compress" button.
6. Download the compressed image.

#### Command-Line Tool

1. Ensure you have Python installed on your system.

2. Run the compression script:
   ```bash
   python compression.py
   ```

3. Follow the prompts to enter the image file name, target size, and quality level.

4. The compressed image will be saved in the `compressed_images` folder.

---

### File Descriptions

- **app.py**: Contains the Streamlit web application code for image compression.
- **compression.py**: Implements the image compression algorithm for the command-line tool.
- **input_images/**: Folder to store uploaded input images.
- **compressed_images/**: Folder to store compressed images.
**
