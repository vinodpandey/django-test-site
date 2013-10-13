django-test-site
================

Prerequisites:-
virtualenv-2.7 should be installed/available
https://github.com/vinodpandey/blog/blob/master/virtualenv-python2.7.3.sh

This setup includes:-

1. Dependencies
   Django==1.5
   South==0.7.6
   django-debug-toolbar==0.9.4
2. Different settings (dev.py and prod.py) for different environments
3. Seperation of configurations for apps (see djang_debug_toolbar setting block in dev.py)
3. sqlite3 as database


virtualenv-2.7 --no-site-packages virtualenv
cd virtualenv
git clone git@github.com:vinodpandey/django-test-site.git
source bin/activate
cd django-test-site
pip install -r requirements.txt
python manage.py syncdb
python manage.py migrate

python manage.py runserver

deactivate