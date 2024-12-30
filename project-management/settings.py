import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Define the base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Get the secret key from environment variables or use a default value
SECRET_KEY = os.getenv("SECRET_KEY", "your-default-secret-key")

# Set the debug mode based on environment variables
DEBUG = os.getenv("DEBUG", "True") == "True"

# Define the allowed hosts for the application
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "localhost").split(",")

# Define the installed applications
INSTALLED_APPS = [
    # Django admin application
    "django.contrib.admin",
    # Django authentication framework
    "django.contrib.auth",
    # Django content types framework
    "django.contrib.contenttypes",
    # Django sessions framework
    "django.contrib.sessions",
    # Django messages framework
    "django.contrib.messages",
    # Django static files handling
    "django.contrib.staticfiles",
    # Django REST framework
    "rest_framework",
    # Django CORS headers
    "corsheaders",
    # Core application
    "core",
]

# Define the middleware for the application
MIDDLEWARE = [
    # Security middleware
    "django.middleware.security.SecurityMiddleware",
    # Session middleware
    "django.contrib.sessions.middleware.SessionMiddleware",
    # Common middleware
    "django.middleware.common.CommonMiddleware",
    # CSRF protection middleware
    "django.middleware.csrf.CsrfViewMiddleware",
    # Authentication middleware
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    # Message middleware
    "django.contrib.messages.middleware.MessageMiddleware",
    # Clickjacking protection middleware
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # CORS headers middleware
    "corsheaders.middleware.CorsMiddleware",
]

ROOT_URLCONF = "project_management.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "project_management.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv('DB_NAME'),
        "USER": os.getenv('DB_USER'),
        "PASSWORD": os.getenv('DB_PASSWORD'),
        "HOST": os.getenv('DB_HOST', 'localhost'),
        "PORT": os.getenv('DB_PORT', '5432'),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
