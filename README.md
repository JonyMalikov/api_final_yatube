# **API для социальной сети**

[![Python](https://img.shields.io/badge/Python-3.7-blue?style=flat-square&logo=Python&logoColor=3776AB&labelColor=d0d0d0)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-2.2.16-blue?style=flat-square&logo=Django&logoColor=3776AB&labelColor=d0d0d0)](https://docs.djangoproject.com/en/2.2/)
[![Django REST framework](https://img.shields.io/badge/Django_REST_framework-3.12.4-blue?style=flat-square&logo=Django&logoColor=3776AB&labelColor=d0d0d0)](https://www.django-rest-framework.org/)
[![djoser](https://img.shields.io/badge/djoser-2.1.0-blue?style=flat-square&logoColor=3776AB&labelColor=d0d0d0)](https://djoser.readthedocs.io/en/latest/)
[![Pillow](https://img.shields.io/badge/Pillow-8.3.1-blue?style=flat-square&logoColor=3776AB&labelColor=d0d0d0)](https://pillow.readthedocs.io/en/stable/)
---

**API для социальной сети** - Yandex Practicum образовательный проект по обучению работе с API.

### Описание:

API для проекта социальной сети YaTube

В рамках этого API можно:
Получать все посты с возможностью фильтрации по группе
Создавать, редактировать или удалять собственные посты
Комментировать другие посты или смотреть комментарии определенного поста
Создавать группы для постов
Подписываться на понравившегося автора
Посмотреть все подписки, также возможен поиск подписок конкретного пользователя
Выполнить аутентификацию по JWT-токену

### Примеры запросов и ответов:

![get](https://img.shields.io/badge/%20-GET%20-green) `http://127.0.0.1:8000/api/v1/posts/{id}/`

```json
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2023-04-11T14:15:22Z",
  "image": "string",
  "group": 0
}
```

![](https://img.shields.io/badge/%20-POST%20-blue) `/api/v1/posts/ `

```json
{
  "text": "string",
  "image": "jpg",
  "group": 1
}
```

```json
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2023-04-11T14:15:22Z",
  "image": "jpg",
  "group": 1
}
```

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com/JonyMalikov/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```
## Документация

Когда вы запустите проект, по адресу http://127.0.0.1:8000/redoc/ будет доступна документация для API Yatube