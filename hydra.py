
import threading 
from tkinter import *  

def hydra():
    root = Tk()
    root.title("Cutt of one face, two shall take it's place")
    root.geometry("400x400")
    root.configure(bg='black')
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()

def on_closing():
    for i in range(2):
        x = threading.Thread(target=hydra)
        x.start()

if __name__ == "__main":
    hydra()