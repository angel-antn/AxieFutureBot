import os
from telegram.ext import Updater, CommandHandler
from telegram import InlineKeyboardMarkup, InlineKeyboardButton

def start(update, context):

    button_github=InlineKeyboardButton(text="Visitar Github", url="https://github.com/angel-antn/AxieFutureBot")

    update.message.reply_text(text="¡Bienvenido a AxieFutureBot!\n\n"\
    "El bot destinado a servir como recurso auxiliar para aquellas personas "\
    "que recien empiezan en el mundo de Axie Infinity.\n\n"\
    "Seleccione una opcion para continuar: ",
    reply_markup=InlineKeyboardMarkup([
        [button_github]
    ]))

if __name__ == "__main__":

    updater = Updater(token=os.environ.get("TOKEN_AXIEFUTUREBOT"),use_context=True)
    
    updater.dispatcher.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()