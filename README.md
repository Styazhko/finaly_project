# Финальный проект
## Описание
Данный автотест предназначен для тестирования магазина товаров.
## Установка и запуск
1. Склонировать репозиторий с Github:
```
https://github.com/Styazhko/finaly_project
```
2. Перейти в директорию проекта
3. Создать виртуальное окружение:
```
python -m venv venv
```
4. Активировать окружение:
```
venv\Scripts\activate
```
5. Установить зависимости:
```
pip install -r requirements.txt
```
6. Запустить автотест(для тестов с маркировкой "need_review", "default='chrome'"):
```
pytest -v --tb=line --language=en -m need_review
```