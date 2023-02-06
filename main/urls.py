from django.urls import path
from . import views
from write.models import Write, Photo

app_name = 'viewer'

urlpatterns = [
    path('', views.index, name='index'),
    path('write/', include('write.urls')),



    ]
