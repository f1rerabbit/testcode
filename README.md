# AI Video Factory Backend

Backend-сервис на **Python 3.12 + FastAPI** с поддержкой **SQLAlchemy 2.0**, **Pydantic v2**, **Alembic**, **PostgreSQL** и **Redis**.

## Структура

```text
app/
  main.py
  core/
    config.py
    database.py
  api/
    router.py
    routes/
      health.py
```

## Быстрый старт (Docker)

1. Создайте `.env` на основе шаблона:

```bash
cp .env.example .env
```

2. Запустите сервисы:

```bash
docker compose up --build
```

3. Проверьте health endpoint:

```bash
curl http://localhost:8000/health
```

Ожидаемый ответ:

```json
{"status":"ok"}
```

## Локальный запуск backend

```bash
cd backend
python3.12 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## Тесты

```bash
cd backend
pytest
```

## Alembic

```bash
cd backend
alembic revision -m "init"
alembic upgrade head
```
