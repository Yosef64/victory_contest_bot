from telegram.ext import CommandHandler,filters,MessageHandler
from app.bot.handlers import start,profile,statistics,leaderboard,rulesAndRegulations
from telegram import Update,CallbackQuery

async def handle_option(update:Update,context:CallbackQuery):
    
    text = str(update.message.text)
    if text == "🚀 Start":
        await start(update,context)
    elif text == "👤 Profile":
        await profile(update,context)
    elif text == "📊 Statistics":
        await statistics(update,context)
    elif text == "🥇 Leaderboard":
        await leaderboard(update,context)
    elif text == "Rules and Regulations":
        await rulesAndRegulations(update,context)
    

botHandlers = [
    CommandHandler("start",start),
    MessageHandler(filters.TEXT & ~filters.COMMAND, handle_option)
]

    
