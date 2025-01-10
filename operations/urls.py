from django.urls import path
from . import views




urlpatterns = [
    path('api/rotate_image/', views.rotate_image, name='rotate_image'),
    path('api/convert_pdf_to_image/', views.convert_pdf_to_image, name='convert_pdf_to_image'),
]