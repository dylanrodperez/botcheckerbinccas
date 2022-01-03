# -*- coding: utf-8 -*-

from telegram.ext import (Updater, CommandHandler)

def start(update, context):
	''' START '''
	# Enviar un mensaje a un ID determinado.
	context.bot.send_message(update.message.chat_id, "Bienvenido")

def main():
	TOKEN="2073976428:AAHyWgKV5CQ6f_n6vJy3zAao_Ujy4QDoMAk"
	updater=Updater(TOKEN, use_context=True)
	dp=updater.dispatcher

	# Eventos que activarán nuestro bot.
	dp.add_handler(CommandHandler('start',	start))

	# Comienza el bot
	updater.start_polling()
	# Lo deja a la escucha. Evita que se detenga.
	updater.idle()

if __name__ == '__main__':
	main()
