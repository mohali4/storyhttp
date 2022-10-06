from django.urls import re_path
from .views import story_server

urlpatterns = [
    re_path('.*',story_server)
]