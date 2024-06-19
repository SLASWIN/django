from django.urls import path
from newapp.views import *
urlpatterns = [
    path('reg/',register),
    path('lg',log)
]