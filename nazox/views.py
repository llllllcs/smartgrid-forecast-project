from django.http import request
from django.shortcuts import redirect, render
from django.views import View   
from django.contrib.auth.mixins import LoginRequiredMixin

# Dashboard
class DashboardView(LoginRequiredMixin,View):
    def get(self, request):
        print(request.session)
        greeting = {}
        greeting['title'] = "实时监控看板"
        greeting['pageview'] = "运行过程监控"
        return render(request, 'menu/index-2.html', greeting)  # 原先是menu/index.html

# Calender
class CalendarView(LoginRequiredMixin,View):
    def get(self, request):
        greeting = {}
        greeting['title'] = "Calendar"
        greeting['pageview'] = "VisionNav"
        return render(request, 'menu/calendar.html',greeting)

# Chat
class ChatView(LoginRequiredMixin,View):
    def get(self, request):
        greeting = {}
        greeting['title'] = "Chat"
        greeting['pageview'] = "VisionNav"
        return render(request, 'menu/apps-chat.html',greeting)

# Kanban Board
class KanbanBoardView(LoginRequiredMixin,View):
    def get(self, request):
        greeting = {}
        greeting['title'] = "Kanban Board"
        greeting['pageview'] = "VisionNav"
        return render(request, 'menu/apps-kanban-board.html',greeting)

def bar_wait_simultaneous_f(request):
    return render(request, 'pages/utility/mycharts_8.html', {})


def pie_wait_2_f(request):
    return render(request, 'pages/utility/mycharts_9.html', {})