from telegram.ext import Application, CommandHandler

from app.bot.options import botHandlers


async def startup_boot():
    ptb = (
    Application.builder()
    .updater(None)
    .token("7897490261:AAFMKWSSK0wHuSHlROpQH5WW9v4VsSTlkoA") 
    .read_timeout(7)
    .get_updates_read_timeout(42)
    .build()
   )
    await ptb.initialize()
    for handler in botHandlers:
        ptb.add_handler(handler)
    return ptb