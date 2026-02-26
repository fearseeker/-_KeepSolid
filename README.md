1. Клонировать репозиторий
git clone https://github.com/fearseeker/-_KeepSolid.git

2. Создать виртуальное окружение
python -m venv venv

3. Активировать окружение
.venv\Scripts\activate

4. Установить зависимости
pip install -r requirements.txt

5. Применить миграции
python manage.py migrate

6. Загрузить тестовые данные
python manage.py loaddata db.json

7. Запустить сервер
python manage.py runserver
