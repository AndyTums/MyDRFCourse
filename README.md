# Приложение для управления привычками

Это приложение позволяет пользователям создавать, отслеживать и управлять своими привычками. Оно построено на основе Django REST Framework (DRF) и включает следующие функции:

- **Авторизация пользователей**: Регистрация, вход и управление профилем.
- **Управление привычками**: Создание, редактирование, удаление и отслеживание привычек.
- **Периодические задачи**: Использование Celery и Celery Beat для напоминаний и уведомлений.
- **Docker**: Простая установка и запуск с помощью Docker.
- **Deploy**: Отправка проекта на удаленный сервер.

---

## Основные функции

- **Регистрация и авторизация**:
  - Регистрация нового пользователя.
  - Вход в систему с использованием JWT-токенов.
  - Обновление и удаление профиля.

- **Управление привычками**:
  - Создание привычек с указанием названия, описания, периодичности и времени выполнения.
  - Отслеживание прогресса выполнения привычек.
  - Получение списка привычек с фильтрацией и сортировкой.

- **Напоминания и уведомления**:
  - Использование Celery для отправки уведомлений (например, в Телеграм) о необходимости выполнения привычек.
  - Использование Celery Beat для периодических задач (например, ежедневных напоминаний).

---

## Технологии

- **Backend**:
  - Django
  - Django REST Framework (DRF)
  - Celery
  - Celery Beat
  - PostgreSQL
  - Docker
  - Nginx
  - Git Actions

- **Авторизация**:
  - JWT (JSON Web Tokens)

- **Очереди задач**:
  - Redis

- **Контейнеризация**:
  - Docker
  - Docker Compose

---

## Установка и запуск

### 1. Клонируйте репозиторий

```bash
git clone https://github.com/AndyTums/MyDRFCourse.git
````

### 2. Настройте переменные окружения
```bash
Создайте файл `.env` в корневой директории и добавьте в него следующие переменные:

SECRET_KEY=

DEBUG=

# Данные для подключения к БД
NAME=
USER=
PASSWORD=
HOST=
PORT=

# DOCKER
POSTGRES_PASSWORD=PASSWORD
POSTGRES_USER=USER
POSTGRES_PORT=PORT
POSTGRES_DB=NAME
POSTGRES_HOST=HOST
CELERY_BROKER_URL = 'redis://redis:6379/0'
CELERY_RESULT_BACKEND = 'redis://redis:6379/0'

# Почта для отправки сообщений
EMAIL_HOST_PASSWORD =

# TELEGRAM
API_TOKEN_TELEGRAM =
TG_NAME_CHANEL =
```

### 3. Запустите приложение с помощью Docker Compose

```bash
docker-compose up --build
```

После запуска приложение будет доступно по адресу: http://localhost:8000.

### API Endpoints

**Авторизация**:

  - POST http://localhost:8000/login/ - вход в ЛК
  - POST http://localhost:8000/logout/ - выход с ЛК

  - POST http://localhost:8000/token/refresh/ - обновление токена

**Привычки**:

  - GET http://localhost:8000/habit/ - список привычек
  - GET http://localhost:8000/habit/id/ - информация о привычке
  - POST http://localhost:8000/habit/ - создание привычки
  - PATCH http://localhost:8000/habit/id/ - редактирование привычки
  - DELETE http://localhost:8000/habit/id/ - удаление привычки

**Пользователь**:

  - GET http://localhost:8000/user/ - список пользователей
  - GET http://localhost:8000/user/id/ - информация о пользователе
  - POST http://localhost:8000/user/ - создание пользователя
  - PATCH http://localhost:8000/user/id/ - редактирование пользователя
  - DELETE http://localhost:8000/user/id/ - удаление пользователя


### 4. Использование Celery и Celery Beat

- Celery используется для выполнения асинхронных задач, таких как отправка уведомлений.

- Celery Beat используется для выполнения периодических задач, таких как ежедневные напоминания.

#### Пример задачи Celery:
``` bash
from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_reminder_email(email, message):
    send_mail(
        'Напоминание о привычке',
        message,
        'from@example.com',
        [email],
        fail_silently=False,
    )
```

#### Пример периодической задачи Celery Beat
В файле settings.py:
``` bash
from celery.schedules import crontab

CELERY_BEAT_SCHEDULE = {
    'check_is_active': {
        'task': 'habit.tasks.send_message_to_user',
        'schedule': timedelta(seconds=20),
    },
}
```

### 5. Структура проекта:
``` bash
habit-tracker/
├── .env
├── .github/workflows/ci.yml
├── docker-compose.yml
├── Dockerfile
├── manage.py
├── requirements.txt
├── habits/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── tasks.py
│   └── test.py
└── myproject/
    ├── settings.py
    ├── urls.py
    └── ...
```

### 6. Использование Deploy

**Настройка удаленного сервера**:
- Сервер настроен для развертывания веб-приложения.
- Установлены необходимые пакеты и зависимости для работы проекта (Python, Django, Gunicorn, Nginx).
- Приложение доступно по IP-адресу: 84.201.161.178.
- Настроены параметры безопасности: используются SSH-ключи для доступа.

**Шаги выполнения запуска workflow**:

- Файл YAML для GitHub Actions находится в репозитории в папке .github/workflows.
- Workflow запускается при каждом push в репозиторий.
- Workflow включает шаг для запуска тестов проекта.
- Тесты успешно выполняются в рамках workflow и завершаются с отчетом.
- Ошибки тестов останавливают выполнение следующих шагов workflow.
- Workflow содержит шаг деплоя, который запускается только после успешного завершения тестов.
- Проект автоматически деплоится на удаленный сервер.
- Деплой выполняется корректно, без ошибок.

#### Для быстрой загрузки проекта на сервер, используйте Git Actions -->> [.yml](./.github/workflows/ci.yml)
Незабудьте внести ваши данные в переменное окружение, а так же запросить secrets. у владельца репозитория!

### 7. Лицензия

#### Этот проект распространяется под лицензией MIT. Подробности см. в файле LICENSE.
