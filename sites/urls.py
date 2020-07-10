from django.conf.urls import url
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns=[
    path('', views.home_page,name = 'home_page'),
    path('search/', views.search_results, name='search_results'),
    path('profile/(?P<username>\w+)', views.profile, name='profile'),
    path('upload/', views.upload_project, name='upload_project'),
    path('edit', views.edit, name='edit_profile'),
    path('rate/(?P<project_id>\d+)',views.rate_project, name='rate'),
    path('vote/(?P<project_id>\d+)',views.vote, name='vote'),
    path('api/profile/', views.ProfileList.as_view())
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)