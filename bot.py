from config_data.config import load_config

config = load_config()

bot_token = config.tg_bot.token
admin = config.tg_bot.admin_ids

print(bot_token, admin)
