from django.urls import URLPattern, path
from .views import homepageview
URLPatterns = [
    #the first empty string refers that if the user requests the homepage represented by the empty string the user view called homepageview
    path('',homepageview,name='home')
]