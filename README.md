Веб-приложение на Django для просмотра и скачивания файлов с публичных ссылок Яндекс.Диска.

Этот README содержит всю необходимую информацию для:
- Быстрого старта проекта
- Понимания структуры
- Использования основных функций
- Установки и настройки

Документ структурирован и содержит примеры кода там, где это необходимо.

СТРУКТУРА ПРОЕКТА:
app/
├── services.py
├── views.py
├── urls.py
└── templates/app/file_list.html


## Технологии

- Python 3.8+
- Django 4.0+
- Bootstrap 5
- Yandex Disk REST API

## Установка

1. Клонируйте репозиторий:
```bash

git clone https://github.com/your-username/yandex-disk-explorer.git

cd yandex-disk-explorer
```

3. Создайте виртуальное окружение и установите зависимости:
```
python -m venv venv
source venv/bin/activate  # для Linux/Mac
venv\Scripts\activate     # для Windows
pip install -r requirements.txt
```

4. Примените миграции:
```
python manage.py migrate
```

6. Запустите сервер:
```
python manage.py runserver
```

## Структура проекта
# services.py
Содержит класс YaDiskAPI для работы с API Яндекс.Диска:
get_file() - получение списка файлов
download_file() - получение ссылки на скачивание

# views.py
Контроллеры Django:
file_list() - отображение списка файлов
download_file() - обработка скачивания

# urls.py
urlpatterns = [
    path('', views.file_list, name='file_list'),
    path('download/', views.download_file, name='download_file'),
]


## Использование
Откройте приложение в браузере
Вставьте публичную ссылку Яндекс.Диска
Просмотрите список доступных файлов
Скачайте нужные файлы

Автор
Ostrovan Aleksei 
Telegram: 
t.me/A43721





