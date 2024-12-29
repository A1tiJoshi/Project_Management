from django.db import models

# Define the Project model
class Project(models.Model):
    # Name of the project
    name = models.CharField(max_length=255)
    # Description of the project
    description = models.TextField()
    # Start date of the project
    start_date = models.DateField()
    # End date of the project
    end_date = models.DateField()

# Define the Task model
class Task(models.Model):
    # Title of the task
    title = models.CharField(max_length=255)
    # Description of the task
    description = models.TextField()
    # Due date of the task
    due_date = models.DateField()
    # Foreign key to the Project model
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="tasks")

# Define the TeamMember model
class TeamMember(models.Model):
    # Name of the team member
    name = models.CharField(max_length=255)
    # Email of the team member
    email = models.EmailField(unique=True)
    # Many-to-many relationship with the Project model
    project = models.ManyToManyField(Project, related_name="team_members")
