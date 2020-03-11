import tkinter as tk
from tkinter import filedialog
from tkinter import *
import os

#Create the window
class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__(self)

        self.master = master

        self.master.resizable(width=False, height=False)
        self.master.title('Check Files')
        self.master.config(bg='#F5F5F5')
        #Create the button for opening the directory using the openBrowser function
        self.btnBrowse = Button(self.master, text="Open", command=lambda:openBrowser(self), bg='#B0C4DE',width=12)
        self.btnBrowse.grid (row=1, column=1, padx=(15,20), pady=(35,35))
        #create the text entry box to house the directory
        self.insert1 = Entry(self.master, bg='#DCDCDC',width=50,)
        self.insert1.grid(row=1, column=2, rowspan=1,padx=(15,20), pady=(35,35))
#the function to open the directory for the user to select a file path       
def openBrowser(self):
    current_directory = filedialog.askdirectory() #opens directory
    file_path = os.path.join(current_directory) #sets the users selection to the file_path
    self.insert1.delete(0, END) #clears the text box. If the user has made a prior selection it will remove it.
    self.insert1.insert(END, file_path) #inserts the users selection to the entry box that we called "insert1"
    

if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop
