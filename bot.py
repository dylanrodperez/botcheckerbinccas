import os
import telegram
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler


def handle_start(update, context):

    update.message.reply_text(
        text=(
            'This bot has been migrated to a new one: @ForwarderGeniusBot.'
            '\nGo there and run /start to continue'
        ),
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Go to the bot', url='https://t.me/ForwarderGeniusBot')]
        ])
    )


if __name__ == '__main__':

    token = "2073976428:AAHyWgKV5CQ6f_n6vJy3zAao_Ujy4QDoMAk2073976428:AAHyWgKV5CQ6f_n6vJy3zAao_Ujy4QDoMAk"

    bot = telegram.Bot(token=token)

    updater = Updater(token=token, use_context=True)

    dp = updater.dispatcher
    dp.add_handler(
        CommandHandler('start', handle_start)
    )

    updater.start_polling()

    print(f'running at @{bot.username}')

    updater.idle()
