import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from .models import User


def due_error(request):
    context = {'getIndexData': '访问出错，请重试或点击下方按钮返回主页！'}
    return render(request, 'index.html', context)


@csrf_exempt
def due_login(request):
    if request.method == "POST":
        username = request.POST['username']
        passwd = request.POST['passwd']
        # 检查数据库中是否存在该用户信息
        tmp = User.objects.filter(name=username).exists()
        if tmp:
            check_login = User.objects.filter(name=username, passwd=passwd).exists()
            if check_login:
                # 下述get无法应用于登录验证，仅可获取用户信息
                test_user = User.objects.get(name=username, passwd=passwd)
                data = json.loads(serializers.serialize('json', [test_user]))
                return JsonResponse(data, safe=False)
            else:
                return JsonResponse('验证失败', safe=False)
        else:
            print(789)
            return render(request, 'index.html', {'getIndexData': '尚未注册'})
    else:
        return render(request, 'index.html', {'getIndexData': '非法请求，已记录您的IP地址信息'})


@csrf_exempt
def due_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        passwd = request.POST['passwd']
        # 检查数据库中是否存在该用户信息
        tmp = User.objects.filter(name=username).exists()
        if tmp:
            return JsonResponse('该用户已存在', safe=False)
        else:
            if User.objects.create(name=username, passwd=passwd, space_size=100, level_vip=0, online_status=0):
                return JsonResponse('注册成功', safe=False)
            else:
                return JsonResponse("注册出错", safe=False)
