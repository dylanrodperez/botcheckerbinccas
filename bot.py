import random
from telegram import (ParseMode)
from telegram.ext import (Updater, CommandHandler)

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
logger = logging.getLogger(__name__)
def error_callback(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def start(update, context):
	chat_id=update.message.chat_id
	msg=f"<b>Hi Sir Send /cmds For Watch My Commands Availabes</b>"
	update.message.reply_text(msg, parse_mode=ParseMode.HTML)

def cmds(update, context):
	chat_id=update.message.chat_id
	msg="<b>My Commands Availables: <code>/gen</code></b>"
	update.message.reply_text(msg, parse_mode=ParseMode.HTML)

def main():
	TOKEN="2073976428:AAHyWgKV5CQ6f_n6vJy3zAao_Ujy4QDoMAk"
	updater=Updater(TOKEN, use_context=True)
	dp=updater.dispatcher
	dp.add_handler(CommandHandler('start',	start))

	dp.add_error_handler(error_callback)
	updater.start_polling()
	updater.idle()

