import sys
import os
import django
from myapp.models import *

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
django.setup()