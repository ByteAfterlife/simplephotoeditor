from PIL import Image, ImageColor
import customtkinter
import os
import sys
from colorama import Fore
import time
path = input("Path to image for editing? ")
imageformats = ['.png', '.jpg', '.jpeg']
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
app.geometry("400x300")
app.title("Adobe PS dollarama edition")

RotationValue = 0
Flip = ""
def setrotate():
    global RotationValue
    RotationValue = customtkinter.CTkInputDialog(text="Value? ", title="Value Request")
    RotationValue = int(RotationValue.get_input())
    if RotationValue == "":
        del RotationValue

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




rotate = customtkinter.CTkButton(app, text="Rotate image", command=setrotate)
rotate.pack(padx=20, pady=20)
crop = customtkinter.CTkButton(app, text="Flip image", command=setflip)
crop.pack(padx=20, pady=25)
app.mainloop()


def destroy():
    sys.exit()

if os.path.exists(path):
    image = Image.open(path)
    if RotationValue:
        image = image.rotate(RotationValue, expand=True, fillcolor=ImageColor.getcolor('yellow','RGB'))
    if Flip:
        if Flip == "H":
            image = image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
        elif Flip == "V":
            image = image.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
        elif Flip == "B":
            image = image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
            image = image.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
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