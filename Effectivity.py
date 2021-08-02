from telegram import InlineKeyboardMarkup, InlineKeyboardButton, ChatAction
import telebot
import os

tb=telebot.TeleBot(os.environ.get("TOKEN_AXIEFUTUREBOT"))

button_reptil=InlineKeyboardButton(text="Reptil", callback_data="ataque_reptil")
button_planta=InlineKeyboardButton(text="Planta", callback_data="ataque_planta")

button_aqua=InlineKeyboardButton(text="Aqua", callback_data="ataque_aqua")
button_ave=InlineKeyboardButton(text="Ave", callback_data="ataque_ave")

button_bestia=InlineKeyboardButton(text="Bestia", callback_data="ataque_bestia")
button_bicho=InlineKeyboardButton(text="Bicho", callback_data="ataque_bicho")

button_start=InlineKeyboardButton(text="Volver al menu principal", callback_data="start")

def ataque(update, context):

    query=update.callback_query
    query.answer()

    query.edit_message_text(text="¡Excelente!\n\n"\
        "Ahora empecemos...\n"\
        "Para poder calcular la efectividad de sus ataque, debe indicar de que tipo son:",
    reply_markup=InlineKeyboardMarkup([
        [button_reptil],
        [button_planta],
        [button_aqua],
        [button_ave],
        [button_bestia],
        [button_bicho],
        [button_start]
    ]))

def image_effectivity(update, context):

    query=update.callback_query
    query.answer()

    query.edit_message_text(text="¡La guia va en camino!\n\n"\
        "Gracias por usar AxieFutureBot\n"\
        "Para volver a vernos escribe \"/start\""
    )

    chat_id=update.effective_message.chat.id

    chat=update.effective_message.chat
    
    chat.send_action(
        action=ChatAction.UPLOAD_PHOTO,
        timeout=None
    )
    
    tb.send_photo(chat_id,open("imagenes/fortalezas_debilidades.png", "rb"))