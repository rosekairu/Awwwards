from django.conf.urls import url
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns=[
    path('', views.home_page,name = 'home'),
    path('search/', views.search_results, name='search_results'),
    #url(r'^profile/(?P<username>[\w.@+-]+)/$', views.profile, name='profile'),
    path('project/<post>/', views.view_project, name='project'),
    path('profile/<username>/', views.profile, name='profile'),
    path('upload/', views.upload_project, name='upload_project'),
    path('edit', views.edit, name='edit-profile'),
    #path('rate/<int:pk>',views.rate_project, name='rate'),
    url(r'^rate/(?P<project_id>\d+)',views.rate_project, name='rate'),
    url(r'^vote/(?P<project_id>\d+)',views.vote, name='vote'),
    #path('vote/',views.vote, name='vote'), 
    path('api/profile/', views.ProfileList.as_view(), name='profile_list'),
    path('api/project/', views.ProjectList.as_view(), name='project_list'),
    url(r'^password/$', views.change_password, name='change_password'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)