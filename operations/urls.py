from django.urls import path
from . import views




urlpatterns = [
    path('api/rotate_image/', views.rotate_image, name='rotate_image'),
]