from django.urls import path, include, re_path
from django.views.generic import ListView, DetailView
from .models import News

from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('news/', ListView.as_view(queryset=News.objects.all().order_by("-pub_date")[:20], template_name="news/posts.html")),
    path('<int:news_id>/', views.detail, name= 'detail'),
    path('<int:news_id>/leave_comment/', views.leave_comment, name= 'leave_comment'),
    # path('register/', views.Register, name='Register')
]