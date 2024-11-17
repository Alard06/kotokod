import random
from tkinter import *


def last_letter(city: str):
    # city[-1] # ъ ь ы й
    for letter in city[::-1]:
        if letter not in 'ьъы':
            return letter.upper()


def no_click():
    global letter, random_city
    play_city = entry.get()
    entry.delete(0, END)
    if (play_city not in previos_cities and
        play_city[0] == letter and
        play_city in cities):
        previos_cities.add(play_city)
        letter = last_letter(play_city)
        for city in cities:
            if city[0] == letter and city not in previos_cities:
                previos_cities.add(city)
                random_city = city
                break
        oldletter = letter
        letter = last_letter(random_city)
        answer_city_text.config(text=f'Понятно, мне на "{oldletter}"\n{random_city}, тебе на "{letter}"')
    else:
        ...  # TODO дописать



with open('cities.txt', 'r', encoding='utf-8') as f:
    file = f.read()

cities = file.split('\n')
random_city = random.choice(cities)
letter = last_letter(random_city)

previos_cities = set()

# Базовые настройки
root = Tk()
root.title('не Города')
root.geometry('500x500')
root.resizable(False, False)

# Поля с текстом
input_city_text = Label(root, text='Введите текст', font=('Times New Roman', 20))
answer_city_text = Label(root, text=f'{random_city}, тебе на "{letter}"', font=('Times New Roman', 20))

# Поля для ввода текста

entry = Entry(root, font=('Times New Roman', 15))

# Кнопки
button = Button(root, text='Ввод', command=no_click, font=('Times New Roman', 15))

# Упаковка кнопок и текста
input_city_text.pack()
answer_city_text.pack()
button.pack()
entry.pack()


root.mainloop()