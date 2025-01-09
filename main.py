from config_data.config import load_config
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

config = load_config('.env')

bot = Bot(token=config.tg_bot.token)
dp = Dispatcher()

some_var_1 = 1
some_var_2 = 'Some text'

dp.workflow_data.update({'my_int_var': some_var_1, 'my_text_var': some_var_2})


@dp.message(Command(commands='start'))
async def process_start_command(message: Message, my_int_var, my_text_var):
    await message.answer(text=str(my_int_var))
    await message.answer(text=my_text_var)
    
if __name__ == '__main__':
    dp.run_polling(bot)