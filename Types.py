from telegram import InlineKeyboardMarkup, InlineKeyboardButton

button_tipos_secretos=InlineKeyboardButton(text="¿Tipos secretos?", callback_data="secretos")
button_start=InlineKeyboardButton(text="Volver al menu principal", callback_data="start")

def tipos(update, context):

    query=update.callback_query
    query.answer()

    query.edit_message_text(text="¡Excelente!\n\n"\
        "Veamos...\n"\
        "Existen 9 tipos de Axies: Bestia, Aqua, Planta, Ave, Bicho, Reptil y 3 más que son \"secretos\"\n\n"\
        "¡Bestia! Este tipo de Axie se concentra en acertar buenos golpes criticos. "\
        "Son Axies capaces de obtener el maximo de moral (la moral determina tu daño critico)\n\n"\
        "¡Aqua! Este tipo de Axie tiene un equilibrio entre vida y velocidad. Su mayor desventaja es su baja moral, "\
        "sin embargo, no es impedimento para ser considerado uno de los mejores tipos dentro del juego\n\n"\
        "¡Planta! Este tipo de Axie es una verdadera muralla por excelencia, su funcion es resistir lo más que se pueda para que "\
        "tus demas Axies hagan el mayor daño posible\n\n"\
        "¡Ave! No existen Axies más rapidos dentro del juego, y a eso sumale el buen daño que tienen, "\
        "sin embargo su cantidad de vida es poca\n\n"\
        "¡Bicho! Son Axies con multiples funciones, desde dar soporte al equipo hasta usar sus habilidades de control, "\
        "sin embargo, es mejor que alguien avanzado las use\n\n"\
        "¡Reptil! Parecidos a los acuaticos si... pero con más moral, vida y cartas de armadura\n\n",
    reply_markup=InlineKeyboardMarkup([
        [button_tipos_secretos],
        [button_start]
    ]))

def secretos(update, context):

    query=update.callback_query
    query.answer()

    query.edit_message_text(text="¿Tipos secretos?\n\nbueno... no del todo...\n\n"\
        "Los 3 tipos secretos son Meca, Alba y Ocaso. Se consideran \"secretos\" por ser raros de conseguir. Ademas, no poseen cartas\n\n"\
        "¡Meca! Axies capaces de hacer grandes combos gracias a su alta Skill, combos que hacen más daño y habilidades "\
        "defensivas que protegen más. Estos Axies se pueden conseguir mezclando un Axie tipo Bicho puro y un Axie tipo Bestia puro\n\n"\
        "¡Alba! Axies algo similares a los meca, aunque con un poco mas de vida. Estos Axies se pueden conseguir mezclando un Axie tipo Ave puro y un Axie tipo Planta puro\n\n"\
        "¡Ocaso! Axies con poca moral, pero mucha vida y velocidad. Estos Axies se pueden conseguir mezclando un Axie tipo Reptil puro y un Axie tipo Aqua puro\n\n",
    reply_markup=InlineKeyboardMarkup([
        [button_start]
    ]))


