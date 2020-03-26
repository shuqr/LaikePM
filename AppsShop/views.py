# -*- coding: utf-8 -*-

from django.http import HttpResponse

from django.shortcuts import render
from AppsShop.models import AppVersion


# 数据库操作
def add(request):
    appVersion = AppVersion()
    appVersion.appName = request.GET['appName']
    appVersion.version = request.GET['version']
    appVersion.versionCode = request.GET['versionCode']
    appVersion.branchName = request.GET['branchName']
    appVersion.downloadUrl = request.GET['downloadUrl']
    appVersion.save()
    return HttpResponse("success")


def show(request):
    ctx = {}
    list = AppVersion.objects.filter(appName='小千助手').order_by('-createTime')[:20]
    ctx['list'] = list
    return render(request, 'apps.html', ctx)
