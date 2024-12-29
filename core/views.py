from rest_framework.viewsets import ModelViewSet
from .models import Project, Task, TeamMember
from .serializers import ProjectSerializer, TaskSerializer, TeamMemberSerializer

# ViewSet for the Project model
class ProjectViewSet(ModelViewSet):
    # Define the queryset for the viewset
    queryset = Project.objects.all()
    # Specify the serializer class to be used
    serializer_class = ProjectSerializer

# ViewSet for the Task model
class TaskViewSet(ModelViewSet):
    # Define the queryset for the viewset
    queryset = Task.objects.all()
    # Specify the serializer class to be used
    serializer_class = TaskSerializer

# ViewSet for the TeamMember model
class TeamMemberViewSet(ModelViewSet):
    # Define the queryset for the viewset
    queryset = TeamMember.objects.all()
    # Specify the serializer class to be used
    serializer_class = TeamMemberSerializer
