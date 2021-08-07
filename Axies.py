from telegram import InlineKeyboardMarkup, InlineKeyboardButton, ChatAction
import telebot
import os

tb=telebot.TeleBot(os.environ.get("TOKEN_AXIEFUTUREBOT"))

button_info=InlineKeyboardButton(text="Más información", url="https://whitepaper.axieinfinity.com/")

def juego(update, context):

    query=update.callback_query
    query.answer()

    query.edit_message_text(text="¿Has escuchado de Axie Infinty pero no te queda claro que es?\n\n"\
        "¡No te procupes! Ahora lo entenderas todo. "\
        "Axie Infinity es un juego de mascotas donde los jugadores luchan, crian y comercian "\
        "con criaturas de fantasia llamadas Axies\n\n"\
        "El juego fue desarrollado por Sky Mavis y esta claramente inspirado en juegos como pokemon o tamagochi, "\
        "ademas de tener fuertes influencias de juegos de cartas\n\n"\
        "Algunos socios del proyecto Axie Infinity son: Samsung, Ubisoft y Binance, etc...\n\n"\
        "Gracias por usar AxieFutureBot\n"\
        "Para volver a vernos escribe \"/start\"\n\n",
    reply_markup=InlineKeyboardMarkup([
        [button_info]
    ]))

    chat_id=update.effective_message.chat.id

    chat=update.effective_message.chat
    
    chat.send_action(
        action=ChatAction.UPLOAD_PHOTO,
        timeout=None
    )
    
    tb.send_sticker(chat_id,open("imagenes/webp/juego.webp", "rb"))

def axie(update, context):

    query=update.callback_query
    query.answer()

    query.edit_message_text(text="¿Quieres saber que es un Axie?\n\n"\
        "¡Genial! veamos...\n\n"\
        "Los Axies son las adorables y feroces criaturas que protagonizan Axie Infinity. "\
        "Viven dentro del mundo de Lunacia y seran nuestras mascotas. "\
        "Mascotas que usaremos para pelear contra otros jugadores y enemigos del juego en combates por turnos en tiempo real\n\n"\
        "Gracias por usar AxieFutureBot\n"\
        "Para volver a vernos escribe \"/start\"\n\n"
    )

    chat_id=update.effective_message.chat.id

    chat=update.effective_message.chat
    
    chat.send_action(
        action=ChatAction.UPLOAD_PHOTO,
        timeout=None
    )
    
    tb.send_sticker(chat_id,open("imagenes/webp/axie.webp", "rb"))