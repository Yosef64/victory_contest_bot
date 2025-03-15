import requests
from app.config.setting import BASE_API_URL

async def check_user_register(tele_id):
    res = await requests.get(f"{BASE_API_URL}/student/{tele_id}")
    return res["student"]

