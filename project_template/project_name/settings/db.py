from pathlib import Path

from environs import Env

env = Env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

DEFAULT_DB = env.str("DB_CONNECTION", "sqlite")

DB_CONNECTIONS = {
    'sqlite': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
    "postgres": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env.str("POSTGRES_DB", "postgres"),
        "USER": env.str("POSTGRES_USER", "postgres"),
        "PASSWORD": env.str("POSTGRES_PASSWORD", "secret"),
        "HOST": env.str("POSTGRES_HOST", "127.0.0.1"),
        "PORT": env.int("POSTGRES_PORT", 5432),
    }
}

# Database
# https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#databases
DATABASES = {
    'default': DB_CONNECTIONS[DEFAULT_DB],
    **DB_CONNECTIONS
}