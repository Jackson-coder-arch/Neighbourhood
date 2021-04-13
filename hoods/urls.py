from django.urls import path
# from . import views
from .views import (
    home,
    neighbourhood,
    business,
    posts,
    details,
)
app_name='hoods'
urlpatterns = [
    path('',home, name='home'),
    path('neighbourhood/',neighbourhood,name='neighbourHood'),
    path('business/',business,name='business'),
    path('posts/',posts,name='posts'),
    path('details/<id>/',details,name='details')
]