from django.urls import path 
from . import views

urlpatterns=[
    path('fb/', views.facebook, name='fb' )
]