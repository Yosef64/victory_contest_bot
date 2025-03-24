from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update,ReplyKeyboardMarkup
from telegram.ext import CommandHandler, CallbackContext,ContextTypes,MessageHandler,filters
from app.utils.helpers import check_user_register
from app.utils.variables import welcome_back_txt,welcom_text,error_message,rules
from app.config.setting import MINI_APP_URL
def getmarkup():
    keyboard = [
    ["🚀 Start", "👤 Profile"],
    ["📊 Statistics", "Rules and Regulations"],
    ["🥇 Leaderboard"]
]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    return reply_markup

async def start(update:Update,_:ContextTypes.DEFAULT_TYPE):
    user_id = str(update.message.from_user.id)
    try:
        user = await check_user_register(user_id)
        if user:
            reply_markup = getmarkup()
            await update.message.reply_text(welcome_back_txt,reply_markup=reply_markup,parse_mode="MarkdownV2")
            return
        
        keyboard = [[InlineKeyboardButton("⚡ Register Now 💥", web_app={"url": f"{MINI_APP_URL}/register?tele_id={user_id}"})]]

        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text(welcom_text, reply_markup=reply_markup,parse_mode="MarkdownV2")
    except Exception as e:
        await update.message.reply_text(error_message,parse_mode="MarkdownV2")
        print(e)


async def profile(update:Update,context:CallbackContext):
    user = update.effective_user
    full_name = user.full_name
    username = f"@{user.username}" if user.username else ""
    userId = str(user.id)
    message = (
        f"""🌟 *Hey {full_name}, your profile is calling\\!* 🌟\n\n
        *Unleash your best self\\!* With just one tap, you can\\:\n
        🔥 *View your full profile* 👀\n
        ⚙️ *Customize your settings* \n
        ✨ *Edit your profile like a boss* \n\n
        🎯 *Boost your bio* \n
        📸 *Refresh your profile picture* \n
        🎨 *Level up your preferences* \n\n
        ⚡ *Your profile, your power\\! Ready to take control? Tap below\\!* ⬇️"""
    )

    keyboard = [
        [InlineKeyboardButton("🔥 View Profile 👀", web_app={"url":f"{MINI_APP_URL}/profile/{userId}"})],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(message, reply_markup=reply_markup, parse_mode="MarkdownV2")

    return
async def statistics(update:Update,context:CallbackContext):
    user = update.effective_user
    full_name ,user_id= user.full_name,user.id

    message = (
        f"""🔥 *Your performance stats are in\\!* Here’s what you can check\\:\n"
        🏅 *Total Contests Participated\\:* \n
        ⚡ *The Time You Spent\\:* \n
        📈 *Average Performance Score\\:* \n
        ❌ *Total Missed Questions* \\(Based on Grade, Chapter, Subject\\)\\: \n\n
        💪 *Keep pushing the limits\\!* Every contest is a chance to grow\\! 💪\n
        💡 *Want to improve?* Check past results and track progress\\! \n\n
        *Tap below to view full statistics\\!*"""
    )
    keyboard = [
        [InlineKeyboardButton("📊 View Statistics 👀", web_app={"url":f"{MINI_APP_URL}/statistics/{user_id}"})],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(message,reply_markup=reply_markup,parse_mode="MarkdownV2")
    return
async def leaderboard(update:Update,context:CallbackContext):
    user = update.effective_user
    full_name ,user_id = user.full_name,user.id
    message = (
        f"""🥇 *Hey {full_name}, the competition is heating up\\!* 🔥\n\n
        🏆 *Welcome to the Leaderboard\\!* Here’s how the rankings stand\\:\n\n
        📅 *Today's Contest Ranking\\:* \n
        📆 *Weekly Top Performers\\:* \n
        📊 *Monthly Champions\\:* 🏅\n\n
        💡 *Stay consistent and climb the ranks\\!* Every contest is a chance to rise higher\\! \n
        ⚡ *Think you can be the best?* Keep pushing your limits and dominate the leaderboard\\! \n\n
        *Tap below to check the full rankings\\!*"""
    )
    try:
        keyboard = [
        [InlineKeyboardButton("🔥 View Leaderboard 👀", web_app={"url":f"{MINI_APP_URL}/leaderboard?tele_id={user_id}"})],
    ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text(message,reply_markup=reply_markup,parse_mode="MarkdownV2")
        return
    except Exception as e:
        print(e)
        await update.message.reply_text(error_message,parse_mode="MarkdownV2")
        return


async def rulesAndRegulations(update:Update,context:CallbackContext):
    try:

        await update.message.reply_text(rules,parse_mode="MarkdownV2")
        return
    except Exception as e:
        await update.message.reply_text(error_message,parse_mode="MarkdownV2")
        print(e)
    return
        
        