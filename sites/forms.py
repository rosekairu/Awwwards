from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Project, Profile, Rate

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['user', 'pub_date', 'profile']
        fields = ('project_name', 'details', 'project_url', 'screenshot')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user','rate']
        fields = ['profile_picture', 'bio', 'contact_info']

class RateForm(forms.ModelForm):
    class Meta:
        model =Rate
        exclude= ['user','project']