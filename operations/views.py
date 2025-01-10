from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from rest_framework import status
from uploads.models import *
from uploads.serializers import *
from PIL import Image
# Create your views here.


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
