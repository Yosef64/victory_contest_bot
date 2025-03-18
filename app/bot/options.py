from telegram.ext import CommandHandler,filters,MessageHandler
from app.bot.handlers import start,profile
from telegram import Update,CallbackQuery

def handle_option(update:Update,context:CallbackQuery):
    user_id = str(update.message.from_user.id)
    text = str(update.message.text)
    if text == "Start":
        start(update,context)
    elif text == "Profile":
        profile(update,context)


botHandlers = [
    CommandHandler("start",start),
    MessageHandler(filters.TEXT & ~filters.COMMAND, handle_option)
]

    
