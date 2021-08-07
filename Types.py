from telegram import InlineKeyboardMarkup, InlineKeyboardButton, ChatAction
import telebot
import os

tb=telebot.TeleBot(os.environ.get("TOKEN_AXIEFUTUREBOT"))

button_tipos_secretos=InlineKeyboardButton(text="¿Tipos secretos?", callback_data="secretos")
button_start=InlineKeyboardButton(text="Volver al menu principal", callback_data="start")

button_bestia=InlineKeyboardButton(text="Bestia", callback_data="bestia")
button_aqua=InlineKeyboardButton(text="Aqua", callback_data="aqua")
button_planta=InlineKeyboardButton(text="Planta", callback_data="planta")
button_ave=InlineKeyboardButton(text="Ave", callback_data="ave")
button_bicho=InlineKeyboardButton(text="Bicho", callback_data="bicho")
button_reptil=InlineKeyboardButton(text="Reptil", callback_data="reptil")

button_meca=InlineKeyboardButton(text="Meca", callback_data="meca")
button_alba=InlineKeyboardButton(text="Alba", callback_data="alba")
button_ocaso=InlineKeyboardButton(text="Ocaso", callback_data="ocaso")

def tipos(update, context):

    query=update.callback_query
    query.answer()

    query.edit_message_text(text="Veamos...\n\n"\
        "Existen 9 tipos de Axies: Bestia, Aqua, Planta, Ave, Bicho, Reptil y "\
        "3 más que son \"secretos\"\n\n",
    reply_markup=InlineKeyboardMarkup([
        [button_bestia],
        [button_aqua],
        [button_planta],
        [button_ave],
        [button_bicho],
        [button_reptil],
        [button_tipos_secretos],
        [button_start]
    ]))

def bestia(update, context):

    query=update.callback_query
    query.answer()

    query.edit_message_text(text="¡Bestia!\n\nEste tipo de Axie se concentra en acertar "\
        "buenos golpes criticos. "\
        "Son Axies capaces de obtener el maximo de moral\n\nGracias por usar AxieFutureBot\n"\
        "Para volver a vernos escribe \"/start\"\n\n"
    )

    chat_id=update.effective_message.chat.id

    chat=update.effective_message.chat
    
    chat.send_action(
        action=ChatAction.UPLOAD_PHOTO,
        timeout=None
    )
    
    tb.send_sticker(chat_id,open("imagenes/webp/bestia.webp", "rb"))

def aqua(update, context):

    query=update.callback_query
    query.answer()

    query.edit_message_text(text="¡Aqua!\n\nEste tipo de Axie tiene un equilibrio "\
        "entre vida y velocidad. Su mayor desventaja es su baja moral, "\
        "sin embargo, no es impedimento para ser considerado uno de los mejores "\
        "tipos dentro del juego\n\nGracias por usar AxieFutureBot\n"\
        "Para volver a vernos escribe \"/start\"\n\n"
    )

    chat_id=update.effective_message.chat.id

    chat=update.effective_message.chat
    
    chat.send_action(
        action=ChatAction.UPLOAD_PHOTO,
        timeout=None
    )
    
    tb.send_sticker(chat_id,open("imagenes/webp/aqua.webp", "rb"))

def planta(update, context):
    
    query=update.callback_query
    query.answer()

    query.edit_message_text(text="¡Planta!\n\nEste tipo de Axie es una verdadera muralla "\
        "por excelencia, su funcion es resistir lo más que se pueda para que "\
        "tus demas Axies hagan el mayor daño posible\n\nGracias por usar AxieFutureBot\n"\
        "Para volver a vernos escribe \"/start\"\n\n"
    )

    chat_id=update.effective_message.chat.id

    chat=update.effective_message.chat
    
    chat.send_action(
        action=ChatAction.UPLOAD_PHOTO,
        timeout=None
    )
    
    tb.send_sticker(chat_id,open("imagenes/webp/planta.webp", "rb"))

def ave(update, context):

    query=update.callback_query
    query.answer()

    query.edit_message_text(text="¡Ave!\n\nNo existen Axies más rapidos dentro del juego, "\
        "y a eso sumale el buen daño que tienen, "\
        "sin embargo su cantidad de vida es poca\n\nGracias por usar AxieFutureBot\n"\
        "Para volver a vernos escribe \"/start\"\n\n"
    )

    chat_id=update.effective_message.chat.id

    chat=update.effective_message.chat
    
    chat.send_action(
        action=ChatAction.UPLOAD_PHOTO,
        timeout=None
    )
    
    tb.send_sticker(chat_id,open("imagenes/webp/ave.webp", "rb"))

