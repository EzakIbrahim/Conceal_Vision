# Conceal_Vision

This Python application provides a user-friendly interface for hiding and revealing text within image (steganography) and could also hiding and reveal files within images and  videos . It offers the following functionalities:

# Text Steganography (Using ExifHeader)

Hide Text in an Image: Embed a secret message within an image's Exif data, making the hidden information undetectable to the naked eye.
Extract Text from an Image: Recover the hidden text from an image containing Exif-based steganography.

# File Hiding 
  1. Conceal Files in an Image or video : This functionality aims to embed files within an image or video (will be descussed later).
  
  2. Extract Files from an Image or video:  This functionality aims to recover hidden files from an image or video after concealment (will be descussed later).

# Text Steganography explanation (Text_To_Image.py):

  ## Explanation:
  This is a simple example from the code i use to create the functionlity of the (simple text to image) option in the software,the code implements steganography(the art of hiding messages in everyday files like images). It uses the stegano library.
  ## Breakdown:
  ### Imports:
  `from stegano import exifHeader`: Imports the hide and reveal functions (presumably) from a custom exifHeader module within the stegano library.
  ### User Input:
  `user_Choice = int(input("Choose The Mod:\n[1] Encode\n[2] decode\nOption: "))`: Prompts the user to choose between encoding (hiding a message) or decoding (revealing a hidden message). It reads the input, converts it to an integer, and stores it in `user_Choice`.
  ### Encoding (if user_Choice is 1):
  `image = input("Write the image name and extinsion example: image.jpg\n")`: Prompts the user to enter the name and extension of the image file containing the secret message.
  
  `FinalImageName = input("Write the Final image name and extinsion example: Final.png\n")`: Prompts the user to enter the desired name and extension for the final image where the message will be hidden.
  
  `HiddenMessage = input("Write the desired text to be hidden\n")`: Prompts the user to enter the text they want to hide.
  
  `secret = exifHeader.hide(image, FinalImageName, secret_message=HiddenMessage)`: Calls the hide function (likely from exifHeader) to perform the encoding. It passes the original image name, final image name, and the secret message as arguments. The return value      is stored in secret (possibly for debugging or internal use).
  
  `print("DONE")`: Prints a success message if encoding is successful.
  ### Decoding (if user_Choice is 2):
  `Decodedimage = input("Write the image name and extinsion example: image.jpg\n")`: Prompts the user to enter the name and extension of the image containing the hidden message.
  
  `print(exifHeader.reveal(Decodedimage))`: Calls the reveal function (likely from exifHeader) to extract the hidden message. It passes the image name as an argument. The revealed message is then printed.
  ### Error Handling:
  `else`: If the user's choice is not 1 or 2 (invalid option).
  
  `print("ERROR: invalid option")`: Prints an error message.

  ### Important Notes:
  Steganography techniques can be fragile and easily detectable depending on the method used. It's generally not considered a secure way to hide sensitive information.

# File Hiding explanation (Files_In_image_OR_video.py):
## Explanation:
This Python code defines two functions for hiding and extracting files within an image. It's a very basic implementation of steganography, which is the practice of hiding information in another medium.
### Libraries:
shutil: This library helps with file operations like copying.
### Hide_files function:
  - It takes three arguments:

    `zip_file_path`: Path to the file you want to hide (compressed into a ZIP)

    `image_file_path`: Path to the image where you want to hide the file

    `output_directory`: Directory to save the modified image

It checks if all arguments are provided.

If valid, it opens the image and ZIP file in binary read mode ('rb').

It creates a path for the output image (output.png) within the specified directory.

It opens the output image in binary write mode ('wb').

Using shutil.copyfileobj, it essentially copies the content of both the image and ZIP file sequentially into the new output image. 
> [!NOTE]
> This is a very rudimentary way of hiding data and can be easily detected.

### Extract_files function:
 - It takes two arguments:

   `concealed_file_path`: Path to the image containing the hidden file.

   `output_directory`: Directory to save the extracted ZIP file.

It checks if both arguments are provided.

It opens the concealed image file in binary read mode ('rb').

It searches for the specific byte sequence (b'\x50\x4b\x03\x04') that indicates the beginning of a ZIP file. If not found, it raises an error.

If found, it positions the read pointer to the start of the ZIP data within the image file.

It reads the remaining data as the concealed ZIP data.

It creates a path for the extracted ZIP file (extracted.zip) within the specified directory.

It opens the output ZIP file in binary write mode ('wb') and writes the extracted data to it.


> [!CAUTION]
> Important points:
>This is a basic example and has limitations. It doesn't hide the data securely and might damage the image quality.
There are more sophisticated steganography techniques that embed data in a less noticeable way.
Be aware of the legal implications of hiding data in files without permission.
