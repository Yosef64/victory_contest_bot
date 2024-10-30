from contextlib import asynccontextmanager
from http import HTTPStatus
from telegram import Update
from telegram.ext import Application, CommandHandler
from telegram.ext._contexttypes import ContextTypes
from fastapi import FastAPI, Request, Response



app = FastAPI()
async def start(update, _: ContextTypes.DEFAULT_TYPE):
    """Send a message when the command /start is issued."""
    await update.message.reply_text("starting...") 
@app.post("/")
async def process_update(request: Request):
    ptb = (
    Application.builder()
    .updater(None)
    .token("7897490261:AAFMKWSSK0wHuSHlROpQH5WW9v4VsSTlkoA") 
    .read_timeout(7)
    .get_updates_read_timeout(42)
    .build()
   )
    ptb.add_handler(CommandHandler("start", start))
    req = await request.json()
    
    update = Update.de_json(req, ptb.bot)
    await ptb.process_update(update)
    return Response(status_code=HTTPStatus.OK)
@app.get("/")
def index(request:Request):
    return {"message": "Hello World"}


