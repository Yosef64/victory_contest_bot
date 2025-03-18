from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update,ReplyKeyboardMarkup
from telegram.ext import CommandHandler, CallbackContext,ContextTypes,MessageHandler,filters
from app.utils.helpers import check_user_register
from app.utils.variables import welcome_back_txt,welcom_text
from app.config.setting import MINI_APP_URL
def getmarkup():
    keyboard = [
        ["Start", "Profile"],
        ["Statistics", "Last Contest"],
        ["Leaderboard"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    return reply_markup
async def start(update:Update,_:ContextTypes.DEFAULT_TYPE):
    user_id = str(update.message.from_user.id)
    try:
        user = await check_user_register(user_id)
        if user:
            reply_markup = getmarkup()
            await update.message.reply_text(welcome_back_txt,reply_markup=reply_markup)
            return
        
        keyboard = [[InlineKeyboardButton("⚡ Register Now 💥", web_app={"url": f"{MINI_APP_URL}/register?tele_id={user_id}"})]]

        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text(welcom_text, reply_markup=reply_markup)
    except Exception as e:
        
        await update.message.reply_text(e.__str__())


async def profile(update:Update,context:CallbackContext):
    user = update.effective_user
    full_name = user.full_name
    username = f"@{user.username}" if user.username else "No username"

    message = (
        f"🔥 **Hey {full_name}, your profile is calling!** 🌟\n\n"
        "🚀 **Unleash your best self!** With just one tap, you can:\n"
        "🔥 **View your full profile** 👀\n"
        "💎 **Customize your settings** ⚙️\n"
        "💥 **Edit your profile like a boss** ✨\n\n"
        "🎯 **Boost your bio** 📝\n"
        "📸 **Refresh your profile picture** 🔄\n"
        "🎨 **Level up your preferences** 💡\n\n"
        "⚡ **Your profile, your power!** Ready to take control? Tap below! ⬇️🔥"
    )

    keyboard = [
        [InlineKeyboardButton("🔥 View Profile 👀", web_app={"url":f"{MINI_APP_URL}/profile"})],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(message, reply_markup=reply_markup, parse_mode="Markdown")
    