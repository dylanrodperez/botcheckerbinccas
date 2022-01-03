import random
from telegram import (ParseMode)
from telegram.ext import (Updater, CommandHandler)

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
logger = logging.getLogger(__name__)
def error_callback(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def start(update, context):
context.bot.send_message(update.message.chat_id, "Hi Sir Use My Command: /cmds", parse_mode=ParseMode.HTML)

coin(update, context)
def coin(update, context):
cid=update.message.chat_id
msg="⚫️ Cara" if random.randint(1,2)==1 else "⚪️ Cruz"
update.message.reply_text(msg)

def main():
TOKEN="2073976428:AAHyWgKV5CQ6f_n6vJy3zAao_Ujy4QDoMAk"
updater=Updater(TOKEN, use_context=True)
dp=updater.dispatcher

dp.add_handler(CommandHandler('start',	start))
dp.add_handler(CommandHandler('coin',	coin))

dp.add_error_handler(error_callback)
updater.start_polling()
updater.idle()

if __name__ == '__main__':
	print(('[Nombre del bot] Start...'))
	main()
