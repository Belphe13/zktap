# zktap

## How to Set Up the Web App

1. Install Django

2. Run the server in the folder containing manage.py (../zktap):

        python3 manage.py runserver
    
3. Then open

        http://127.0.0.1:8000/

## Ways to Modify Database

1. Admin page: login as superuser to modify doors and users directly

        http://127.0.0.1:8000/admin
    
2. Using Django shell
    
        python3 manage.py shell
        >>> from catalog.models import User, Door
        >>> new_door = Door(door_name="", location="", public_key)
        >>> new_door.save()
    
3. Using python shell with test.py
    
        python manage.py shell < test.py


## Accounts
superuser
username: admin
password: adminadmin

user
username: user1
password: user1user1

## Additional Features
Create the site (../):

    django-admin startproject zktap

Create the app catalog(../zktap):

    python3 manage.py startapp catalog

Create superuser (../zktap):

    python3 manage.py createsuperuser

# Tutorails

https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django

https://docs.djangoproject.com/en/2.2/intro/


locallibrary - zktap

  catalog - catalog
