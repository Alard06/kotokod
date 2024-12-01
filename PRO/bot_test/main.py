import os
import random

import dotenv
import asyncio

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command, CommandStart
from keyboards import start_kbs, start_test_kbs

dotenv.load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

users = dict()
user_question = dict()  # Хранится индекс вопроса. {'tg_id': 2}

@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer('Здравствуйте! Я бот', reply_markup=start_kbs())

@dp.callback_query()
async def callback_query(callback: types.CallbackQuery):
    command = callback.data

    if command == 'start':
        await callback.message.answer('Вы попали в бота, в котором проводится тест на знание Python!'
                                      , reply_markup=start_test_kbs())
    print(callback.from_user.id)

async def quest(chatid, userid):
    lvl = users[userid]
    lel = question[lvl]

    index = random.randint(0, len(lel['quest']-1))
    question = question['quest'][index]
    correct = question['answer_true'][index]
    false_answers = question['answer_false'][index]

    options = [correct] + false_answers
    random.shuffle(options)

    buttons = [[InlineKeyboardButton(text=opt, callback_data=opt) for opt in options]]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    await bot.send_message(chatid, question, reply_markup=keyboard)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
