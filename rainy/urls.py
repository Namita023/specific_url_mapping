from django.urls import path
from rainy.views import *

app_name="anything"

urlpatterns=[
    path('pear/',pear,name='pear'),
    path('blueberry/',blueberry,name='blueberry'),
]