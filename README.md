Разработано в рамках Группового проектного обучения в ТУСУРе по кейсу от Т-Банка
---

# 🚘 T-Parking API

> **API для управления парковочными местами и пользователями**

## Описание проекта

Parking Assistant — это веб-приложение, позволяющее управлять парковочными местами и пользователями. Система предоставляет удобный интерфейс для регистрации, входа, просмотра и редактирования информации о парковочных местах (занято/свободно), а также позволяет администраторам управлять данными.

### 🧠 Функциональность:
- Регистрация и авторизация пользователей
- Просмотр этажей и парковочных мест
- Обновление статуса парковочного места
- Управление пользователями и парковками (только для администраторов)

---

## 🛠️ Технологии

Проект реализован с использованием следующих технологий:

| Категория       | Технология                         |
|----------------|------------------------------------|
| Backend        | FastAPI, SQLAlchemy ORM            |
| База данных    | PostgreSQL                         |
| Аутентификация | JWT, OAuth2                        |
| Миграции       | Alembic                            |
| Контейнеры     | Docker, Docker Compose             |
| Логирование    | Python logging                     |
| Тестирование   | Pytest (частично)                  |

---

## 📁 Структура проекта

```
.
├── alembic/              # Миграции базы данных
├── app/
│   ├── config/           # Конфигурация базы данных
│   ├── core/             # Логика безопасности (JWT)
│   ├── crud/             # CRUD операции
│   ├── models/           # Модели SQLAlchemy
│   ├── routers/          # Роутеры FastAPI
│   ├── schemas/          # Pydantic модели (валидация)
│   └── main.py           # Точка входа FastAPI
├── docker-compose.yml    # Оркестрация сервисов
├── Dockerfile            # Настройка контейнера
├── requirements.txt      # Зависимости Python
└── README.md             # Документация
```

---

## 🗂️ Модели базы данных

### 1. `User` (`app/models/user.py`)
```python
id: int
first_name: str
last_name: str
middle_name: Optional[str]
email: str (unique)
telegram_username: Optional[str]
office_address: str
hashed_password: str
is_active: bool
is_admin: bool
is_email_verified: bool
created_at: datetime
```

### 2. `Floor` (`app/models/floor.py`)
```python
id: int
name: str (unique, например: B1, B2)
```

### 3. `ParkingSpot` (`app/models/parking_spot.py`)
```python
id: int
number: str (unique)
is_occupied: bool
occupied_by_id: Optional[int] (Foreign Key к User.id)
floor_id: int (Foreign Key к Floor.id)
updated_at: datetime
```

---

## 🌐 API Endpoints

### **Auth**
- `POST /api/auth/register` — регистрация пользователя
- `POST /api/auth/login` — получение токена

### **Floors**
- `POST /floors/` — добавить этаж
- `GET /floors/` — получить список этажей

### **Parking Spots**
- `POST /spots/` — добавить парковочное место
- `GET /spots/` — получить список парковочных мест
- `PUT /spots/{spot_id}` — обновить статус парковки

### **Admin Panel**
- `GET /admin/spots` — просмотр всех парковок (только админ)
- `PUT /admin/spots/{spot_id}` — обновление парковки (админ)
- `GET /admin/users` — просмотр всех пользователей (админ)
- `PUT /admin/users/{user_id}` — обновление пользователя (админ)

---

## 🔒 Безопасность

- Используется JWT-токен для аутентификации (`access_token`)
- Защита паролей через `bcrypt`
- Разграничение прав: обычные пользователи и администраторы
- Все эндпоинты требуют аутентификации

---

## 🔄 Миграции

Для управления миграциями используется **Alembic**:

```bash
alembic revision --autogenerate -m "Описание миграции"
alembic upgrade head
```

---

## 🐳 Запуск проекта

### Перед запуском:
Создайте `.env` файл в корне проекта:
```env
POSTGRES_USER=admin
POSTGRES_PASSWORD=password
POSTGRES_DB=parking_db
DATABASE_URL=postgresql+psycopg2://admin:password@db:5432/parking_db
SECRET_KEY=your_secret_key_here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### Запуск через Docker:
```bash
docker-compose up -d
```

Сервисы:
- **FastAPI**: `http://localhost:8000`
- **PostgreSQL**: `localhost:5432`
- **pgAdmin**: `http://localhost:5050`

---

## 📘 Документация API

После запуска доступна Swagger документация:
- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 📝 Лицензия

MIT License

--- 
