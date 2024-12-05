# Используем базовый образ Python
FROM python:3.10-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем зависимости
COPY app/requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем код приложения
COPY app/ .

# Запускаем приложение
CMD ["python", "app.py"]
