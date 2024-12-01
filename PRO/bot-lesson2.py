import asyncio
import random


from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command, CommandStart
from aiogram.types import InputFile
from aiogram.types import FSInputFile

API_TOKEN = '8194121363:AAHr_6_mXomKWF-2hd6nmSetaeFemLnm3B8'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()


users = []

@dp.message(CommandStart())
async def start(message: types.Message):
    global users
    users.append(message.from_user.id)
    await message.answer('Привет, я бот')


@dp.message()
async def echo(message: types.Message):
    if message.text in 'приветhellohi':
        await message.answer('ну hello')
    elif message.text in 'как дела какдела':
        answers = ['плохо', 'ok', 'хорошо', 'норм']
        await message.answer(random.choice(answers))
    elif message.text.lower() == 'шрифты':
        text = """
        <b> Python </b>
        <a href='https://google.com'>Google</a>
        <u>Test </u>
        <em> Python2 </em>
        """
        await message.answer(text, parse_mode='html')
    elif message.text.lower() == 'emoji':
        await message.answer('😎😂😊😆😋😘🤩🤗😐😶😏😫😜')
    elif message.text.lower() == 'sticker':
        await bot.send_sticker(chat_id=message.chat.id, sticker='CAACAgIAAxkBAAENQHlnTA-kI_Egv5ttp1y21bm-1tcv6gACOBYAAhLqyUrmYRkf4nWoIzYE')
    elif message.text.lower() == 'флуд':
        for user_id in users:
            await bot.send_message(user_id, 'это спам флуд')
            await asyncio.sleep(0.1)
    elif message.text.lower() == 'фото':
        # input_file = InputFile('tesdt.png')
        input_file = FSInputFile('tesdt.png')
        await message.answer_photo(photo=input_file, caption='Тестовое фото')
        ...
    elif message.text.lower() == 'фото из интернета':
        await message.answer_photo('https://avatars.mds.yandex.net/i?id=af696da68685b4513a5d4bff4da7e42b_l-5667950-images-thumbs&n=13')
    # await message.answer(message.text)

# 50

async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
