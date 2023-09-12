# Проект Yatube. Повышение функциональности.

![Python](https://img.shields.io/badge/Python-313131?style=flat&logo=Python&logoColor=white&labelColor=306998)
![Django](https://img.shields.io/badge/Django-313131?style=flat&logo=django&labelColor=092e20)
![Pytest](https://img.shields.io/badge/pytest-313131?style=flat&logo=pytest&logoColor=ffffff&labelColor=%23009fe3)
![Unittest](https://img.shields.io/badge/Unittest-8b3daa?style=flat&logo=cup&logoColor=ffffff)
![Visual Studio](https://img.shields.io/badge/VS%20Code-313131?style=flat&logo=visualstudiocode&logoColor=ffffff&labelColor=0098FF)

## Проект Yatube — это платформа для публикаций (блог). 
### На данном этапе реализовано отображение иллюстраций к постам, система комментариев, кеширование главной страницы, кастомные страницы ошибок, подписки на авторов и лента постов из подписок. Покрытие тестами нового функционала. 

### Как запустить проект:

1. Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/deltabobkov/hw05_final.git

cd hw05_final
```

2. Cоздать и активировать виртуальное окружение:

```
python -m venv env

source env/Scripts/activate
```

3. Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip

pip install -r requirements.txt
```

4. Выполнить миграции:

```
python manage.py migrate
```

5. Создать супер пользователя:

```
python manage.py createsuperuser
```

6. Запустить проект:

```
python manage.py runserver
```

**Проект будет доступен по адресу:**  
http://localhost/

