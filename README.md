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
    ## User Input:
  `user_Choice = int(input("Choose The Mod:\n[1] Encode\n[2] decode\nOption: "))`: Prompts the user to choose between encoding (hiding a message) or decoding (revealing a hidden message). It reads the input, converts it to an integer, and stores it in `user_Choice`.

