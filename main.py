
from config_data.config import Config, loadconfig
import asyncio
import aiogram

from aiogram import Bot, Dispatcher, F

from aiogram.client.default import DefaultBotProperties
# from aiogram.enums import ParseMode


from aiogram.filters import CommandStart, Command
from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove)
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from hadlers import other_handlers, user_handlers
from random import randint

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather
BOT_TOKEN = '7555150775:AAG1Gl0sUKuQ54nU5Z5Xz-SRoYM-8SuuUes'

# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

game = False
# Создаем список списков с кнопками
button1 = KeyboardButton(text="Давай.")
button2 = KeyboardButton(text="Не буду.")

button3 = KeyboardButton(text="камень")
button4 = KeyboardButton(text="ножницы")
button5 = KeyboardButton(text="бумага")


keyboard: list[list[KeyboardButton]] = [
    [button1, button2] 
]

game_keyboard: list[list[KeyboardButton]] = [
    [button3, button4, button5] 
]
# Создаем объект клавиатуры, добавляя в него кнопки
my_keyboard = ReplyKeyboardMarkup(
    keyboard=keyboard,
    resize_keyboard=True
)

game_keyboard = ReplyKeyboardMarkup(
    keyboard=game_keyboard,
    resize_keyboard=True
)

@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text='Привет! Сыграем в игру "камень", "ножницы", "бумага"',
        reply_markup=my_keyboard
    )

@dp.message(Command(commands="help"))
async def process_start_command(message: Message):
    await message.answer(
        text='Правила игры....',
    )
    
# Этот хэндлер будет срабатывать на остальные любые сообщения
@dp.message(F.text=='Давай.')
async def process_other_answers(message: Message):
        game = True
        await message.answer(
            # reply_markup=ReplyKeyboardRemove(),
            text='Выберите один из вариантов: ',
            reply_markup=game_keyboard
        )
answers = ['бумага', 'камень', 'ножницы']
@dp.message(F.text.in_(['камень','ножницы','бумага']))
async def process_other_answers(message: Message):
        print(message.text)
        answer = answers[randint(0,2)]
        result = 'Код не дописан.'
        if message.text == 'камень' and answer == 'бумага' or \
            message.text == 'бумага' and answer == 'ножницы' or \
            message.text == 'ножницы' and answer == 'камень':
            result = 'Я победил'
        elif message.text == 'камень' and answer == 'камень' or \
            message.text == 'бумага' and answer == 'бумага' or \
            message.text == 'ножницы' and answer == 'ножницы'    :
            result = 'Ничья'
        else:
            result = 'Ты выграл'
        game = False
        await message.answer(
            text=f'Ты показал. {message.text}. Я показал: {answer}. {result}', 
            reply_markup=ReplyKeyboardRemove()
        )
        
@dp.message(F.text=='Не буду.')
async def process_other_answers(message: Message):
        game = False
        await message.answer(
            'Сыграем в следующий раз. '
        )

if __name__ == '__main__':
    dp.run_polling(bot)