import tkinter

class ProgramGUI: # define a ProgramGUI class

    def __init__(self):
        
        self.main = tkinter.Tk() # create the main window
        self.main.title("Workshop 9: GUI Programming")
        self.main.geometry("400x400") #Set the main window size 400*400
        self.main.resizable(0, 0) #Prevent the main window from being resized/maximised.
        self.main.iconbitmap('Graphicloads-100-Flat-Home.ico') #change icon
        self.main.configure(background='green')

        self.main.attributes('-alpha', 0.8)
        self.main.lift()
        #self.main.attributes("-fullscreen", True) 

        
        tkinter.mainloop()

gui = ProgramGUI() # create a ProgramGUI object
