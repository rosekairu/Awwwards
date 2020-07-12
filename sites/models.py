from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime as dt

# Create your models here.
class Profile(models.Model):
    profile_picture = models.ImageField(upload_to = 'images/',blank=True)
    user = models.OneToOneField(User,default="",on_delete=models.CASCADE, primary_key=True)    
    bio = models.TextField(default="", max_length = 50,null = True)
    contact_info = models.CharField(max_length=200, blank=True)
    join_date = models.DateTimeField(auto_now_add=True, null=True)
    profile_Id = models.IntegerField(default=0)
    all_projects = models.ForeignKey('Project', on_delete=models.PROTECT, null=True)
    rate = models.ManyToManyField('Project', related_name='image',max_length=30)

    def __str__(self):
        return self.bio

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def update_bio(self, bio):
        self.bio = bio
        self.save()

    @classmethod
    def get_profile_data(cls):
        return Profile.objects.all()

    @classmethod
    def get_by_id(cls, id):
        details = Profile.objects.get(user = id)
        return details

    @classmethod
    def filter_by_id(cls, id):
        details = Profile.objects.filter(user = id).first()
        return details

    @classmethod
    def search_user(cls, name):
        userprofile = Profile.objects.filter(user__username__icontains = name)
        return userprofile

    class Meta:
        db_table = 'profiles'


class Project(models.Model):
    screenshot = models.ImageField(upload_to = 'images/')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    project_name = models.CharField(max_length =10)
    pub_date = models.DateTimeField(auto_now_add=True, null=True)
    details = models.TextField()
    project_url = models.CharField(max_length =50)
    user_project_id = models.IntegerField(default=0)
    design = models.IntegerField(choices=list(zip(range(0, 11), range(0, 11))), default=0)
    usability = models.IntegerField(choices=list(zip(range(0, 11), range(0, 11))), default=0)
    creativity = models.IntegerField(choices=list(zip(range(0, 11), range(0, 11))), default=0)
    content = models.IntegerField(choices=list(zip(range(0, 11), range(0, 11))), default=0)
    vote_submissions = models.IntegerField(default=0)


    class Meta:
        ordering = ['-pk']

    def save_project(self):
        self.save()
    
    @classmethod
    def get_project(cls, profile):
        project = Project.objects.filter(Profile__pk = profile)
        return project
    
    @classmethod
    def get_all_projects(cls):
        project = Project.objects.all()
        return project

    @classmethod
    def search_by_profile(cls,search_term):
        proj = cls.objects.filter(profile__name__icontains=search_term)
        return proj

    @classmethod
    def get_profile_projects(cls, profile):
        project = Project.objects.filter(profile__pk = profile)
        return project

    @classmethod
    def find_project_id(cls, id):
        identity = Project.objects.get(pk=id)
        return identity

class Rate(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, null = True)
    project = models.ForeignKey(Project,on_delete=models.PROTECT,related_name='rate',null=True)
    design = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    usability = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)], null=True)
    creativity = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)],blank=True,null=True)
    content = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    average = models.FloatField(max_length=8)
    

    def __str__(self):
        return self.design

    def save_rate(self):
        self.save()

    def delete_rate(self):
        self.delete()

    class Meta:
        db_table = 'ratings'

    @classmethod
    def get_rate(cls, profile):
        rate = Rate.objects.filter(Profile__pk = profile)
        return rate
    
    @classmethod
    def get_all_rating(cls):
        rating = Rate.objects.all()
        return rating


class Comment(models.Model):
    comment = models.CharField(max_length=80, null=True)
    user = models.ForeignKey(User, null=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.comment

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()

    class Meta:
        db_table = 'comments'
        ordering = ["-id"]