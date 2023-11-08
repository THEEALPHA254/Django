from django.urls import path,include
from .views import *
urlpatterns = [
    
    path('add_fee/', create_Fee_balance, name='add_Fee_balance')
]