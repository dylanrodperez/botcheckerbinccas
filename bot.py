
import random
from telegram import (ParseMode)
from telegram.ext import (Updater, CommandHandler)

# [Opcional] Recomendable poner un log con los errores que apareceran por pantalla.
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
logger = logging.getLogger(__name__)
def error_callback(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def start(update, context):
	''' START '''
	# Enviar un mensaje a un ID determinado.
	context.bot.send_message(update.message.chat_id, "<b>Hi Sir Use My Command /cmds</b>", parse_mode=ParseMode.HTML)

	# Podemos llamar a otros comandos, sin que se haya activado en el chat (/help).
	coin(update, context)
def coin(update, context):
	''' ⚪️/⚫️ Moneda 
	Genera un número elatorio entre 1 y 2.
	'''
	cid=update.message.chat_id
	msg="⚫️ Cara" if random.randint(1,2)==1 else "⚪️ Cruz"
	# Responde directametne en el canal donde se le ha hablado.
	update.message.reply_text(msg)

def main():
	TOKEN="2073976428:AAHyWgKV5CQ6f_n6vJy3zAao_Ujy4QDoMAk"
	updater=Updater(TOKEN, use_context=True)
	dp=updater.dispatcher

	# Eventos que activarán nuestro bot.
	# /comandos
	dp.add_handler(CommandHandler('start',	start))
	dp.add_handler(CommandHandler('coin',	coin))

	dp.add_error_handler(error_callback)
    # Comienza el bot
	updater.start_polling()
    # Lo deja a la escucha. Evita que se detenga.
	updater.idle()

if __name__ == '__main__':
	print(('[Nombre del bot] Start...'))
	main()
