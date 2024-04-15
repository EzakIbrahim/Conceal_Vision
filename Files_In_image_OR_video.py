import shutil

# Function to conceal files within an image
def Hide_files(zip_file_path,image_file_path,output_directory):
    if zip_file_path and image_file_path and output_directory:
            # Open the image and ZIP files
            with open(image_file_path, 'rb') as img_file, open(zip_file_path, 'rb') as zip_file:
                output_image_path = f"{output_directory}/output.png"
                # Create a new image by copying the content of the image and ZIP file into it
                with open(output_image_path, 'wb') as output_file:
                    shutil.copyfileobj(img_file, output_file)
                    shutil.copyfileobj(zip_file, output_file)

# Function to decrypt files concealed within an image
def Extract_files(concealed_file_path,output_directory):
    if concealed_file_path and output_directory:
            with open(concealed_file_path, 'rb') as concealed_file:
                # Locate the start position of the ZIP file within the output image
                zip_start = concealed_file.read().find(b'\x50\x4b\x03\x04')  # ZIP file signature
                if zip_start == -1:
                    raise ValueError("Concealed ZIP file not found in the image.")

                # Extract the concealed ZIP data
                concealed_file.seek(zip_start)
                zip_data = concealed_file.read()

                # Save the extracted data as a ZIP file
                output_zip_path = f"{output_directory}/extracted.zip"
                with open(output_zip_path, 'wb') as output_file:
                    output_file.write(zip_data)
