from django.contrib import admin
from .models import Project, Task, TeamMember

# Register the Project model with the admin site
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    # Display these fields in the list view
    list_display = ("name", "start_date", "end_date")
    # Add search functionality for these fields
    search_fields = ("name", "description")

# Register the Task model with the admin site
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    # Display these fields in the list view
    list_display = ("title", "due_date", "project")
    # Add filter functionality for these fields
    list_filter = ("due_date", "project")
    # Add search functionality for these fields
    search_fields = ("title", "description")

# Register the TeamMember model with the admin site
@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    # Display these fields in the list view
    list_display = ("name", "email")
    # Add search functionality for these fields
    search_fields = ("name", "email")
