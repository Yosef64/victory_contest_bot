import requests
from app.config.setting import BASE_API_URL

async def check_user_register(tele_id):
    res = requests.get(f"{BASE_API_URL}/api/student/{tele_id}")
    print("result of the aoi call",res)
    return res["student"]

