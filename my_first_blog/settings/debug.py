from .base import *


config_secret_debug = json.loads(open(CONFIG_SECRET_DEBUG_FILE).read())

DEBUG = True

ALLOWED_HOSTS = config_secret_debug["django"]["allowed_hosts"]

WSGI_APPLICATION = 'my_first_blog.wsgi.debug.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
