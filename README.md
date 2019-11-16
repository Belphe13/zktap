## zktap

# how to set up the web app:

Install Django

run the server (../zktap):

    python3 manage.py runserver
    
then open

    http://127.0.0.1:8000/

Tutorails I have been reading:

https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django

https://docs.djangoproject.com/en/2.2/intro/


# accounts
superuser
username: admin
password: adminadmin

user
username: user1
password: user1user1

# additional features
create the site (../):

    django-admin startproject zktap

create the app catalog(../zktap):

    python3 manage.py startapp catalog

create superuser (../zktap):

    python3 manage.py createsuperuser

locallibrary - zktap

  catalog - catalog
