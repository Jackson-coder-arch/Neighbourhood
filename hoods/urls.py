from django.urls import path
# from . import views
from .views import (
    home,
    neighbourhood,
    business,
)
app_name='hoods'
urlpatterns = [
    path('',home, name='home'),
    path('neighbourhood/',neighbourhood,name='neighbourHood'),
    path('business/',business,name='business')
]