# Куда пойти — Москва глазами Артёма


Сайт о самых интересных местах столицы.


## Переменные окружения

Определите переменные окружения в файле `.env` в формате: `ПЕРЕМЕННАЯ=значение`:
- `DEBUG` — дебаг-режим. Поставьте `True` для включения, `False` — для 
выключения отладочного режима. По умолчанию дебаг-режим отключен.
- `SECRET_KEY` — секретный ключ проекта, например: `fwei3$@K!fjslfji;erfkdsewyiwero`
- `ALLOWED_HOSTS` — список разрешенных хостов.
- `STATIC_URL` — отображаемый каталог со статичными файлами, по умолчанию `'/static/'`. 
- `MEDIA_ROOT` — каталог для хранения медиа-файлов, по умолчанию `'media'`.
- `MEDIA_URL` — отображаемый каталог с медиа-файлами, по умолчанию `'/media/'`
- `SECURE_HSTS_SECONDS` — по умолчанию противоположно значению `DEBUG`
- `SECURE_SSL_REDIRECT` — по умолчанию противоположно значению `DEBUG`
- `SESSION_COOKIE_SECURE` — по умолчанию противоположно значению `DEBUG`
- `CSRF_COOKIE_SECURE` — по умолчанию противоположно значению `DEBUG`


## Установка и запуск на локальном сервере

- Скачайте код из репозитория
- Установите зависимости командой:
```shell
pip install -r requirements.txt
```
- Создайте файл `.env` в корневой папке и пропишите необходимые переменные 
окружения в формате: `ПЕРЕМЕННАЯ=значение`
- Выполните миграцию БД:
```commandline
python manage.py migrate
```
- Запустите скрипт командой:
```commandline
python manage.py runserver
```


### Наполнение базы данных

Для заполнения базы данных тестовой информацией используется команда `load_place`.

Аргументом скрипту передаётся путь к локальному .json файлу (`-p`/`--local_path`) 
или url к .json файлу (`-u`/`--url`) с информацией вида
```json
{
    "title": "Экскурсионный проект «Крыши24.рф»",
    "imgs": [
        "https://kudago.com/media/images/place/d0/f6/d0f665a80d1d8d110826ba797569df02.jpg",
        "https://kudago.com/media/images/place/66/23/6623e6c8e93727c9b0bb198972d9e9fa.jpg",
        "https://kudago.com/media/images/place/64/82/64827b20010de8430bfc4fb14e786c19.jpg"
    ],
    "description_short": "Хотите увидеть Москву с высоты птичьего полёта?",
    "description_long": "<p>Проект «Крыши24.рф» проводит экскурсии ...</p>",
    "coordinates": {
        "lat": 55.753676,
        "lng": 37.64
    }
}
```
Например:
```commandline
python manage.py load_place -u "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/%D0%90%D0%BD%D1%82%D0%B8%D0%BA%D0%B0%D1%84%D0%B5%20Bizone.json"

python manage.py load_place -p places/place_details.json
```


### Панель администратора

Панель администратора сайта доступна по адресу `sitename/admin/`. Для
создания учетной записи администратора используйте команду:
```commandline
python manage.py createsuperuser
```


## Демо-версия сайта

Демо-версия сайта доступна по ссылке [hyggebox.pythonanywhere.com](http://hyggebox.pythonanywhere.com/)
Данные взяты из репозитория [devmanorg/where-to-go-places](https://github.com/devmanorg/where-to-go-places)



## Цели проекта

Код написан в учебных целях.

Тестовые данные взяты с сайта [KudaGo](https://kudago.com/).