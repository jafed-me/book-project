from .base import *

SECRET_KEY='django-insecure-nquxy%lv!!gty6oos81fk1eply+rjzdjo2uxr3e!_tnip4)_fl'

DEBUG = True

ALLOWED_HOSTS = [
    '0.0.0.0',
    '127.0.0.1'
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
