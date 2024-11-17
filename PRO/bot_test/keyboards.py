from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def start_kbs():
    kb = [
        [InlineKeyboardButton(text='Начать', callback_data='start')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=kb)


def start_test_kbs():
    kb = [
        [InlineKeyboardButton(text='Начать тест', callback_data='quests')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=kb)