from http import HTTPStatus
from fastapi import APIRouter, Request, Response
from telegram import Update
from app.bot.telegram import startup_boot

router = APIRouter()

@router.post("/webhook")
async def webhook(request: Request):
    ptb = startup_boot()
    req = await request.json()
    
    update = Update.de_json(req, ptb.bot)
    await ptb.process_update(update)
    return Response(status_code=HTTPStatus.OK)
    
@router.get("/")
async def root(request:Request):
    return {"message":"It's working fine"}