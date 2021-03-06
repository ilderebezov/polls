# Poll API
API для системы опросов пользователей

##### Функционал для администратора системы:
- авторизация в системе (без регистрации)
- добавление/изменение/удаление опросов. Атрибуты опроса: название, дата старта,
  дата окончания, описание. После создания поле "дата старта" у опроса
  менять нельзя
- добавление/изменение/удаление вопросов в опросе. Атрибуты вопросов: текст
  вопроса, тип вопроса (ответ текстом, ответ с выбором одного варианта, ответ с
  выбором нескольких вариантов)

##### Функционал для пользователей системы:
- получение списка активных опросов
- прохождение опроса: опросы можно проходить анонимно, в качестве идентификатора
  пользователя в API передаётся числовой ID, по которому сохраняются ответы
  пользователя на вопросы; один пользователь может участвовать в любом
  количестве опросов
- получение пройденных пользователем опросов с детализацией по ответам
  (что выбрано) по ID уникальному пользователя

#### Установка:
1. Склонируйте репозиторий
2. Создайте и войдите в вирутальное окружение
3. Установите зависимости:
    - `pip install -r requirements.txt`
5. Проведите миграции
    - `python manage.py makemigrations`
    - `python manage.py migrate`
6. Создайте суперпользователя
    - `python manage.py createsuperuser`
7. Запустите тестовый сервер
    - `python manage.py runserver`