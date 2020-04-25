import os
import random
import sys
from tkinter import Tk, Frame, Button, mainloop, Label, PhotoImage, messagebox

try:
    win = Tk()
    win.resizable(False, False)
    win.title("Image Randomizer")
    win.iconbitmap("imageRandomizer.ico")

    index = 0
    images = os.listdir('images')

    path = os.path.dirname(sys.argv[0]) + "/images/"

    if len(images) == 0:
        messagebox.showerror("Error", "No images found! Did you put any images in the images folder?")
        sys.exit(1)
    random.shuffle(images)
    render = PhotoImage(file=path + images[index])

    def getImage():
        global index
        fileToOpen = path + images[index]
        newImage = PhotoImage(file=fileToOpen)
        currentImage.configure(image=newImage)
        currentImage.image = newImage

    def reset():
        if messagebox.askokcancel(title="Confirm", message="The image order will be shuffled and the first image in the new shuffle will be shown. Are you sure?"):
            global index
            index = 0
            random.shuffle(images)
            getImage()

    def getNextImage():
        global index
        if index < len(images) - 1:
            index += 1
            getImage()

    def getLastImage():
        global index
        if index > 0:
            index -= 1
            getImage()

    currentImageFrame = Frame(win)
    currentImageFrame.pack_propagate(0)
    currentImage = Label(currentImageFrame, bg="#00ff00")
    currentImage.configure(image=render)
    currentImage.grid()
    currentImageFrame.grid(row=0, padx=4, pady=4)

    buttonFrame = Frame(win)

    lastButton = Button(buttonFrame, text="Previous", width=10, command=lambda: getLastImage())
    lastButton.grid(row=0, column=0, padx=6, pady=4)

    nextButton = Button(buttonFrame, text="Next", width=10, command=lambda: getNextImage())
    nextButton.grid(row=0, column=1, padx=6, pady=4)

    resetButton = Button(buttonFrame, text="Shuffle and Reset", width=20, command=lambda: reset())
    resetButton.grid(row=1, column=0, columnspan=2, pady=4)

    buttonFrame.grid(row=1, padx=6, pady=4)

    mainloop()
except Exception as e:
    messagebox.showerror("Error", "An unexpected error occurred. The program will close. Details: " + str(e))
    sys.exit(1)