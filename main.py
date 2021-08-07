from Axies import juego, axie
from Stats import estadisticas, vitalidad, velocidad, habilidad, moral
from Types import tipos, secretos, bestia, aqua, planta, ave, bicho, reptil, meca, alba, ocaso
from Effectivity import ataque, image_effectivity
from RPDEffectivity import ataque_reptil, ataque_planta, ataque_grupo1_y, ataque_grupo1_n, ataque_grupo1_e
from AAAEffectivity import ataque_ave, ataque_aqua, ataque_grupo2_y, ataque_grupo2_n, ataque_grupo2_e
from BBMEffectivity import ataque_bestia, ataque_bicho, ataque_grupo3_y, ataque_grupo3_n, ataque_grupo3_e
import os
from Start import start, start_again
from telegram.ext import Updater, CommandHandler, ConversationHandler, CallbackQueryHandler

if __name__ == "__main__":

    updater = Updater(token=os.environ.get("TOKEN_AXIEFUTUREBOT"),use_context=True)
    
    dp=updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(ConversationHandler(

        entry_points=[
            CallbackQueryHandler(pattern="start", callback=start_again),
            CallbackQueryHandler(pattern="juego", callback=juego),
            CallbackQueryHandler(pattern="axie", callback=axie),
            CallbackQueryHandler(pattern="estadisticas", callback=estadisticas),
            CallbackQueryHandler(pattern="vitalidad", callback=vitalidad),
            CallbackQueryHandler(pattern="velocidad", callback=velocidad),
            CallbackQueryHandler(pattern="habilidad", callback=habilidad),
            CallbackQueryHandler(pattern="moral", callback=moral),
            CallbackQueryHandler(pattern="tipos", callback=tipos),
            CallbackQueryHandler(pattern="bestia", callback=bestia),
            CallbackQueryHandler(pattern="aqua", callback=aqua),
            CallbackQueryHandler(pattern="planta", callback=planta),
            CallbackQueryHandler(pattern="ave", callback=ave),
            CallbackQueryHandler(pattern="bicho", callback=bicho),
            CallbackQueryHandler(pattern="reptil", callback=reptil),
            CallbackQueryHandler(pattern="secretos", callback=secretos),
            CallbackQueryHandler(pattern="meca", callback=meca),
            CallbackQueryHandler(pattern="alba", callback=alba),
            CallbackQueryHandler(pattern="ocaso", callback=ocaso),
            CallbackQueryHandler(pattern="efectividad", callback=ataque),
            CallbackQueryHandler(pattern="ataque_reptil", callback=ataque_reptil),
            CallbackQueryHandler(pattern="ataque_planta", callback=ataque_planta),
            CallbackQueryHandler(pattern="ataque_ave", callback=ataque_ave),
            CallbackQueryHandler(pattern="ataque_aqua", callback=ataque_aqua),
            CallbackQueryHandler(pattern="ataque_bestia", callback=ataque_bestia),
            CallbackQueryHandler(pattern="ataque_bicho", callback=ataque_bicho),
            CallbackQueryHandler(pattern="ataque_grupo1_y", callback=ataque_grupo1_y),
            CallbackQueryHandler(pattern="ataque_grupo1_n", callback=ataque_grupo1_n),
            CallbackQueryHandler(pattern="ataque_grupo1_e", callback=ataque_grupo1_e),
            CallbackQueryHandler(pattern="ataque_grupo2_y", callback=ataque_grupo2_y),
            CallbackQueryHandler(pattern="ataque_grupo2_n", callback=ataque_grupo2_n),
            CallbackQueryHandler(pattern="ataque_grupo2_e", callback=ataque_grupo2_e),
            CallbackQueryHandler(pattern="ataque_grupo3_y", callback=ataque_grupo3_y),
            CallbackQueryHandler(pattern="ataque_grupo3_n", callback=ataque_grupo3_n),
            CallbackQueryHandler(pattern="ataque_grupo2_e", callback=ataque_grupo3_e),
            CallbackQueryHandler(pattern="image_effectivity", callback=image_effectivity)
        ],
        states={},
        fallbacks=[]
    ))

    updater.start_polling()
    updater.idle()