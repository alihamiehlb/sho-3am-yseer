from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_list, name='news_list'),  # Root path for /news/
    path('fetch/', views.fetch_messages, name='fetch_messages'), 
]
