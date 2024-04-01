# webCrawler/crawler/urls.py
from django.urls import path
from . import views  # Import views from the current directory

# For URLs that end in /post/, use the handle_post function found in the views.py
# you can make a POST request to https://www.gaslightai.com/api/post/
urlpatterns = [
    path('get/', views.handle_get, name='handle_get'),
]
