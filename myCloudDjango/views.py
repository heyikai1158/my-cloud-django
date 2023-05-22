from django.shortcuts import render


def due_error(request):
    context = {'getIndexData': '访问出错，请重试或点击下方按钮返回主页！'}
    return render(request, 'index.html', context)
