from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8%v6$b2h(+$cq^&!n2q9qg#d3+_@e7$7v4a+erdfu7gk1u#n+d'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['192.168.1.84', '192.168.1.84:8001']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


try:
    from .local import *
except ImportError:
    pass
