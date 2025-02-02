FROM python:3.12-slim

# Рабочая директория проекта в контейнере
WORKDIR /lms_drf

RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем Poetry
RUN pip install --no-cache-dir poetry

# Копируем файлы с зависимостями
COPY pyproject.toml poetry.lock ./

# Устанавливаем зависимости с помощью Poetry
RUN poetry install --no-root

# Создаем директорию для медиафайлов
RUN mkdir -p /lms_drf/media

# Открываем порт 8000 для взаимодействия с приложением
EXPOSE 8000

# Определяем команду для запуска приложения
CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
