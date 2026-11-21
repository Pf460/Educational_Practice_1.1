# Учебная практика 05

---
### Разработка кода информационных систем

--- 

### Инструкция по запуску:

````bash
git clone https://github.com/Pf460/Educational_Practice_1.1.git

cd locallibrary
python -m venv .venv
````

Активируем виртуальное окружение в соответствии с ОС

````bash
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser

python manage.py runserver
````

### Рабочие адреса

- http://127.0.0.1:8000/ - базовый url
- http://127.0.0.1:8000/admin - админка