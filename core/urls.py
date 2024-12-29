from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, TaskViewSet, TeamMemberViewSet

# Create a router and register our viewsets with it
router = DefaultRouter()
router.register("projects", ProjectViewSet)
router.register("tasks", TaskViewSet)
router.register("team-members", TeamMemberViewSet)

# The API URLs are now determined automatically by the router
urlpatterns = [
    # Include the router URLs in the urlpatterns
    path("", include(router.urls)),
]
