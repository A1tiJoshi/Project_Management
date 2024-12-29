from rest_framework import serializers
from .models import Project, Task, TeamMember

# Serializer for the Project model
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        # Specify the model to be serialized
        model = Project
        # Include all fields in the serialization
        fields = "__all__"

# Serializer for the Task model
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        # Specify the model to be serialized
        model = Task
        # Include all fields in the serialization
        fields = "__all__"

# Serializer for the TeamMember model
class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        # Specify the model to be serialized
        model = TeamMember
        # Include all fields in the serialization
        fields = "__all__"
