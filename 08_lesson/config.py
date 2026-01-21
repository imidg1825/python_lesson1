import os


BASE_URL = os.getenv("YOUGILE_BASE_URL")
API_TOKEN = os.getenv("YOUGILE_API_TOKEN")

if not BASE_URL:
    raise RuntimeError("Не задана переменная окружения YOUGILE_BASE_URL")

if not API_TOKEN:
    raise RuntimeError("Не задана переменная окружения YOUGILE_API_TOKEN")
