from contextlib import asynccontextmanager
from http import HTTPStatus
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext._contexttypes import ContextTypes
from fastapi import FastAPI, Request, Response
from app.api.endpoints import router


app = FastAPI()

app.include_router(router=router)

#https://api.telegram.org/bot7897490261:AAFMKWSSK0wHuSHlROpQH5WW9v4VsSTlkoA/setWebhook?url=https://victory-fast.vercel.app/webhook

