## Курсовая работа 7
- Добавлена модель привычек.
- Реализованы эндпоинты.
- Реализованы валидаторы.
- Реализована пагинация для вывода списка привычек текущего пользователя.
- Реализованы права доступа.
- Настроены интеграцию с Телеграм и отложенная задача через Celery.
- Настоен CORS.
- Настрен вывод документации.
- Добавлены тесты, покрытие составляет 83%.
- Работа проверена с помощью Postman.
- Результат проверки Flake8 равен 100%

### Основные приложения
- Ubuntu 22.04.5 LTS
- Python 3.10.12
- Poetry 1.8.2
- git 2.34.1
- VSCode 1.95.2 (Windows 11)
- PostgreSQL 16.3

### Применённые пакеты
- django
- djangorestframework
- djangorestframework-simplejwt
- django-filter
- django-celery-beat
- django-cors-headers
- psycopg2-binary
- python-dotenv
- requests
- celery
- drf-yasg
- coverage
- redis
- black

### Пользователи, создаваемые командой createusers:
- igor@sky.pro
- ivan@sky.pro
- irina@sky.pro

Пароль: 123

### Инструкция для развертывания проекта

#### Клонирование проекта:
```
git clone https://github.com/AidarPutilov/kurs7.git
```

#### Переход в каталог
```
cd kurs7
```

#### Базовые настройки
```
Ввести настройки django, сервера PostgreSQL, сервера Redis, ID бота Телеграм. Переименовать файл в .env.
```

#### Создание базы данных
```
sudo -i -u postgres
createdb kurs7
```

#### Активация Poetry, установка пакетов
```
poetry shell
poetry install
```

#### Применение миграций
```
python3 manage.py migrate
```

#### Добавление пользователей
```
python3 manage.py createusers
```

#### Запуск проекта
```
python3 manage.py runserver
```

#### Запуск тестов
```
python3 manage.py test
```

#### Запуск обработчика очереди для получения задач и их выполнения
```
celery -A config worker --beat --scheduler django --loglevel=info
```

#### Доступ к документации
```
http://127.0.0.1:8000/swagger/ - Swagger
http://127.0.0.1:8000/redoc/ - Redoc
```

### Запросы User
```
http://127.0.0.1:8000/users/register/ - Регистрация пользователя
http://127.0.0.1:8000/users/login/ - Авторизация, получение токена
http://127.0.0.1:8000/users/list/ - Список пользователей
http://127.0.0.1:8000/users/view/<pk>/ - Просмотр пользователя
http://127.0.0.1:8000/users/update/<pk>/ - Редактирование пользователя
http://127.0.0.1:8000/users/delete/<pk>/ - Удаление пользователя
```

### Запросы Habit
```
http://127.0.0.1:8000/main/ - LIST, CREATE
http://127.0.0.1:8000/main/<pk>/ - RETRIEVE, PUT, PATCH, DELETE
http://127.0.0.1:8000/main/public/ - Список публичных записей
```
