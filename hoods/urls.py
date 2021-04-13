from django.urls import path,re_path
# from . import views
from .views import (
    home,
    neighbourhood,
    details,
    join_hood,
    leave_hood,
    profile,
    search_business,
)
app_name='hoods'
urlpatterns = [
    path('',home, name='home'),
    path('neighbourhood/',neighbourhood,name='neighbourhood'),
    path('search_business/',search_business,name='search_business'),
    path('details/<int:id>/',details,name='details'),
    path('join_hood/<id>',join_hood,name='join_hood'),
    path('leave_hood/<id>',leave_hood,name='leave_hood'),
    path('profile/<prof_id>', profile, name='profile'),

]