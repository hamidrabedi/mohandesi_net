from .base import (
    INSTALLED_APPS,
    MIDDLEWARE,
)

from decouple import config
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

INSTALLED_APPS.insert(0,'jazzmin')
INSTALLED_APPS+= [
    'user',
    'comment',
    'product',
    'pages',
    'django_user_agents',
    'django_filters',
    'cacheops',
]

MIDDLEWARE+= [
    'django_user_agents.middleware.UserAgentMiddleware',
    'utils.exception_handler.ErrorHandlerMiddleware' #for capturing exceptions
]

# ######################## #
#   DJANGO DEBUG TOOLBAR   #
# ######################## #
if config("DEBUG_TOOLBAR", default=False, cast=bool):
    INSTALLED_APPS.append('debug_toolbar')
    MIDDLEWARE.insert(0, 'debug_toolbar.middleware.DebugToolbarMiddleware')

    def show_toolbar(request):
        return True
    DEBUG_TOOLBAR_CONFIG = {
        "SHOW_TOOLBAR_CALLBACK" : show_toolbar,
    }

# ########## #
#   SENTRY   #
# ########## #
sentry_sdk.init(
    dsn=config("DSN"),
    integrations=[DjangoIntegration()],
    traces_sample_rate=1.0,
    send_default_pii=True
)

# ################ #
#    Thumbnail     #
# ################ #
THUMBNAIL_DEBUG = config('THUMBNAIL_DEBUG', cast=bool)

THUMBNAIL_KVSTORE = 'sorl.thumbnail.kvstores.redis_kvstore.KVStore'
THUMBNAIL_ENGINE = 'sorl.thumbnail.engines.pil_engine.Engine'
THUMBNAIL_FORMAT='JPEG'
THUMBNAIL_REDIS_DB = config('REDIS_THUMBNAIL_DATABASE', cast=int)
THUMBNAIL_REDIS_PASSWORD=config('REDIS_PASSWORD')
THUMBNAIL_REDIS_HOST=config('REDIS_HOST')
THUMBNAIL_REDIS_PORT=config('REDIS_PORT')
THUMBNAIL_KEY_PREFIX=config('THUMBNAIL_KEY_PREFIX')


# ######### #
#   CACHE   #
# ######### #

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"

REDIS_AUTHENTICATION_URL = f"{config('REDIS_USER')}:{config('REDIS_PASSWORD')}"
REDIS_ADDRESS = f"{config('REDIS_HOST')}:{config('REDIS_PORT')}"
REDIS_DB = config("REDIS_DATABASE")
REDIS_TEST_DB = config("REDIS_TEST_DATABASE")
REDIS_PROTO = config('REDIS_PROTOCOL')

REDIS_TEST_CONNECTION_URL = f"{REDIS_PROTO}://{REDIS_AUTHENTICATION_URL}@{REDIS_ADDRESS}/{REDIS_TEST_DB}"
REDIS_CONNECTION_URL = f"{REDIS_PROTO}://{REDIS_AUTHENTICATION_URL}@{REDIS_ADDRESS}/{REDIS_DB}"

CACHEOPS_REDIS = REDIS_CONNECTION_URL

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": REDIS_CONNECTION_URL,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "COMPRESSOR": "django_redis.compressors.zlib.ZlibCompressor",
        }
    },
    "test": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": REDIS_TEST_CONNECTION_URL,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
        
    }
}

CACHEOPS = {
    'product.*':{'ops': 'all','timeout':60*60},
    'pages.*':{'ops': 'all','timeout':60*60}
}