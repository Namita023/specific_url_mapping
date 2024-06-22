from django.urls import path
from summer.views import *

app_name="anything"

urlpatterns=[
    path('mango/',mango,name='mango'),
    path('grapes/',grapes,name='grapes'),
]