from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from rest_framework import status
from uploads.models import *
from uploads.serializers import *
from PIL import Image
from pdf2image import convert_from_path
import os
from django.conf import settings
# Create your views here.


#endpoint to rotate images
@api_view(['POST'])
def rotate_image(request):

    try:
        image_id = request.data.get('image_id')
        angle = request.data.get('angle')

        if not image_id or angle is None:
            return JsonResponse({'error': 'image id and angle are required.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            angle = int(angle)
        except ValueError:
            return JsonResponse({'error': 'invalid rotation angle. need to be an integer.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            image_obj = ImageFile.objects.get(id=image_id)
        except ImageFile.DoesNotExist:
            return JsonResponse({'error': 'image not found.'}, status=status.HTTP_400_BAD_REQUEST)

        image_path = image_obj.image_item.path
        content_type = Image.MIME[Image.open(image_path).format]

        with Image.open(image_path) as image_item:
            rotated_img = image_item.rotate(angle, expand=True)

            response = HttpResponse(content_type)
            rotated_img.save(response, image_item.format)
            return response

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




#endpoint to convert pdf to images
@api_view(['POST'])
def convert_pdf_to_image(request):
    try:
        pdf_id = request.data.get('pdf_id')
        if not pdf_id:
            return JsonResponse({'error': 'pdf id is required.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            pdf_obj = PDFFile.objects.get(id=pdf_id)
        except PDFFile.DoesNotExist:
            return JsonResponse({'error': 'pdf not found.'}, status=status.HTTP_404_NOT_FOUND)

        pdf_path = pdf_obj.pdf_item.path

        #poppler path of my pc
        poppler_path = r'C:\Users\User\Poppler\Release-24.08.0-0\poppler-24.08.0\Library\bin'

        #adding poppler path to env
        os.environ["PATH"] += os.pathsep + poppler_path

        try:
            pages = convert_from_path(pdf_path, dpi=300)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        if len(pages) == 0:
            return JsonResponse({'error': 'no pages found in the pdf.'}, status=status.HTTP_400_BAD_REQUEST)


        directory_path = os.path.join(settings.MEDIA_ROOT, 'images', pdf_obj.name)
        if not os.path.exists(directory_path):
            os.makedirs(directory_path, exist_ok=True)

        for iterate, page in enumerate(pages):
            image_name = f'{iterate + 1}.png'
            
            image_path = os.path.join(directory_path, image_name)
            
            page.save(image_path, 'PNG')

            image_file = ImageFile.objects.create(
                name=image_name,
                image_item=f'images/{pdf_obj.name}/{image_name}'
            )
            

        return JsonResponse({'message': 'pdf converted successfully. images saved in the converted folder.'}, status=status.HTTP_200_OK)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)