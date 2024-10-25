from django.shortcuts import render
from django.http import JsonResponse
from .telegram_client import fetch_telegram_messages

def news_list(request):
    messages = fetch_telegram_messages()
    return render(request, 'news/news.html', {'messages': messages})

def fetch_messages(request):
    messages = fetch_telegram_messages()
    return JsonResponse(messages, safe=False)