def bicho(update, context):
    
    query=update.callback_query
    query.answer()

    query.edit_message_text(text="¡Bicho!\n\nSon Axies con multiples funciones, "\
        "desde dar soporte al equipo hasta usar sus habilidades de control, "\
        "sin embargo, es mejor que alguien avanzado las use\n\nGracias por usar AxieFutureBot\n"\
        "Para volver a vernos escribe \"/start\"\n\n"
    )

    chat_id=update.effective_message.chat.id

    chat=update.effective_message.chat
    
    chat.send_action(
        action=ChatAction.UPLOAD_PHOTO,
        timeout=None
    )
    
    tb.send_sticker(chat_id,open("imagenes/webp/bicho.webp", "rb"))

def reptil(update, context):
    
    query=update.callback_query
    query.answer()

    query.edit_message_text(text="¡Reptil!\n\nParecidos a los acuaticos si... "\
        "pero con más moral, vida y cartas de armadura\n\nGracias por usar AxieFutureBot\n"\
        "Para volver a vernos escribe \"/start\"\n\n"
    )

    chat_id=update.effective_message.chat.id

    chat=update.effective_message.chat
    
    chat.send_action(
        action=ChatAction.UPLOAD_PHOTO,
        timeout=None
    )
    
    tb.send_sticker(chat_id,open("imagenes/webp/reptil.webp", "rb"))

def secretos(update, context):

    query=update.callback_query
    query.answer()

    query.edit_message_text(text="¿Tipos secretos?\n\nbueno... no del todo...\n\n"\
        "Los 3 tipos secretos son Meca, Alba y Ocaso. Se consideran \"secretos\" por "\
        "ser raros de conseguir. Ademas, no poseen cartas\n\n",
    reply_markup=InlineKeyboardMarkup([
        [button_meca],
        [button_alba],
        [button_ocaso],
        [button_start]
    ]))

def meca(update, context):

    query=update.callback_query
    query.answer()

    query.edit_message_text(text="¡Meca!\n\nAxies capaces de hacer grandes combos "\
        "gracias a su alta habilidad (Skill), combos que hacen más daño y habilidades "\
        "defensivas que protegen más. Estos Axies se pueden conseguir mezclando un Axie "\
        "tipo Bicho puro y un Axie tipo Bestia puro\n\nGracias por usar AxieFutureBot\n"\
        "Para volver a vernos escribe \"/start\"\n\n"
    )

    chat_id=update.effective_message.chat.id

    chat=update.effective_message.chat
    
    chat.send_action(
        action=ChatAction.UPLOAD_PHOTO,
        timeout=None
    )
    
    tb.send_sticker(chat_id,open("imagenes/webp/meca.webp", "rb"))

def alba(update, context):
    
    query=update.callback_query
    query.answer()

    query.edit_message_text(text="¡Alba!\n\nAxies algo similares a los meca, "\
        "aunque con un poco mas de vida. Estos Axies se pueden conseguir mezclando un "\
        "Axie tipo Ave puro y un Axie tipo Planta puro\n\nGracias por usar AxieFutureBot\n"\
        "Para volver a vernos escribe \"/start\"\n\n"
    )

    chat_id=update.effective_message.chat.id

    chat=update.effective_message.chat
    
    chat.send_action(
        action=ChatAction.UPLOAD_PHOTO,
        timeout=None
    )
    
    tb.send_sticker(chat_id,open("imagenes/webp/alba.webp", "rb"))

def ocaso(update, context):
    
    query=update.callback_query
    query.answer()

    query.edit_message_text(text="¡Ocaso!\n\nAxies con poca moral, pero mucha vida y "\
        "velocidad. Estos Axies se pueden conseguir mezclando un Axie tipo Reptil "\
        "puro y un Axie tipo Aqua puro\n\nGracias por usar AxieFutureBot\n"\
        "Para volver a vernos escribe \"/start\"\n\n"
    )

    chat_id=update.effective_message.chat.id

    chat=update.effective_message.chat
    
    chat.send_action(
        action=ChatAction.UPLOAD_PHOTO,
        timeout=None
    )
    
    tb.send_sticker(chat_id,open("imagenes/webp/ocaso.webp", "rb"))