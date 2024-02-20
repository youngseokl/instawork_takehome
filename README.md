Steps to run the application:
```
Data migration:
python3 manage.py makemigrations
python3 manage.py migrate

Load initial Instawork admin account:
python3 manage.py loaddata initial_data.json

Run server:
python3 manage.py runserver
```
