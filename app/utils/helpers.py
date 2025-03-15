import httpx
import requests
from app.config.setting import BASE_API_URL

async def check_user_register(tele_id):
    async with httpx.AsyncClient() as client:
        res = await client.get(f"{BASE_API_URL}/api/student/{tele_id}")
        res.raise_for_status() 
        data = res.json()
        return data.get("student")

