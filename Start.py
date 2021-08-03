from telegram import InlineKeyboardMarkup, InlineKeyboardButton

button_juego=InlineKeyboardButton(text="¿Que es Axie infinity?", callback_data="juego")
button_axie=InlineKeyboardButton(text="¿Que es un Axie?", callback_data="axie")
button_tipos=InlineKeyboardButton(text="Tipos de Axies", callback_data="tipos")
button_efectividad=InlineKeyboardButton(text="Efectividad de ataques", callback_data="efectividad")
button_github=InlineKeyboardButton(text="Visitar Github", url="https://github.com/angel-antn/AxieFutureBot")


def start(update, context):

    update.message.reply_text(text="¡Bienvenido a AxieFutureBot!\n\n"\
    "El bot destinado a servir como recurso auxiliar para aquellas personas "\
    "que recien empiezan en el mundo de Axie Infinity.\n\n"\
    "Seleccione una opcion para continuar: ",
    reply_markup=InlineKeyboardMarkup([
        [button_juego],
        [button_axie],
        [button_tipos],
        [button_efectividad],
        [button_github]
    ]))

def start_again(update, context):

    query=update.callback_query
    query.answer()

    query.edit_message_text(text="¡Bienvenido a AxieFutureBot!\n\n"\
    "El bot destinado a servir como recurso auxiliar para aquellas personas "\
    "que recien empiezan en el mundo de Axie Infinity.\n\n"\
    "Seleccione una opcion para continuar: ",
    reply_markup=InlineKeyboardMarkup([
        [button_juego],
        [button_axie],
        [button_tipos],
        [button_efectividad],
        [button_github]
    ]))