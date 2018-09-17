import tkinter as tk
from PIL import Image, ImageTk
import threading
import time
from scrapers.imagescraper import grab_rdm_img
from imggui import ImgGui

class CtrlGui(threading.Thread):
    """
    CtrlGui class in a seperate thread
    """

    def __init__(self, img_urls, img_gui, hours=0, mins=0, secs=10):
            threading.Thread.__init__(self)
            self.running = True

            self.img_urls = img_urls
            self.img_gui = img_gui

            


            self.time1 = ''
            self.prevSec = ''            
            self.default_secs = self.secs = secs
            self.default_mins = self.mins = mins
            self.default_hours = self.hours = hours
            self.clock_running = True
            

            #calls run
            self.start()

    def callback(self):
        self.root.quit()

    def run(self):

        #initialize window
        self.root = tk.Tk()
        self.root.geometry("300x250")

        #clock = Label(rootWindow, font=('fixed', 20, 'bold'))
        self.clock = tk.Label(self.root, font=('fixed', 20))
        self.clock.grid(row = 1, column = 2, padx = 5, pady = (5,2))

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.timeout()

        self.tick()
        self.root.mainloop()
        

    def on_closing(self):
        self.root.destroy()
        self.running = False

    def tick(self):
        # get the current local time from the PC
    #    time2 = time.strftime('%Y/%m/%d %H:%M:%S')
        if self.clock_running:
            newSec = time.strftime('%S')
        else:
            newSec = ''
            self.prevSec = ''
        if newSec != self.prevSec:
            self.prevSec = newSec
            self.secs = self.secs - 1
            if self.secs < 0:
                self.secs = 59
                self.mins = self.mins - 1
                if self.mins < 0:
                    self.mins = 59
                    self.hours = self.hours - 1
                    if self.hours < 0:
                        self.timeout()                

        time2 = '%02d:%02d:%02d' % (self.hours, self.mins, self.secs)
        # if time string has changed, update it
        if time2 != self.time1:
            self.time1 = time2
            self.clock.config(text=time2)
        # calls itself every 200 milliseconds
        # to update the time display as needed
        # could use >200 ms, but display gets jerky
        self.clock.after(200, self.tick)

    def timeout(self):
        self.hours = self.default_hours
        self.mins = self.default_mins
        self.secs = self.default_secs

        #new image
        if self.img_gui.running:
            img = grab_rdm_img(self.img_urls)
            self.img_gui.display_img(img)
