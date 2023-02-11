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
