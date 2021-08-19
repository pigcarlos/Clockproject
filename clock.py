from tkinter import*
from time import strftime

#Window
Window = Tk()
Window.geometry("530x160")
Window.resizable(0,0)
Window.title("Clock")

#Body frame
Frame(Window, width=530, height=160, background="#404040").place(x=0, y=0,)

#Function
def time():
    clock=strftime("%H : %M : %S")
    label.config(text=clock)
    label.after(1000,time)

#Label 
label = Label(Window, font=("Agency FB", 60, "bold"), padx=25, pady=35, bg="#404040", foreground="white")
label.pack(anchor="center")

#call function
time()

Window.mainloop()