# Спринт №3 Социальная сеть блогеров

## Описание
Создано и зарегистрировано приложение Posts. Подключена база данных. Десять последних записей выводятся на главную страницу. В админ-зоне доступно управление объектами модели Post: можно публиковать новые записи или редактировать/удалять существующие.

Пользователь может перейти на страницу любого сообщества, где отображаются десять последних публикаций из этой группы.

## Настройка и запуск
Склонировать проект:
```
git clone https://github.com/maksim-moryakov/hw02_community.git
```

Устанавить виртуальное окружение:
```
python -m venv venv
```
Активировать виртуальное окружение:
```
source venv/Scripts/activate
```
> Для деактивации виртуального окружения:
>
>``` 
>deactivate
>```

Обнавить пакетный менеджер pip и устанавить зависимости:
```
python -m pip install --upgrade pip
pip install -r requirements.txt
```
Применяем миграции:
```
python yatube/manage.py makemigrations
python yatube/manage.py migrate
```

Файлы с изобразениями и стилями расспологаются по ссылке: 
```
https://code.s3.yandex.net/Python-dev/web_hw02_community_with_text_01_06_22.zip
```
Их необходимо разместить в дериктории static


## Используемые технологии
- Python 3.9
- Django 2.2.19
- pytz 2022.7.1
- sqlparse 0.4.3
## Автор
- Моряков Максим
- Email: maksim.moryakov@gmail.com 