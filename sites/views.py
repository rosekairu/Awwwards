import datetime as dt
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile, Project,Rate
from .forms import ProjectForm,ProfileForm,RateForm
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializer import ProfileSerializer,ProjectSerializer
from .permissions import IsAdminOrReadOnly
from django.core.exceptions import ObjectDoesNotExist


def convert_dates(dates):
    # function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    '''
    Returns the actual day of the week
    '''
    day = days[day_number]
    return day

# Create your views here.
def home_page(request):
    date = dt.date.today()
    project = Project.objects.all()
    return render(request,'home.html',locals())


def search_results(request):
    profile= Profile.objects.all()
    project= Project.objects.all()
    if 'Project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_project = Project.search_by_profile(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',locals())

    else:
        message = "You haven't searched for any term"
        return render(request,'search.html',{"message":message})


@login_required(login_url='/accounts/login/')
def profile(request, username):
    
    app = Project.objects.all()
    profile = User.objects.get(username=username)
    # print(profile.id)

    try:
        profile_details = Profile.get_by_id(profile.id)
    except:
        profile_details = Profile.filter_by_id(profile.id)

    app = Project.get_profile_projects(profile.id)
    title = f'@{profile.username} awwward projects and screenshots'

    return render(request, 'profile.html', locals())
    
    
#editing user profile fillform & submission
@login_required(login_url='/accounts/login/')
def edit(request):
    profile = User.objects.get(username=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            edit = form.save(commit=False)
            edit.user = request.user
            edit.save()
            return redirect('sites:edit-profile')
    else:
        form = ProfileForm()
    return render(request, 'edit-profile.html', locals())


#logs out current user from account
def logout(request):
    return render(request, 'home.html')


@login_required(login_url='/accounts/login')
def upload_project(request):
    if request.method == 'POST':
        uploadform = ProjectForm(request.POST, request.FILES)
        if uploadform.is_valid():
            upload = uploadform.save(commit=False)
            upload.profile = request.user
            upload.save()
            return redirect('sites:home')
    else:
        uploadform = ProjectForm()
    return render(request,'update-project.html',locals())


def view_project(request):
    project = Project.objects.get_all()
    return render(request,'home.html', locals())


def rate(request):
    profile = User.objects.get(username=request.user)
    return render(request,'rate.html',locals())

def view_rate(request,project_id):
    user = User.objects.get(username=request.user)
    project = Project.objects.get(pk=project_id)
    rate = Rate.objects.filter(project_id=project_id)
    print(rate)
    return render(request,'project.html',locals())

@login_required(login_url='/accounts/login')
def rate_project(request,project_id):
    project = Project.objects.get(pk=project_id)
    profile = User.objects.get(username=request.user)
    if request.method == 'POST':
        rateform = RateForm(request.POST, request.FILES)
        print(rateform.errors)
        if rateform.is_valid():
            rating = rateform.save(commit=False)
            rating.project = project
            rating.user = request.user
            rating.save()
            return redirect('vote',project_id)
    else:
        rateform = RateForm()
    return render(request,'rate.html',locals())

@login_required(login_url='/accounts/login/')
def vote(request,project_id):
   try:
       project = Project.objects.get(pk=project_id)
       rate = Rate.objects.filter(project_id=project_id).all()
       print([r.project_id for r in rate])
       rateform = RateForm()
   except ObjectDoesNotExist:
       raise Http404()
   return render(request,"project.html", locals())


class ProfileList(APIView):
    def get(self, request, format=None):
        all_profile = Profile.objects.all()
        serializers = ProfileSerializer(all_profile, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = ProfileSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    permission_classes = (IsAdminOrReadOnly,)

class ProjectList(APIView):
    def get(self, request, format=None):
        all_project = Project.objects.all()
        serializers = ProjectSerializer(all_project, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = ProjectSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
    permission_classes = (IsAdminOrReadOnly,)
 