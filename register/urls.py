from django.urls import path,include
from .views import *

urlpatterns = [
    
    path('add_Student/', create_Students, name='add_Students')
]