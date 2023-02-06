from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
import requests
import json
from write.models import Write, Photo

def viewer(request, write_id):
    template = loader.get_template('viewer/viewer.html')
    result = write_id
    return HttpResponse(template.render({'write_id':result}, request))



'''
viewer에서 id를 안주고 things를 list화 사켜서 주면
photo가 key를 못얻음.
viewer list 앞에 write_id 넣어주고 html에서 어떠한 변수가 받아먹도록 해주기.

[글 1, img, 글 2, img]
for x in list:
    if x == @img:
        for y in photo_result:
            img:y
    else:
        p_tag

'''
