from Types import tipos, secretos
from Effectivity import ataque, image_effectivity
from RPDEffectivity import ataque_reptil, ataque_planta, ataque_grupo1_y, ataque_grupo1_n
from AAAEffectivity import ataque_ave, ataque_aqua, ataque_grupo2_y, ataque_grupo2_n
from BBMEffectivity import ataque_bestia, ataque_bicho, ataque_grupo3_y, ataque_grupo3_n
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
            CallbackQueryHandler(pattern="tipos", callback=tipos),
            CallbackQueryHandler(pattern="secretos", callback=secretos),
            CallbackQueryHandler(pattern="efectividad", callback=ataque),
            CallbackQueryHandler(pattern="ataque_reptil", callback=ataque_reptil),
            CallbackQueryHandler(pattern="ataque_planta", callback=ataque_planta),
            CallbackQueryHandler(pattern="ataque_ave", callback=ataque_ave),
            CallbackQueryHandler(pattern="ataque_aqua", callback=ataque_aqua),
            CallbackQueryHandler(pattern="ataque_bestia", callback=ataque_bestia),
            CallbackQueryHandler(pattern="ataque_bicho", callback=ataque_bicho),
            CallbackQueryHandler(pattern="ataque_grupo1_y", callback=ataque_grupo1_y),
            CallbackQueryHandler(pattern="ataque_grupo1_n", callback=ataque_grupo1_n),
            CallbackQueryHandler(pattern="ataque_grupo2_y", callback=ataque_grupo2_y),
            CallbackQueryHandler(pattern="ataque_grupo2_n", callback=ataque_grupo2_n),
            CallbackQueryHandler(pattern="ataque_grupo3_y", callback=ataque_grupo3_y),
            CallbackQueryHandler(pattern="ataque_grupo3_n", callback=ataque_grupo3_n),
            CallbackQueryHandler(pattern="image_effectivity", callback=image_effectivity)
        ],
        states={
            
        },
        fallbacks=[]

    ))

    updater.start_polling()
    updater.idle()