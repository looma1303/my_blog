from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Command
from django.shortcuts import redirect
import requests
import json
from write.models import Write, Photo


def index(request):
    template = loader.get_template('main/index.html')
    message = '안녕하세요.'

    return HttpResponse(template.render({'message':message}, request))




def createform(request):

    command_list= ['clear', '?', 'write']
    template = loader.get_template('main/index.html')
    if request.method == 'POST':
        user = Command()
        user.cmd = request.POST['cmd']
        if user.cmd[0] == "/":
            length= -1 * len(user.cmd)
            user.cmd = user.cmd[length + 1:]
            cmd_state = "NOT FOUND"
            for x in command_list:
                if user.cmd == x:
                    cmd_state = "FOUND"
                    command = x
                    #print('command:',x)
                else:
                    pass
            if cmd_state == "FOUND":
                message = run_command(command)
                #print(message,type(x))
            else:
                message = "명령어를 찾을 수 없습니다."
        else:
            message = "값이 입력 되지 않았습니다."
        user.save()
    return HttpResponse(template.render({'message':message}, request))


def run_command(command):
    if command == 'clear':
        result = "안녕하세요"
    elif command == '?':
        result = "/clear: 초기화"
    elif command == 'write':
        result = 'need_write_page'
    else:
        pass
    return result
