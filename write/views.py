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
        #write.pics = request.FILES.get('images')
        write.pub_date = timezone.now()
        write.save()
        for img in request.FILES.getlist('images'):
            # Photo 객체를 하나 생성한다.
            photo = Photo()
            # 외래키로 현재 생성한 Post의 기본키를 참조한다.
            photo.write_id = write.id
            # imgs로부터 가져온 이미지 파일 하나를 저장한다.
            photo.image = img
            # 데이터베이스에 저장
            photo.save()
    return redirect('/write')
