import os, sys
sys.path.append('/var/www/twiremind')
os.environ['DJANGO_SETTINGS_MODULE'] = 'twiremind.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()