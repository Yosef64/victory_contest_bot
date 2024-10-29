import json
import os
from typing import Optional
from fastapi import FastAPI, Request, BackgroundTasks
from pydantic import BaseModel
from telegram import Bot, Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.environ.get("TOKEN")

app = FastAPI()

TOKEN = '7897490261:AAFMKWSSK0wHuSHlROpQH5WW9v4VsSTlkoA'
WEBHOOK_URL = 'https://jositgwebapp.vercel.app/api/index'
bot = Bot(token=TOKEN)

class TelegramWebhook(BaseModel):
    """
    Telegram Webhook Model using Pydantic for request body validation
    """
    update_id: int
    message: Optional[dict]
    edited_message: Optional[dict]
    channel_post: Optional[dict]
    edited_channel_post: Optional[dict]
    inline_query: Optional[dict]
    chosen_inline_result: Optional[dict]
    callback_query: Optional[dict]
    shipping_query: Optional[dict]
    pre_checkout_query: Optional[dict]
    poll: Optional[dict]
    poll_answer: Optional[dict]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [[InlineKeyboardButton("Visit Web App", web_app={"url": "https://josialex.vercel.app/"})]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Welcome! Click the button below to visit our web app.", reply_markup=reply_markup)
def register_handlers(dispatcher):
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

@app.post("/webhook")
async def webhook(webhook_data: TelegramWebhook, background_tasks: BackgroundTasks):
    """
    Telegram Webhook
    """
    bot = Bot(token=TOKEN)
    application = ApplicationBuilder().token(TOKEN).build()
    register_handlers(application)

    update = Update.de_json(webhook_data.dict(), bot)

    await application.process_update(update)
    
    return {"message": "ok"}


@app.get("/")
def index():
    return {"message": "Hello All Developers"}
