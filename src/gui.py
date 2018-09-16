import tkinter as tk
from PIL import Image, ImageTk
import threading

class Gui(threading.Thread):
    """
    Gui class in a seperate thread
    """

    def __init__(self):
            threading.Thread.__init__(self)
            self.running = True

            #calls run
            self.start()

    def callback(self):
        self.root.quit()

    def run(self):
        #initialize window
        self.root = tk.Tk()

        #initialize image region
        self.img_label = tk.Label(self.root)
        self.img_label.pack(side="left")

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

    def on_closing(self):
        self.root.destroy()
        self.running = False

    def display_img(self, img):

        #resize
        img = self.img_resize(img, 960, True)

        # configure image label with image
        self.image_tk = ImageTk.PhotoImage(img)
        self.img_label.configure(image=self.image_tk)
        

    def img_resize(self, img, basesize, boundIsHeight = False):
        if boundIsHeight:
            #calculate new width keeping aspect ratio and height of basesize
            hpercent = (basesize/float(img.size[1]))
            wsize = int((float(img.size[0])*float(hpercent)))
            img = img.resize((wsize,basesize), Image.ANTIALIAS)
        else:
            #calculate new height keeping aspect ratio and width of basesize
            wpercent = (basesize/float(img.size[0]))
            hsize = int((float(img.size[1])*float(wpercent)))
            img = img.resize((basesize,hsize), Image.ANTIALIAS)
        return img

