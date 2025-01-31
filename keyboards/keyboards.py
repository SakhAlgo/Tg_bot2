from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove)
from lexicon.lexicon import LEXICON_RU

# Создаем список списков с кнопками
button1 = KeyboardButton(text=LEXICON_RU['yes_button'])
button2 = KeyboardButton(text=LEXICON_RU['no_button'])

button3 = KeyboardButton(text=LEXICON_RU['rock'])
button4 = KeyboardButton(text=LEXICON_RU['scissors'])
button5 = KeyboardButton(text=LEXICON_RU['paper'])
button6 = KeyboardButton(text=LEXICON_RU['no_button'])

keyboard: list[list[KeyboardButton]] = [
    [button1, button2] 
]

game_keyboard: list[list[KeyboardButton]] = [
    [button3, button4, button5, button6] 
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
