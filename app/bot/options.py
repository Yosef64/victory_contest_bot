from telegram.ext import CommandHandler,filters,MessageHandler
from app.bot.handlers import start,profile
from telegram import Update,CallbackQuery

async def handle_option(update:Update,context:CallbackQuery):
    
    text = str(update.message.text)
    if text == "Start":
        await start(update,context)
    elif text == "Profile":
        await profile(update,context)


botHandlers = [
    CommandHandler("start",start),
    MessageHandler(filters.TEXT & ~filters.COMMAND, handle_option)
]

    
