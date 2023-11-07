from django.urls import path
from .views import *

urlpatterns = [
    path('members/', memberList, name='memberList'),
    path('members/<int:id>', memberDetails, name='memberDetails'),
    path('news/', newsList, name='newsList'),
    path('news/<int:id>', newsDetails, name='newsDetails'),
]