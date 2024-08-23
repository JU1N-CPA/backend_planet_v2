import os

from .base import *  # NOQA

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'almadosreis',
        'CLIENT': {
            'host': os.environ.get("MONGO_HOST"),
            'port': int(os.environ.get("MONGO_PORT")),
            'username': os.environ.get("MONGO_INITDB_ROOT_USERNAME"),
            'password': os.environ.get("MONGO_INITDB_ROOT_PASSWORD"),
        }
    }
}

ALLOWED_HOSTS = ['admin', '127.0.0.1']
