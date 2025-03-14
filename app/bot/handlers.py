from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CommandHandler, CallbackContext,ContextTypes

async def start(update,_:ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("Visit Web App", web_app={"url": "https://victory-contest.vercel.app/"})]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Welcome! Click the button below to visit our web app.", reply_markup=reply_markup)

handlers = [
    CommandHandler("start",start)
]