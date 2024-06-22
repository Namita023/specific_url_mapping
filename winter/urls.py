from django.urls import path
from winter.views import *

app_name="anything"

urlpatterns=[
    path('apple/',apple,name='apple'),
    path('guava/',guava,name='guava'),
]