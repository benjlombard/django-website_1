from .base import *

DEBUG = True
ALLOWED_HOSTS = []
INTERNAL_IPS = ('127.0.0.1')

INSTALLED_APPS = [
    'debug_toolbar',
    'django_jenkins',
] + INSTALLED_APPS

MIDDLEWARE =[
    'debug_toolbar.middleware.DebugToolbarMiddleware',
] + MIDDLEWARE

TEMPLATE_DEBUG = True
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

#python manage jenkins --enable-coverage
#a folder reports is created with the file *.reports and *.xml
#this folder reports must be added to .gitignore
#the folder htmlcov must be also added to .gitignore
JENKINS_TASKS = [
    'django_jenkins.tasks.run_pep8',
    'django_jenkins.tasks.run_flake8',
    'django_jenkins.tasks.run_pyflakes',
    #"'django_jenkins.tasks.run_jslint',
    'django_jenkins.tasks.run_csslint',
    #'django_jenkins.tasks.run_sloccount',

    #by default
    #"'django_jenkins.tasks.run_pylint', => error with exit keyword
    #'django_jenkins.tasks.with_coverage', => plus besoin, à la place exécuter : python manage.py jenkins --enable-coverage
    #'django_jenkins.tasks.django_tests',
]
ADMIN_HONEYPOT_EMAIL_ADMINS = True
ADMINS =['benjamin.lombard.fr@gmail.com','mlsuyt@protonmail.com']

PROJECT_APPS=(
    'blog',
)
