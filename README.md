django-test-site
================

Django Test Site

git clone git@github.com:vinodpandey/django-test-site.git  
cd django-test-site  
virtualenv-2.7 --no-site-packages .  
source bin/activate  
pip install -r config/requirements.txt  
python manage.py syncdb  
python manage.py migrate  

python manage.py runserver  

deactivate
