"""
WSGI config for discuss project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os, sys

# add the hellodjango project path into the sys.path
sys.path.append('/home/vagrant/HN_Clone/venv')

# add the virtualenv site-packages path to the sys.path
sys.path.append('/home/vagrant/HN_Clone/venv')

# poiting to the project settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "discuss.settings")



from django.core.wsgi import get_wsgi_application








application = get_wsgi_application()
