from django.urls import path
# from . import views
from .views import (
    home,
    neighbourhood,
    business,
    posts,
    details,
    join_hood,
    leave_hood,
)
app_name='hoods'
urlpatterns = [
    path('',home, name='home'),
    path('neighbourhood/',neighbourhood,name='neighbourhood'),
    path('business/',business,name='business'),
    path('posts/',posts,name='posts'),
    path('details/<int:id>/',details,name='details'),
    path('join_hood/<id>',join_hood,name='join_hood'),
    path('leave_hood/<id>',leave_hood,name='leave_hood'),

]