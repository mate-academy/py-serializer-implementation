import sys
import os
import django

sys.dont_write_bytecode = True
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "car_service.settings")
django.setup()
