from django.shortcuts import render
from rest_framework import status
from django.http import JsonResponse
from .models import *
from rest_framework.decorators import api_view
from .serializers import *
from .utils import *
# Create your views here.



#endpoint to upload images and pdfs
@api_view(['POST'])
def upload_file(request):
    uploaded_item = request.FILES.get('file')

    if not upload_file:
        return JsonResponse({'error': 'no file uploaded.'}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        item_type = uploaded_item.content_type


        updated_name = update_filename(uploaded_item.name)
        uploaded_item.name = updated_name

        
        if item_type.startswith('image/'):
            serializer = ImageFileSerializer(data={'image_item': uploaded_item, 'name': uploaded_item.name})
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({'message': 'image uploaded successfully.'}, status=status.HTTP_201_CREATED)
            else:
                return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        elif item_type == 'application/pdf':
            pages = get_pdf_page(uploaded_item)
            serializer = PDFFileSerializer(data={'pdf_item': uploaded_item, 'name': uploaded_item.name, 'pages': pages})
            if serializer.is_valid():
                serializer.save(pages=pages)
                return JsonResponse({'message': 'pdf uploaded successfully.'}, status=status.HTTP_201_CREATED)
            else:
                return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        else:
            return JsonResponse({'error': 'unsupported file type.'}, status=status.HTTP_400_BAD_REQUEST)
        
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            

            