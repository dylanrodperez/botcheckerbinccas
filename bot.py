
import random
from telegram import (ParseMode)
from telegram.ext import (Updater, CommandHandler)

def start(update, context):
	''' START '''
	context.bot.send_message(update.message.chat_id, "<b>Hi Sir Use My Command /cmds</b>", parse_mode=ParseMode.HTML)


def cmds(update, context):
	''' coin '''
	context.bot.send_message(update.message.chat_id, "<b>My Commands Availables: /gen</b>", parse_mode=ParseMode.HTML)

def main():
	TOKEN="2073976428:AAHyWgKV5CQ6f_n6vJy3zAao_Ujy4QDoMAk"
	updater=Updater(TOKEN, use_context=True)
	dp=updater.dispatcher

	# Eventos que activarán nuestro bot.
	# /comandos
	dp.add_handler(CommandHandler('start',	start))
	dp.add_handler(CommandHandler('cmds',	cmds))

	dp.add_error_handler(error_callback)
    # Comienza el bot
	updater.start_polling()
    # Lo deja a la escucha. Evita que se detenga.
	updater.idle()

if __name__ == '__main__':
	print(('[Nombre del bot] Start...'))
	main()
