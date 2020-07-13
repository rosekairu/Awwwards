from rest_framework import serializers
from .models import Profile,Project

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user', 'profile_picture', 'bio', 'rate')

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('project_name','screenshot','details','project_url')