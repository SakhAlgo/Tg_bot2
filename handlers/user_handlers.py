from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.keyboards import my_keyboard, game_keyboard
from random import randint
from lexicon.lexicon import LEXICON_RU
# from services.services import get_bot_choice, get_winner

router = Router()

@router.message(Command(commands='delmenu'))
async def del_main_menu(message, bot):
    await bot.delete_my_commands()
    await message.answer(text='Кнопка меню удалена')

@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text=LEXICON_RU['/start'],
        reply_markup=my_keyboard
    )

@router.message(Command(commands="help"))
async def process_start_command(message: Message):
    await message.answer(
        text=LEXICON_RU['/help'],
    )
    
# Этот хэндлер будет срабатывать на остальные любые сообщения
@router.message(F.text==LEXICON_RU['yes_button'])
async def process_other_answers(message: Message):
        game = True
        await message.answer(
            # reply_markup=ReplyKeyboardRemove(),
            text=LEXICON_RU['yes'],
            reply_markup=game_keyboard
        )
answers = [LEXICON_RU['rock'], LEXICON_RU['paper'], LEXICON_RU['scissors']]
@router.message(F.text.in_(answers))
async def process_other_answers(message: Message):
        print(message.text)
        answer = answers[randint(0,2)]
        result = LEXICON_RU['other_answer']
        if message.text == LEXICON_RU['rock'] and answer == LEXICON_RU['paper'] or \
            message.text == LEXICON_RU['paper'] and answer == LEXICON_RU['scissors'] or \
            message.text == LEXICON_RU['scissors'] and answer == LEXICON_RU['rock']:
            result = '😋' +LEXICON_RU['bot_won'] 
        elif message.text == LEXICON_RU['rock'] and answer == LEXICON_RU['rock']or \
            message.text == LEXICON_RU['paper'] and answer == LEXICON_RU['paper'] or \
            message.text == LEXICON_RU['scissors'] and answer == LEXICON_RU['scissors']:
            result = "😬" + LEXICON_RU['nobody_won']
        else:
            result = "👍" + LEXICON_RU['user_won']

        await message.answer(
            text=f'Ты показал: {message.text}. Я показал: {answer}. \n        {result}' 
            # reply_markup=ReplyKeyboardRemove()
        )
        
@router.message(F.text==LEXICON_RU['no_button'])
async def process_other_answers(message: Message):
        game = False
        await message.answer(
            text = LEXICON_RU['by-by'],
            reply_markup=ReplyKeyboardRemove()
        )

