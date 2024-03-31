from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import CustomUser
from django.contrib.auth import login, logout


def user(request):
    context = {'user': request.user}
    return render(request, 'user.html', context)


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        new_user = CustomUser(username=username, password=password)
        new_user.save()
        return HttpResponse('ユーザーの作成に成功しました')
    return HttpResponseRedirect('/')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = CustomUser.objects.get(username=username)
        except CustomUser.DoesNotExist:
            return HttpResponse('ログインに失敗しました')

        if user.password == password:
            login(request, user)  # ユーザをログイン状態にする
            return HttpResponseRedirect('/')
        else:
            return HttpResponse('ログインに失敗しました')
    return HttpResponseRedirect('/')


def signout(request):
    logout(request)
    return HttpResponseRedirect('/')
