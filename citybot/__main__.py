import os
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from dotenv import load_dotenv
from citybot.city_know_bot import  user_city_message_received, greet_user

time_format = '%Y-%m-%d %H:%M:%S'
logger = logging.getLogger(__name__)
logging.basicConfig(filename='bot.log',
                    level=logging.INFO,
                    encoding='utf-8', format='%(asctime)s - %(message)s',
                    datefmt=time_format)
load_dotenv()
token = os.getenv('token')

def main():
    mybot = Updater(token, use_context=True)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, user_city_message_received))
    logger.info('Бот стартовал')
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()