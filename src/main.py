import logging
import os

import dotenv
from telegram import Update
from telegram.ext import (
    CallbackContext,
    CommandHandler,
    Filters,
    MessageHandler,
    Updater,
    CallbackQueryHandler
)

from commands import test, echo, start, button

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
dotenv.load_dotenv(dotenv.find_dotenv())

# Create bot
API_KEY = os.getenv("TELEGRAM_API_KEY")
updater = Updater(token=API_KEY)
dispatcher = updater.dispatcher

# Add commands and message handlers
start_handler = CommandHandler("start", start)
dispatcher.add_handler(start_handler)

# echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
# dispatcher.add_handler(echo_handler)

test_handler = CommandHandler("test", test)
dispatcher.add_handler(test_handler)
updater.dispatcher.add_handler(CallbackQueryHandler(button))


# Start bot
updater.start_polling()
