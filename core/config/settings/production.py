from decouple import Config, RepositoryEnv

from .base import *  # noqa

# Specify the env files path
production_django_env_file = path.join(BASE_DIR, ".production", ".django")

production_django_config = Config(RepositoryEnv(production_django_env_file))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = production_django_config("DJANGO_PRODUCTION_SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = production_django_config(
    "DJANGO_PRODUCTION_ALLOWED_HOSTS",
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
