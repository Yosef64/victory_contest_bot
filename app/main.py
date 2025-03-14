from contextlib import asynccontextmanager
from http import HTTPStatus
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext._contexttypes import ContextTypes
from fastapi import FastAPI, Request, Response
from app.api.endpoints import router


app = FastAPI()

app.include_router(router=router)

