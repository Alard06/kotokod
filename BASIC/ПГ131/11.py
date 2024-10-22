from tkinter import *

screen = Tk()
screen.title("Cat")
screen.geometry("500x500")
screen['bg'] = 'white'
screen.resizable(False, False)

text1 = Label(bg='white',
              text='Кошки и корма😼',
              font=('Arial', 20, 'bold'))
text1.pack()
text2 = Label(bg='white',
              fg='grey',
              text='class',
              font=('Arial', 20, 'bold'))
text2.pack()
text3 = Label(bg='black',
              fg='white',
              text='method',
              font=('Arial', 20, 'bold'))
text3.place(relx=0.5, rely=0.5)

screen.mainloop()