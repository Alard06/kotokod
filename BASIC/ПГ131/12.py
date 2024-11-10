from tkinter import *
import webbrowser
import subprocess

subprocess.
screen = Tk()
screen.title("Btn")
screen.geometry("400x400")
screen['bg'] = 'white'

def test():
    webbrowser.open('https://www.google.com')


btn1 = Button(screen, text="Click!",
              command=test,
              bg='red', fg='blue',
              font=("Arial Bold", 20),
              activebackground='blue',
              activeforeground='red')

btn1.place(relx=0.5, rely=0.5)
screen.mainloop()