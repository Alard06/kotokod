from tkinter import *


def test():
    print('Click!')

def print_hello():
    text = f'Привет, {entry_1.get()})'
    entry_1.delete(0, END)
    label_1.config(text=text)

root = Tk()

root.geometry("500x500")
root.title("Study tkinter")


entry_1 = Entry(root, font=("Comic Sans MS", 20))
btn_entry_1 = Button(root,text='Ввести', command=print_hello, font=("Comic Sans MS", 15))

btn_entry_1.place(relx=0.4, rely=0.9)
entry_1.place(relx=0.1, rely=0.7)

btn_1 = Button(root,
               text="Кнопка",
               command=test,
               bg="red", fg="blue",
               font=("Arial Bold", 20))
label_1 = Label(root,
                text="Это просто текст",
                bg="red", fg="blue",
                font=("Arial Bold", 20))

btn_1.place(x=220, y=-50)
label_1.pack()

root.mainloop()
