virtualenv venv --python=`which python`
pip install django
pip install django-recaptcha
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
