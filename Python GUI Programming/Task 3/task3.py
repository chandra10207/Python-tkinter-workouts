import tkinter as tk
from tkinter import messagebox

win = tk.Tk()
win.title("Toasted Sandwich")
win.geometry("400x400") 

filling1 = tk.IntVar()
filling2 = tk.IntVar()
filling3 = tk.IntVar()

def create_order():       
    f1 = int( filling1.get() )
    f2 = int( filling2.get() )
    f3 = int( filling3.get() )
    if(f1 == 0 and f2==0 and f3 == 0):
        messagebox.showerror('No Filling','Select at least one filling')
    else:
        bread_type = bread.get()
        filling = ''
        if(f1 == 1):
            filling = '  Ham\n'

        if(f2 == 1):
            filling = filling + '   Cheese\n'
        if(f3 == 1):
            filling = filling + '   Tomato\n'
            
        message = bread_type +' Bread\n\n'+ 'Fillings:\n '+ filling
        messagebox.showinfo('Order Submitted',message)


breakfastlbl = tk.Label(win, text="Bread").pack()
#breakfastlbl.grid(row=0,column=0)
fillins_list = ['White', 'Wholemeal', 'Multigrain']
bread = tk.StringVar()    
count = 0
for f in fillins_list:
    rb = tk.Radiobutton(win, text=f, value=f,variable=bread)
    count += 1
    rb.pack()
bread.set('White')


label = tk.Label(win, text="\n\nFillings").pack()
CB1 = tk.Checkbutton(win, text="Ham",variable=filling1).pack()
CB2 = tk.Checkbutton(win, text="Cheese",variable=filling2).pack()
CB3 = tk.Checkbutton(win, text="Tomato",variable=filling3).pack()

submitbtn = tk.Button(win, text="Submit Order",command=create_order).pack()

win.mainloop()
