from telegram import InlineKeyboardMarkup, InlineKeyboardButton

button_grupo2_y=InlineKeyboardButton(text="Si son del mismo tipo", callback_data="ataque_grupo2_y")
button_grupo2_n=InlineKeyboardButton(text="No son del mismo tipo", callback_data="ataque_grupo2_n")

button_fortalezas_debilidades=InlineKeyboardButton(text="Recibir imagen", callback_data="image_effectivity")
button_start=InlineKeyboardButton(text="Volver al menu principal", callback_data="start")

def ataque_ave(update, context):

    query=update.callback_query
    query.answer()

    query.edit_message_text(text="¡Muy bien! Un poderoso ataque ave\n\n"\
        "Ahora solo hace falta saber si el Axie atacante es tambien de tipo ave:\n\n"\
        "(Si lo es, recibe un bono de ataque extra)",
    reply_markup=InlineKeyboardMarkup([
        [button_grupo2_y],
        [button_grupo2_n]
    ]))

def ataque_aqua(update, context):

    query=update.callback_query
    query.answer()

    query.edit_message_text(text="¡Muy bien! Un poderoso ataque aqua\n\n"\
        "Ahora solo hace falta saber si el Axie atacante es tambien de tipo aqua:\n\n"\
        "(Si lo es, recibe un bono de ataque extra)",
    reply_markup=InlineKeyboardMarkup([
        [button_grupo2_y],
        [button_grupo2_n]
    ]))

def ataque_grupo2_y(update, context):

    query=update.callback_query
    query.answer()

    query.edit_message_text(text="¡Perfeto! Que un axie sea del mismo tipo que su ataque "\
        "garantiza un buen golpe\n\n"\
        "Si el axie que recibe el ataque es un axie tipo Bestia, Bicho o Meca, "\
        "tu ataque recibe un aumento de daño de 25%, ¡Seguro que lo acabas de un golpe!\n\n"\
        "Si el axie que recibe el ataque es un axie tipo Ave, Aqua o Alba, "\
        "tu ataque recibe un aumento de daño de 10%, ¡Nada despreciable!\n\n"\
        "Si el axie que recibe el ataque es un axie tipo Planta, Reptil u Ocaso, "\
        "tu ataque recibe un decremento de daño de 5%, algo bajo...\n\n"\
        "Si lo deseas, puedes recibir una imagen para entender mejor "\
        "como funcionan las fortalezas y debilidades de los distintos tipos de Axie\n\n",
    reply_markup=InlineKeyboardMarkup([
        [button_fortalezas_debilidades],
        [button_start]
    ]))

def ataque_grupo2_n(update, context):

    query=update.callback_query
    query.answer()

    query.edit_message_text(text="¡Continuemos!\n\n"\
        "Si el axie que recibe el ataque es un axie tipo Bestia, Bicho o Meca, "\
        "tu ataque recibe un aumento de daño de 15%, ¡Golpe durisimo!\n\n"\
        "Si el axie que recibe el ataque es un axie tipo Ave, Aqua o Alba, "\
        "tu ataque no recibe aumentos o decrementos en el daño, "\
        "aun asi... ¡no subestimes un buen golpe neutral!\n\n"\
        "Si el axie que recibe el ataque es un axie tipo Planta, Reptil u Ocaso, "\
        "tu ataque recibe un decremento de daño de 15%, yo que tu me lo pensaria 2 veces...\n\n"\
        "Sin embargo esto no lo es todo, pues si tu axie es tipo Alba la historia cambia...\n\n"\
        "A este Axie especial le corresponde un bono de 7.5% cuando se trata de ataques Ave y Aqua."\
        "Por lo que quedaria así:\n\n"\
        "Si el axie que recibe el ataque es un axie tipo Bestia, Bicho o Meca, "\
        "tu ataque recibe un aumento de daño de 22.5%\n\n"\
        "Si el axie que recibe el ataque es un axie tipo Ave, Aqua o Alba, "\
        "tu ataque recibe un aumento de daño de 7.5%\n\n"\
        "Si el axie que recibe el ataque es un axie tipo Planta, Reptil u Ocaso, "\
        "tu ataque recibe un decremento de daño de 7.5%\n\n"\
        "Si lo deseas, puedes recibir una imagen para entender mejor "\
        "como funcionan las fortalezas y debilidades de los distintos tipos de Axie\n\n",
    reply_markup=InlineKeyboardMarkup([
        [button_fortalezas_debilidades],
        [button_start]
    ]))