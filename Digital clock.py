import tkinter as tk
from time import strftime
clock=tk.Tk()
clock.title("Digital clock")

def time():
    string=strftime("%H:%M:%S %p \n%D")
    label.config(text=string)
    label.after(1000,time)

label=tk.Label(clock,font=('Algerian',70,'bold'),background='black',foreground='white')
label.pack(anchor='center')

time()
clock.mainloop()