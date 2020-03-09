import tkinter
from tkinter import *

class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width=True, height=True)
        self.master.geometry('{}x{}'.format(700, 400))
        self.master.title('Learning Tkinter')
        self.master.config(bg='#B0C4DE')

        self.varFname = StringVar()
        self.varLname = StringVar()

        self.lblFname =  Label(self.master,text="First Name: ", font=("fixedsys",16),fg='#483D8B', bg='#B0C4DE')
        self.lblFname.grid(row=0, column=0, padx=(30,0), pady=(30,0))

        self.lblLname =  Label(self.master,text="Last Name: ", font=("fixedsys",16),fg='#483D8B', bg='#B0C4DE')
        self.lblLname.grid(row=1, column=0, padx=(30,0), pady=(30,0))

        self.lblDisplay = Label(self.master,text="", font=("fixedsys",16),fg='#483D8B', bg='#B0C4DE')
        self.lblDisplay.grid(row=3, column=1, padx=(30,0), pady=(30,0))

        self.txtFname = Entry(self.master,text=self.varFname, font=("fixedsys",16), fg='black', bg='#F0FFFF')
        self.txtFname.grid(row=0, column=1, padx=(30,0), pady=(30,0))
        
        self.txtLname = Entry(self.master,text=self.varLname, font=("fixedsys",16), fg='black', bg='#F0FFFF')
        self.txtLname.grid(row=1, column=1, padx=(30,0), pady=(30,0))

        self.btnSubmit = Button(self.master, text="Submit", width=10, height=2, font=("fixedsys",16),fg='#483D8B', bg='#F0FFFF', command=self.submit)
        self.btnSubmit.grid (row=2, column=1, padx=(0,0), pady=(30,0), sticky=NE)

        self.btnCancel = Button(self.master, text="Cancel", width=10, height=2, font=("fixedsys",16),fg='#483D8B', bg='#F0FFFF', command=self.cancel)
        self.btnCancel.grid (row=2, column=1, padx=(0,120), pady=(30,0), sticky=NE)

    def submit(self):
        fn = self.varFname.get()
        ln = self.varLname.get()
        self.lblDisplay.config(text='Welcome {} {}'.format(fn, ln))

    def cancel(self):
        self.master.destroy()
        
    
           
if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop
