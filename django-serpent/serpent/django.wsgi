import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'django-serpent.settings'

sys.path.append('C:/sites/') #change this for your implementation if need be

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()