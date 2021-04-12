from django.urls import path
from .views import (
    home,
    neighbourhood,
)
urlpatterns = [
    path('',home, name='home')
    path('neighbourhood/',neighbourhood,name='NeighbourHood')
]