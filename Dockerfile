FROM python:3.12

WORKDIR /app

COPY . /app/

RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

EXPOSE 8000
# FROM python:3.12
#
# WORKDIR /app
#
# COPY . /app/
#
# RUN pip install --no-cache-dir -r requirements.txt
#
# ENV PYTHONDONTWRITEBYTECODE=1
# ENV PYTHONUNBUFFERED=1
#
# EXPOSE 8000
#
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

##
# Используем официальный slim-образ Python 3.12
# FROM python:3.12-slim
#
# # Устанавливаем рабочую директорию в контейнере
# WORKDIR /app
#
# # Устанавливаем системные зависимости
# RUN apt-get update \
#     && apt-get install -y gcc libpq-dev curl \
#     && apt-get clean \
#     && rm -rf /var/lib/apt/lists/*
#
# # Устанавливаем Poetry
# RUN curl -sSL https://install.python-poetry.org | python3 -
# ENV PATH="/root/.local/bin:${PATH}"
#
# # Копируем файлы проекта
# COPY pyproject.toml poetry.lock /app/
#
# # Устанавливаем зависимости Python через Poetry
# RUN poetry config virtualenvs.create false && poetry install --no-root --no-interaction --no-ansi
#
# # Копируем исходный код приложения в контейнер
# COPY . /app/
#
# # Создаем директорию для медиафайлов
# RUN mkdir -p /app/media && chmod -R 755 /app/media
#
# # Пробрасываем порт, который будет использовать Django
# EXPOSE 8000
#
# # Команда для запуска приложения