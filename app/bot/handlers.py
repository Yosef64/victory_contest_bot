from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CommandHandler, CallbackContext,ContextTypes
from app.utils.helpers import check_user_register
from app.utils.variables import welcome_back_txt,welcom_text
async def start(update:Update,_:ContextTypes.DEFAULT_TYPE):
    user_id = str(update.message.from_user.id)
    try:
        user = await check_user_register(user_id)
        if user:
            await update.message.reply_text(welcome_back_txt)
            return
        
        keyboard = [[InlineKeyboardButton("Register", web_app={"url": "https://victory-contest.vercel.app/"})]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text(welcom_text, reply_markup=reply_markup)
    except Exception as e:
        await update.message.reply_text(e.__str__())

handlers = [
    CommandHandler("start",start)
]