from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL

from dotenv import load_dotenv
import os

load_dotenv()

db_url = os.getenv("DATABASE_URL")
print("Подключение к:", db_url)

engine = create_engine(db_url)
try:
    conn = engine.connect()
    print("✅ Подключение успешно!")
    conn.close()
except Exception as e:
    print("❌ Ошибка подключения:", str(e))