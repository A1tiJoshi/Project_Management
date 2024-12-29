from django.contrib import admin
from django.urls import path, include

# Define the URL patterns for the project
urlpatterns = [
    # URL pattern for the Django admin site
    path("admin/", admin.site.urls),
    # URL pattern for the core application API
    path("api/core/", include("core.urls")),
]
