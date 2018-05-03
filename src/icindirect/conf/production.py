import raven

from .base import *  # noqa

#
# Standard Django settings.
#
ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

# Caching sessions.
# SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
# SESSION_CACHE_ALIAS = "default"

# Caching templates.
TEMPLATES[0]['OPTIONS']['loaders'] = [
    ('django.template.loaders.cached.Loader', RAW_TEMPLATE_LOADERS),
]

# The file storage engine to use when collecting static files with the
# collectstatic management command.
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

# Production logging facility.
LOGGING['loggers'].update({
    '': {
        'handlers': ['sentry'],
        'level': 'ERROR',
        'propagate': False,
    },
    'django': {
        'handlers': ['django'],
        'level': 'INFO',
        'propagate': True,
    },
    'django.security.DisallowedHost': {
        'handlers': ['django'],
        'level': 'CRITICAL',
        'propagate': False,
    },
})

#
# Custom settings
#

# Show active environment in admin.
ENVIRONMENT = 'production'
SHOW_ALERT = False

# We will assume we're running under https
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_SECURE = True
X_FRAME_OPTIONS = 'DENY'

# Only set this when we're behind Nginx as configured in our example-deployment
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_CONTENT_TYPE_NOSNIFF = True  # Sets X-Content-Type-Options: nosniff
SECURE_BROWSER_XSS_FILTER = True  # Sets X-XSS-Protection: 1; mode=block

#
# Library settings
#

# Raven
INSTALLED_APPS = INSTALLED_APPS + [
    'raven.contrib.django.raven_compat',
]
RAVEN_CONFIG = {
    'dsn': os.getenv('RAVEN_DNS'),
    'release': raven.fetch_git_sha(BASE_DIR),
}
LOGGING['handlers'].update({
    'sentry': {
        'level': 'WARNING',
        'class': 'raven.handlers.logging.SentryHandler',
        'dsn': RAVEN_CONFIG['dsn']
    },
})
