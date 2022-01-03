import os
import telegram
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler


def handle_start(update, context):
   yourname = update.message.chat.first_name

    msg = "Hi "+yourname+"! Welcome to mimic bot."
    context.bot.send_message(update.message.chat.id, msg)


if __name__ == '__main__':

    token = os.environ['TOKEN']

    bot = telegram.Bot(token=token)

    updater = Updater(token=token, use_context=True)

    dp = updater.dispatcher
    dp.add_handler(
        CommandHandler('start', handle_start)
    )

    updater.start_polling()

    print(f'running at @{bot.username}')

    updater.idle()
