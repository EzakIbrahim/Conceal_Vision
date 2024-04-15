from stegano import exifHeader

user_Choice = int(input("Choose The Mod:\n[1] Encode\n[2] decode\nOption: "))

if user_Choice == 1:
    image = input("Write the image name and extinsion example: image.jpg\n")
    FinalImageName = input("Write the Final image name and extinsion example: Final.png\n")
    HiddenMessage = input("Write the desired text to be hidden\n")
    secret = exifHeader.hide(image,
                            FinalImageName, secret_message=HiddenMessage)
    print("DONE")
elif user_Choice == 2:
    Decodedimage = input("Write the image name and extinsion example: image.jpg\n")
    print(exifHeader.reveal(Decodedimage))
else:
    print("ERROR: invalid option")