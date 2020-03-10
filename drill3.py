import tkinter
from tkinter import *

class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__(self)

        self.master = master

        self.master.resizable(width=False, height=False)
        self.master.title('Check Files')
        self.master.config(bg='gainsboro')

        self.btnBrowse1 = Button(self.master, text="Browse...", bg='gainsboro',width=12)
        self.btnBrowse1.grid (row=2, column=1, padx=(15,20), pady=(35,0),sticky=N+W)

        self.btnBrowse2 = Button(self.master, text="Browse...", bg='gainsboro',width=12)
        self.btnBrowse2.grid (row=3, column=1, padx=(15,20), pady=10,sticky=N+W)

        self.btnCheck = Button(self.master, text="Check for files...", bg='gainsboro',width=12, height=2)
        self.btnCheck.grid (row=4, column=1,columnspan=2, rowspan=1,padx=15, pady=15,sticky=S+W)

        self.btnClose = Button(self.master, text="Close Program", bg='gainsboro',width=12, height=2)
        self.btnClose.grid (row=4, column=4,columnspan=2, rowspan=1,padx=15, pady=15,sticky=SE)

        self.insert1 = Entry(self.master, bg='white',width=50)
        self.insert1.grid(row=2, column=2,columnspan=3, rowspan=1,padx=(15,20), pady=(35,0),sticky=N+W)
        
        self.insert2 = Entry(self.master, bg='white',width=50)
        self.insert2.grid(row=3, column=2,columnspan=3, rowspan=1,padx=(15,20), pady=10,sticky=N+W)


        
if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop
