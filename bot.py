import random
from telegram import (ParseMode)
from telegram.ext import (Updater, CommandHandler)
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
logger = logging.getLogger(__name__)
def error_callback(update, context):
logger.warning('Update "%s" caused error "%s"', update, context.error)


def start(update, context):
context.bot.send_message(update.message.chat_id, "<b>Hi Sir Use My Command /cmds</b>", parse_mode=ParseMode.HTML)


def cmds(update, context):
context.bot.send_message(update.message.chat_id, "<b>My Commands Availables: /gen</b>", parse_mode=ParseMode.HTML reply_to_message_id=reply_to_message_id.message)

def main():
	TOKEN="2073976428:AAHyWgKV5CQ6f_n6vJy3zAao_Ujy4QDoMAk"
	updater=Updater(TOKEN, use_context=True)
	dp=updater.dispatcher

	dp.add_handler(CommandHandler('start',	start))
	dp.add_handler(CommandHandler('cmds',	cmds))
	dp.add_error_handler(error_callback)
	updater.start_polling()
	updater.idle()

if __name__ == '__main__':
	print(('[Nombre del bot] Start...'))
	main()
