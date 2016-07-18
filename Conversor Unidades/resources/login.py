try:
    #Python 2
    from Tkinter import Tk, Canvas
except:
    #Python 3
    from tkinter import Tk, Canvas
from PIL import Image, ImageTk


class intro(object):
    def __init__(self):

        self.master=Tk()

        self.x = (self.master.winfo_screenwidth()/3) - (self.master.winfo_width())
        self.y = (self.master.winfo_screenheight()/3) - (self.master.winfo_height())
        self.master.geometry("+%d+%d" % (self.x, self.y))
        self.master.overrideredirect(True)
        self.master.resizable(False,False)
        self.logointroimg=Image.open(r'img/Logo-introscreenmin.jpg')
        self.Tkimage3= ImageTk.PhotoImage(self.logointroimg)

        self.canvas = Canvas(self.master, height=378,width=672 )
        self.canvas.create_image(336,186, image=self.Tkimage3)
        self.canvas.pack()


        self.master.after(1250,self.master.destroy)

        self.master.mainloop()

