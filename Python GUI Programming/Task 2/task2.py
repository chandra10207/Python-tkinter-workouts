import tkinter

class ProgramGUI: # define a ProgramGUI class

    def __init__(self):
        
        self.main = tkinter.Tk() # create the main window
        self.main.title("Workshop 9: GUI Programming")
        self.main.geometry("500x370") #Set the main window size 400*400
        
        photo = tkinter.PhotoImage(file = './logo.png')
        label = tkinter.Label(image=photo)
        label.image = photo 
        label.pack()        
        tkinter.mainloop()

gui = ProgramGUI() # create a ProgramGUI object
