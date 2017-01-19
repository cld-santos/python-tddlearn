import os

DEBUG = True
ALLOWED_HOSTS = []
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = 'local'
ROOT_URLCONF = 'web.urls'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'python_tddlearn',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

INSTALLED_APPS = (
    'django.contrib.staticfiles',
    # our_apps
    'scrum_board',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, "web", "templates"),
        ],
    },
]

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "web", 'static'),
)

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
