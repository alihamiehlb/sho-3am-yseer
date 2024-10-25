from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponseRedirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/', include('news.urls')),  # Route for the news
    path('', lambda request: HttpResponseRedirect('/news/')), # Redirect root to /news/
]
