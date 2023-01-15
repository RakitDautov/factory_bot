# factory_bot

Описание проекта
    
    Проект представляет собой API приложение через которое можно отправлять сообщения на телеграм бота.
    
    Проект запускается в 3 контейнерах:
        nginx
        web
        db

    Авторизация по токену.
    Все запросы от имени пользователя должны выполняться с 
    заголовком "Authorization: Token TOKENVALUE"
    
Необходимые инструменты для запуска

    docker
    docker-compose

Запуск приложения

    Перед запуском необходимо создать файл .env с переменными:
        DB_ENGINE
        DB_NAME
        POSTGRES_USER
        POSTGRES_PASSWORD
        DB_HOST
        DB_PORT
        TELEGRAM_TOKEN
    
    Запуск контейнеров

        docker-compose up -d --build

    
    Запуск скрипта бота
        
        docker exec -it backend bash
        python3 manage.py bot
    
    Чтобы привязать бота к нужному аккаунту необходимо отправить Auth_token пользователя в чат-бот.
    После этого можно отправлять сообщения на телеграм через наше API.

Стек используемых технологий

    Python
    Django, DRF
    Docker
    PostgreSQL
    nginx
    djoser
    python-telegram-bot

Доступные эндпоинты
    
    admin/                              # Панель администратора
    
    POST auth/token/login/              # Получить токен авторизации
    POST auth/token/logout/             # Удаление токена
    
    POST users/                         # Регистрация пользователя
    GET  users/                         # Получение списка пользователей
    GET users/{id}/                     # Получение пользователя по id
    
    GET messages/                       # Получить список сообщений данного пользователя
    POST messages/                      # Создать и отправить сообщение
    