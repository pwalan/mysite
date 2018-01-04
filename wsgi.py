import os
import sys

from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))

os.environ["DJANGO_SETTINGS_MODULE"] = "mysite.settings"

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()