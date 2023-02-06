"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

import main.views
import write.views
#import viewer.views
urlpatterns = [
    path('viewer/', include('viewer.urls')),
    #path('write/', include('write.urls')),
    path('write/', write.views.write, name='write'),
    path('', main.views.index, name='index'),
    path("admin/", admin.site.urls),
    path('createform/', main.views.createform, name='createform'),
    path('write_form/', write.views.write_form, name = 'write_form'),
    #path('', include('write.urls')),
    #path('write/', include('write.urls')),
    #path('write/', write.views.write, name='write'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
