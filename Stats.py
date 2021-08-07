from telegram import InlineKeyboardMarkup, InlineKeyboardButton, ChatAction
import telebot
import os

tb=telebot.TeleBot(os.environ.get("TOKEN_AXIEFUTUREBOT"))

button_vitalidad=InlineKeyboardButton(text="Vitalidad", callback_data="vitalidad")
button_velocidad=InlineKeyboardButton(text="Velocidad", callback_data="velocidad")
button_habilidad=InlineKeyboardButton(text="Habilidad", callback_data="habilidad")
button_moral=InlineKeyboardButton(text="Moral", callback_data="moral")
button_start=InlineKeyboardButton(text="Volver al menu principal", callback_data="start")

def estadisticas(update, context):

    query=update.callback_query
    query.answer()

    query.edit_message_text(text="¿Estadisticas? ¡Así es!\n\n"\
        "Los Axies tienen 4 estaditicas basicas, estas son determinadas por el tipo de Axie "\
        "y por sus partes. Estas 4 estadisticas basicas son: Vitalidad, Velocidad, Habilidad y Moral\n\n"\
        "Indique de cual desea conocer más al respecto: \n\n",
    reply_markup=InlineKeyboardMarkup([
        [button_vitalidad],
        [button_velocidad],
        [button_habilidad],
        [button_moral],
        [button_start]
    ]))

def vitalidad(update, context):

    query=update.callback_query
    query.answer()

    query.edit_message_text(text="¡Vitalidad!\n\n"\
        "La vitalidad son los puntos maximos de vida de un Axie, estos determinan "\
        "la cantidad de daño que un Axie puede soportar antes de ser noqueado\n\n"\
        "Gracias por usar AxieFutureBot\n"\
        "Para volver a vernos escribe \"/start\"\n\n"
    )

    chat_id=update.effective_message.chat.id

    chat=update.effective_message.chat
    
    chat.send_action(
        action=ChatAction.UPLOAD_PHOTO,
        timeout=None
    )
    
    tb.send_sticker(chat_id,open("imagenes/webp/vitalidad_1.webp", "rb"))

def velocidad(update, context):

    query=update.callback_query
    query.answer()

    query.edit_message_text(text="¡Velocidad!\n\n"\
        "La velocidad determina el orden de los turnos. Los axies más rapidos atacan primero. "\
        "La velocidad tambien disminuye la posibilidad de que un Axie sea "\
        "victima de un golpe critico\n\n"\
        "Gracias por usar AxieFutureBot\n"\
        "Para volver a vernos escribe \"/start\"\n\n"
    )

    chat_id=update.effective_message.chat.id

    chat=update.effective_message.chat
    
    chat.send_action(
        action=ChatAction.UPLOAD_PHOTO,
        timeout=None
    )
    
    tb.send_sticker(chat_id,open("imagenes/webp/velocidad_1.webp", "rb"))

def habilidad(update, context):

    query=update.callback_query
    query.answer()

    query.edit_message_text(text="¡Habilidad!\n\n"\
        "La habilidad (Skill) añade daño cuando un Axie juega varias cartas "\
        "a la vez (Es decir cuando hace un combo)\n\n"\
        "Gracias por usar AxieFutureBot\n"\
        "Para volver a vernos escribe \"/start\"\n\n"
    )

    chat_id=update.effective_message.chat.id

    chat=update.effective_message.chat
    
    chat.send_action(
        action=ChatAction.UPLOAD_PHOTO,
        timeout=None
    )
    
    tb.send_sticker(chat_id,open("imagenes/webp/habilidad_1.webp", "rb"))

def moral(update, context):

    query=update.callback_query
    query.answer()

    query.edit_message_text(text="¡Moral!\n\n"\
        "La moral aumenta la probablidad de golpe critico. Tambien hace que sea más "\
        "probable entrar en modo \"Ultima batalla\" y añade más \"ticks\" de Ultima batalla\n\n"\
        "Gracias por usar AxieFutureBot\n"\
        "Para volver a vernos escribe \"/start\"\n\n"
    )

    chat_id=update.effective_message.chat.id

    chat=update.effective_message.chat
    
    chat.send_action(
        action=ChatAction.UPLOAD_PHOTO,
        timeout=None
    )
    
    tb.send_sticker(chat_id,open("imagenes/webp/moral_1.webp", "rb"))