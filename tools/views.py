# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from .forms import AddForm


def index(request):
    if request.method == 'POST':  # 当提交表单时
        form = AddForm(request.POST)  # form 包含提交的数据
        if form.is_valid():  # 如果提交的数据合法
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            return HttpResponse(str(int(a) + int(b)))
    else:  # 当正常访问时
        form = AddForm()

    return render(request, 'tools/index.html', {'form': form})


def send_email(request):
    send_mail('From Django', 'Hello World!', '彭伟<18810662532@163.com>',
              ['pwalan@qq.com'], fail_silently=False)
    return HttpResponse("Send Success!")
