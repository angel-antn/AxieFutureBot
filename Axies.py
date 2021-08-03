from telegram import InlineKeyboardMarkup, InlineKeyboardButton

button_info=InlineKeyboardButton(text="Más información", url="https://whitepaper.axieinfinity.com/")
button_start=InlineKeyboardButton(text="Volver al menu principal", callback_data="start")

def juego(update, context):

    query=update.callback_query
    query.answer()

    query.edit_message_text(text="¿Has escuchado de Axie Infinty pero no te queda claro que es?\n\n"\
        "¡No te procupes! Ahora lo entenderas todo\n\n"\
        "Axie Infinity es un juego de mascotas donde los jugadores luchan, crian y comercian "\
        "con criaturas de fantasia llamadas Axies\n\n"\
        "El juego fue desarrollado por Sky Mavis y esta claramente inspirado en juegos como pokemon o tamagochi, "\
        "ademas de tener fuertes influencias de juegos de cartas\n\n"\
        "Algunos socios del proyecto Axie Infinity son: Samsung, Ubisoft y Binance, etc...\n\n",
    reply_markup=InlineKeyboardMarkup([
        [button_info],
        [button_start]
    ]))

def axie(update, context):

    query=update.callback_query
    query.answer()

    query.edit_message_text(text="¿Quieres saber que es un Axie?\n\n"\
        "¡Genial! veamos...\n\n"\
        "Los Axies son las adorables y feroces criaturas que protagonizan Axie Infinity. "\
        "Viven dentro del mundo de Lunacia y seran nuestras mascotas. "\
        "Mascotas que usaremos para pelear contra otros jugadores y enemigos del juego en combates por turnos en tiempo real\n\n",
    reply_markup=InlineKeyboardMarkup([
        [button_start]
    ]))