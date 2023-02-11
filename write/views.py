from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
import requests
import json
from django.utils import timezone
from .models import Write, Photo

def write(request):
    return render(request, 'write/write.html')

def write_form(request):

    if request.method == 'POST':

        write = Write()

        write.title = request.POST['intro']
        write.things = request.POST['detail']
        write.pub_date = timezone.now()
        write.save()
        for img in request.FILES.getlist('images'):
            photo = Photo()
            photo.write_id = write.id
            photo.image = img
            photo.save()
    return redirect('/write')
