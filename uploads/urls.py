from django.urls import path
from . import views

urlpatterns = [
    path('api/upload_file/', views.upload_file, name='upload_file')
]