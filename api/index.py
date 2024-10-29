from fastapi import FastAPI, Request, BackgroundTasks
from telegram import Bot, Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

app = FastAPI()

TOKEN = '7897490261:AAFMKWSSK0wHuSHlROpQH5WW9v4VsSTlkoA'
WEBHOOK_URL = 'https://jositgwebapp.vercel.app/api/index'
bot = Bot(token=TOKEN)

# Initialize the Telegram Bot application globally
application = ApplicationBuilder().token(TOKEN).build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [[InlineKeyboardButton("Visit Web App", web_app={"url": "https://josialex.vercel.app/"})]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Welcome! Click the button below to visit our web app.", reply_markup=reply_markup)

def register_handlers():
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

register_handlers()

@app.post("/webhook")
async def webhook(request: Request, background_tasks: BackgroundTasks):
    """
    Telegram Webhook
    """
    request_data = await request.json()
    update = Update.de_json(request_data, bot)

    await application.process_update(update)
    
    return {"message": "ok"}

@app.get("/")
def index():
    return {"message": "Hello All Developers"}
