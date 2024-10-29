from fastapi import FastAPI, Request, BackgroundTasks
from telegram import Bot, Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

app = FastAPI()

TOKEN = '7897490261:AAFMKWSSK0wHuSHlROpQH5WW9v4VsSTlkoA'
WEBHOOK_URL = 'https://jositgwebapp.vercel.app/api/index'

# Define bot and the handler functions
bot = Bot(token=TOKEN)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [[InlineKeyboardButton("Visit Web App", web_app={"url": "https://josialex.vercel.app/"})]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Welcome! Click the button below to visit our web app.", reply_markup=reply_markup)

# Function to initialize Application and register handlers
def initialize_application():
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler('start', start))
    return application

@app.post("/webhook")
async def webhook(request: Request, background_tasks: BackgroundTasks):
    """
    Telegram Webhook
    """
    application = initialize_application()

    request_data = await request.json()
    update = Update.de_json(request_data, bot)

    await application.process_update(update)
    
    return {"message": "ok"}

@app.get("/")
def index():
    return {"message": "Hello All Developers"}
