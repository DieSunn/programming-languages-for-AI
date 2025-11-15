FROM python:3.12

WORKDIR /app

COPY requirements.txt .
COPY app/ ./app/
COPY models/ ./models/

# Обновляем pip перед установкой
RUN pip install --no-cache-dir -r requirements.txt

# Запускаем приложение с указанием хоста и порта
CMD ["python", "-c", "import gradio as gr; from app.main import iface; iface.launch(server_name='0.0.0.0', server_port=7860)"]