from decouple import Config, RepositoryEnv

from .base import *  # noqa

# specify the path
local_django_env_file_path = path.join(BASE_DIR, ".envs", ".local", ".django")
local_postgres_env_file_path = path.join(BASE_DIR, ".envs", ".local", ".postgres")


local_django_config = Config(RepositoryEnv(local_django_env_file_path))
local_postgres_config = Config(RepositoryEnv(local_postgres_env_file_path))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = local_django_config("DJANGO_LOCAL_SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = local_django_config(
    "DJANGO_LOCAL_ALLOWED_HOST",
    cast=lambda hosts: [host.strip() for host in hosts.split(",")],
)


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(name)-20s %(asctime)s %(module)s "
            "%(process)d %(thread)d %(message)s"
        }
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        }
    },
    "root": {"level": "INFO", "handler": ["console"]},
}
