import os
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from dotenv import load_dotenv

from citybot.city_know_bot import  play_city_game, greet_user


logging.basicConfig(filename='bot.log', level=logging.INFO)
load_dotenv()
token = os.getenv('token')

def main():
    mybot = Updater(token, use_context=True)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, play_city_game))
    logging.info('Бот стартовал')
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()