from django.http import request
from django.shortcuts import redirect, render
from django.views import View   
from django.contrib.auth.mixins import LoginRequiredMixin

# Email-Inbox
class InboxView(LoginRequiredMixin,View):
    def get(self, request):
        greeting = {}
        greeting['title'] = "系统交互验证"
        greeting['pageview'] = "离线仿真验证"
        return render(request, 'pages/utility/pages-starter.html',greeting)

# Read-Email
class ReadEmailView(LoginRequiredMixin,View):
    def get(self, request):
        greeting = {}
        greeting['title'] = "结果展示"
        greeting['pageview'] = "离线仿真验证"
        return render(request, 'pages/utility/pages-starter.html',greeting)