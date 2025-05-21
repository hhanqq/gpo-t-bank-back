from fastapi import FastAPI
from app.routers import auth, parking, admin
from app.config.database import Base, engine

# Создаем таблицы в БД (только для разработки!)
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Помощник по парковке",
    description="API для управления парковочными местами и пользователями",
    version="1.0.0"
)

# Подключаем роутеры
app.include_router(auth.router, prefix="/api/auth", tags=["Auth"])
app.include_router(parking.router, prefix="/api/parking", tags=["Parking"])
app.include_router(admin.router)

@app.get("/")
def read_root():
    return {
        "message": "Добро пожаловать в API 'Помощник по парковке'",
        "docs": "http://localhost:8000/docs",
        "redoc": "http://localhost:8000/redoc"
    }