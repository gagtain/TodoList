### ToDo List

Для запуска проекта необходимо заполнить .env для django_api, aiogram_bot, fast_api


```aiogram_bot/bot/.env```

```env
token=...
admins=...,...
api_token=xxx
api_url=http://webapi:8000
fast_api_url=http://webapi_fast:8000
```

1. token - Токен от тг-бота, можно получить в @BotFather
2. admins - список id в tg администраторов через ',' им будут приходить ошибки в случае их возникновения
3. api_token - токен установленный в django_api для доступа сторонним сервисам
4. api_url - адрес django_api "http://HOST:PORT"
5. fast_api_url - адрес fast_api "http://HOST:PORT"

```django_api/api/api/.env```

```env
SECRET_KEY=...
CELERY_BROKER_URL=redis://redis:6379/5
REDIS_HOST=redis
REDIS_PORT=6379
REDIS_DB=4
DEBUG=1
POSTGRESQL_HOST=database
POSTGRESQL_PORT=5432
POSTGRESQL_DATABASE=todolist
POSTGRESQL_USER=todolist_user
POSTGRESQL_PASSWORD=todolist_pass
ALLOWED_HOSTS=*
COUNT_SEED=15
BOT_TOKEN=xxx
BOT_TG_TOKEN=7551579......CE......DVsXXXd2CxxBMqry8KfaM
```

1. COUNT_SEED - максимольное кол-во запросов в минуту
2. BOT_TOKEN - токен для доступа сторонним сервисам
3. BOT_TG_TOKEN - токен бота в tg
4. SECRET_KEY - секретный ключ django

```fast_api/api/.env```

```env
DB_ECHO=1
PROJECT_NAME=comments_api
VERSION=0.1
DEBUG=1
CORS_ALLOWED_ORIGINS=*
POSTGRES_HOST=database
POSTGRES_PORT=5432
POSTGRES_DB=todolist
POSTGRES_USER=todolist_user
POSTGRES_PASSWORD=todolist_pass
REDIS_HOST=redis
REDIS_PORT=6379
REDIS_DB=4
TASK_API_URL=http://webapi:8000
api_token=xxx
```

1. api_token - токен установленный в django_api для доступа сторонним сервисам
2. TASK_API_URL - ссылка на django_api


Запуск проекта

```cmd
docker compose up -d --build
```

по умолчанию

http://localhost:8000/ - django_api
http://localhost:8080/ - fast_api

Админка django доступна по адресу ```/admin```

Чтобы создать суперпользователя для входа в /admin, необходимо:

1. Написать команду 
```docker compose exec -it webapi python manage.py createsuperuser```
2. Указать нужные креды


Структура Проекта:

Проект состоит из
1. ```django_api``` - основное ToDo api
2. ```fast_api``` - api комментариев
3. ```aiogram``` - tg бот использующий оба api

В виде БД выступает ```PostgreSQL```

Для кеша и асинхронной очереди используется ```Redis```

Для создания асинхронной очереди используется библиотека ```Celery```, на данный момент используется 1 переодическая задача

Задача реализованна переодически, поскольку при помощи api можно менять дедлайн и выполнение без периодичности повлекло бы за собой ряд издержек

Из трудностей, только обязательное  использование ```aiogram-dialogs```, поскольку довольно давно им пользовался.

в FastAPI можно было добавить ```alembic``` для миграций, но из-за сроков мною указанных и минималистичности проекта, решил не добавлять

В остальном трудностей не заметил, задачи типовые
