import tkinter as tk
from tkinter import filedialog
from tkinter import *
import os
import sys 
import time
import glob
import sqlite3
import shutil  



#variables set to none for later use
filePathSource= None
filePathDestination= None

    
"""
The GUI Is listed below here
"""
#Create the window
class ParentWindow(Frame):
    
    def __init__ (self, master):
        Frame.__init__(self)

        self.master = master

        self.master.resizable(width=False, height=False)
        self.master.title('Check Files')
        self.master.config(bg='#F5F5F5')
        #Create the button for opening the directory using the openBrowser function
        self.btnSearch = Button(self.master, text="Source", command=lambda:openBrowserSource(self), bg='#B0C4DE',width=10)
        self.btnSearch.grid (row=1, column=1, padx=(15,20), pady=(30,10))
        #Create the button for opening the directory using the openBrowser function
        self.btnSearch2 = Button(self.master, text="Destination", command=lambda:openBrowserDestination(self), bg='#B0C4DE',width=10)
        self.btnSearch2.grid (row=2, column=1, padx=(15,20), pady=(0,30))
        #Create the button to iterate through the files from the selected source path and paste txt files in to the destination
        #while also adding in to the db the file names and the timestamp for the update
        self.btnExecute = Button(self.master, text="Execute", command=lambda:searchTxt(self), bg='#B0C4DE',width=10)
        self.btnExecute.grid (row=3, column=2, padx=(15,20), pady=(0,30),sticky=S+E)
        #create the text entry box to house the directory for the Source button
        self.insert1 = Entry(self.master, bg='#DCDCDC',width=50,)
        self.insert1.grid(row=1, column=2,padx=(15,15), pady=(30,10))
        #create the text entry box to house the directory for the destination buttn
        self.insert2 = Entry(self.master, bg='#DCDCDC',width=50,)
        self.insert2.grid(row=2, column=2,padx=(15,15), pady=(0,30))

        create_db(self)

"""
Creating the database here
"""
def create_db(self):
    conn = sqlite3.connect('drill5.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_fileList VARCHAR(250), \
            col_timeStamp VARCHAR(250) \
            )")
        conn.commit()
    conn.close()
    

"""
The functions are listed below here
"""
#the function to open the directory for the user to select a file path

def openBrowserSource(self):
    current_directory = filedialog.askdirectory() #opens directory
    global filePathSource
    filePathSource = os.path.join(current_directory) #sets the users selection to the file_path
    self.insert1.delete(0, END) #clears the text box. If the user has made a prior selection it will remove it.
    self.insert1.insert(END, filePathSource) #inserts the users selection to the entry box that we called "insert1"

def openBrowserDestination(self):
    current_directory = filedialog.askdirectory() #opens directory
    global filePathDestination
    filePathDestination = os.path.join(current_directory) #sets the users selection to the file_path
    self.insert2.delete(0, END) #clears the text box. If the user has made a prior selection it will remove it.
    self.insert2.insert(END, filePathDestination) #inserts the users selection to the entry box that we called "insert2"  

def searchTxt(self):
    os.chdir(filePathSource) #assigns this to the file path that the user selected
    textFiles = glob.glob('*.txt') #searches for the files that end in .txt
    print(textFiles) #this returns the 2 .txt files in the source directory
    for fileName in textFiles: #moves the text files to the destination path the user selected
        shutil.move(fileName,filePathDestination)
        print (os.path.getmtime(filePathDestination+"/"+fileName)) #gets the last modified time in the selected destination path 
        addFileToDatabase(fileName, os.path.getmtime(filePathDestination+"/"+fileName))

def addFileToDatabase(filename, timestamp):
    conn = sqlite3.connect('C:\\Python\\The-Tech-Academy-Basic-Python-Projects\\drill5.db')
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO tbl_files (col_fileList,col_timeStamp) VALUES (?,?)""",(filename, timestamp))
    conn.commit()
    conn.close()
      
if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
    create_db(self)
    
