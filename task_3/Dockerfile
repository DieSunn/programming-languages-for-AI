FROM python:3.9

# Установка рабочей директории в контейнере
WORKDIR /app

# Копирование файла зависимостей в контейнер
COPY requirements.txt .

# Установка зависимостей
RUN pip install --no-cache-dir -r requirements.txt

# Копирование приложения и модели в контейнер
COPY app/ ./app/
COPY models/ ./models/

# Порт для FastAPI приложения
EXPOSE 8000

# Запуск uvicorn сервера для FastAPI приложения
CMD ["uvicorn", "app.server:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]