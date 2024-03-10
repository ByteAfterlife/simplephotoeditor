from PIL import Image, ImageColor, ImageEnhance, ImageFilter
import customtkinter
import os
import sys
from colorama import Fore
import time
path = input("Path to image for editing? ")
imageformats = ['.png', '.jpg', '.jpeg', '.gif']
def checkifimg(input):
    endswithformat = False
    for format in imageformats:
        if input.endswith(format):
            endswithformat = True
    if endswithformat == False:
        return False
if checkifimg(path) == False:
    message = ""
    for index, format in enumerate(imageformats):
        if index < len(imageformats) - 1:
            message = message + format + ", "
        else:
            message = message + format
        
    print(Fore.RED + "Not an image! (" + message + ")")
    time.sleep(3)
    sys.exit()

app = customtkinter.CTk()
app.geometry("300x500")
app.title("Adobe PS dollarama edition")
# Defining default values
RotationValue = 0
Flip = ""
Brightness = 0
Sharpness = 0
Emboss = 0
Color = ""
def setrotate():
    global RotationValue
    RotationValue = customtkinter.CTkInputDialog(text="Value? ", title="Value Request")
    RotationValue = int(RotationValue.get_input())
    if RotationValue == "":
        del RotationValue
    global Color
    Color = customtkinter.CTkInputDialog(text="Also, we need a fill color for the background (since a background will exist if you rotate)? e.g: \"yellow\"", title="Value Request")
    Color = Color.get_input()

def fliphorizontal():
    global Flip
    Flip = "H"
def flipvertical():
    global Flip
    Flip = "V"
def flipboth():
    global Flip
    Flip = "B"
def setflip():
    FlipApp = customtkinter.CTk()
    FlipApp.title("Flip")
    FlipX = customtkinter.CTkButton(FlipApp, text="Flip Horizontally", command=fliphorizontal)
    FlipX.pack(padx=20, pady=20)
    FlipY = customtkinter.CTkButton(FlipApp, text="Flip Vertically", command=flipvertical)
    FlipY.pack(padx=20, pady=25)
    FlipXY = customtkinter.CTkButton(FlipApp, text="Flip both ways", command=flipboth)
    FlipXY.pack(padx=20, pady=30)
    FlipApp.mainloop()
def setbrightness():
    global Brightness
    Brightness = customtkinter.CTkInputDialog(text="Value? ", title="Value Request")
    Brightness = int(Brightness.get_input())
def setsharpness():
    global Sharpness
    Sharpness = customtkinter.CTkInputDialog(text="Value? ", title="Value Request")
    Sharpness = int(Sharpness.get_input())
def emboss():
    global Emboss
    Emboss = 1



rotate = customtkinter.CTkButton(app, text="Rotate image", command=setrotate)
rotate.pack(padx=20, pady=20)
crop = customtkinter.CTkButton(app, text="Flip image", command=setflip)
crop.pack(padx=20, pady=25)
bright = customtkinter.CTkButton(app, text="Brighten image", command=setbrightness)
bright.pack(padx=20, pady=30)
sharp = customtkinter.CTkButton(app, text="Sharpen image", command=setsharpness)
sharp.pack(padx=20, pady=35)
emboss = customtkinter.CTkButton(app, text="Emboss image (not customizable)", command=emboss)
emboss.pack(padx=20, pady=40)
app.mainloop()


def destroy():
    sys.exit()

if os.path.exists(path):
    image = Image.open(path)
    if RotationValue:
        image = image.rotate(RotationValue, expand=True, fillcolor=ImageColor.getcolor(Color,'RGB'))
    if Flip:
        if Flip == "H":
            image = image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
        elif Flip == "V":
            image = image.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
        elif Flip == "B":
            image = image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
            image = image.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
    if Brightness != 0:
        image = ImageEnhance.Brightness(image=image).enhance(Brightness)
    if Sharpness != 0:
        image = ImageEnhance.Sharpness(image=image).enhance(Sharpness)
    if Emboss == 1:
        image = image.filter(ImageFilter.EMBOSS)
    viewresult = customtkinter.CTk()
    viewresult.title("Final product")
    viewresult.geometry("350x200")
    viewfinal = customtkinter.CTkButton(viewresult, text="View final result", command=image.show)
    viewfinal.pack(padx=20, pady=10)
    closeapp = customtkinter.CTkButton(viewresult, text="Destroy result", command=destroy)
    closeapp.pack(padx=20, pady=20)
    viewresult.mainloop()
else:
    print(Fore.RED + "Image not found!")
    time.sleep(3)
