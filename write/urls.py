from django.urls import path
from . import views, previewer
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.write, name='write'),
    #path('', previewer.preview, name = 'preview')


    ] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
