
from config_data.config import Config, load_config
import asyncio
import logging

from aiogram import Bot, Dispatcher, F

from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode 

from aiogram.filters import CommandStart, Command
from aiogram.types import Message, ReplyKeyboardRemove, BotCommand

from keyboards.keyboards import my_keyboard, game_keyboard
from keyboards.set_menu import set_menu

from handlers import other_handlers, user_handlers
from lexicon.lexicon import LEXICON_RU


# Инициализатор логгера
logger = logging.getLogger(__name__)

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather
# BOT_TOKEN = '7555150775:AAG1Gl0sUKuQ54nU5Z5Xz-SRoYM-8SuuUes'

async def main():
    # создаем комманды в списке меню

    # Конфигурируем логирование
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')
    config = load_config()

    # Создаем объекты бота и диспетчера
    bot = Bot(
        token=config.tg_bot.token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    dp = Dispatcher()
    
    await set_menu(bot)
    # db.startup.register(set_main_menu)
    # Регистриуем роутеры в диспетчере
    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)



asyncio.run(main())