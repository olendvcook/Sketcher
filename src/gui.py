import tkinter as tk
from PIL import Image, ImageTk

def display_img(img):
    window = tk.Tk()

    #resize
    """
    basewidth = 1080
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((basewidth,hsize), Image.ANTIALIAS)

    baseheight = 1080
    hpercent = (baseheight/float(img.size[1]))
    wsize = int((float(img.size[0])*float(hpercent)))
    img = img.resize((wsize,baseheight), Image.ANTIALIAS)
    """
    img = img_resize(img, 960, True)

    image_tk = ImageTk.PhotoImage(img)
    tk.Label(window, image=image_tk).pack()
    window.mainloop()

def img_resize(img, basesize, boundIsHeight = False):
    if boundIsHeight:
        hpercent = (basesize/float(img.size[1]))
        wsize = int((float(img.size[0])*float(hpercent)))
        img = img.resize((wsize,basesize), Image.ANTIALIAS)
    else:
        wpercent = (basesize/float(img.size[0]))
        hsize = int((float(img.size[1])*float(wpercent)))
        img = img.resize((basesize,hsize), Image.ANTIALIAS)
    return img

