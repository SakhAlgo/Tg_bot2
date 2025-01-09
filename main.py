from config_data.config import load_config

conf = load_config('.env')

bot_token = conf.tg_bot.token
print(bot_token)
