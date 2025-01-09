from django.urls import path
from . import views

urlpatterns = [
    path('api/list_images/', views.list_images, name='list_images'),
    path('api/list_pdfs/', views.list_pdfs, name='list_pdfs'),
    path('api/get_image/<str:pk>/', views.get_image, name='get_image'),
    path('api/get_pdf/<str:pk>/', views.get_pdf, name='get_pdf'),
    path('api/delete_image/<str:pk>/', views.delete_image, name='delete_image'),
    path('api/delete_pdf/<str:pk>/', views.delete_pdf, name='delete_pdf'),
]
