from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'j3rz@b0+r6^q9itb-0rd=1=wpso2$y0bo&&7j0xne!6bl#5xt3'
# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'), )
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')



MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')