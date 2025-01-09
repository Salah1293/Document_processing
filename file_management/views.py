from django.shortcuts import render
from uploads.models import *
from uploads.serializers import *
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import JsonResponse
from rest_framework.response import Response
# Create your views here.

#endpoint to list all images
@api_view(['GET'])
def list_images(request):
    images_list = ImageFile.objects.all()
    
    if images_list.exists():
        data = ImageFileSerializer(images_list, many=True).data
        return JsonResponse(data, status=status.HTTP_200_OK, safe=False)
    else:
        return JsonResponse({'error': 'images not found.'}, status=status.HTTP_404_NOT_FOUND, safe=False)


#endpoint to list all pdfs
@api_view(['GET'])
def list_pdfs(request):
    pdfs_list = PDFFile.objects.all()

    if pdfs_list.exists():
        data = PDFFileSerializer(pdfs_list, many=True).data
        return JsonResponse(data, status=status.HTTP_200_OK, safe=False)
    else:
        return JsonResponse({'error': 'pdfs not found.'}, status=status.HTTP_404_NOT_FOUND, safe=False)
    

#endpoint to get image by id
@api_view(['GET'])
def get_image(request, pk):
    try:
        image_item = ImageFile.objects.get(pk=pk)
    except ImageFile.DoesNotExist:
        return Response({'error': 'image not found.'}, status=status.HTTP_404_NOT_FOUND)
    
    data = ImageFileSerializer(image_item).data
    return Response(data, status=status.HTTP_200_OK)



#endpoint to get pdf by id
@api_view(['GET'])
def get_pdf(request, pk):
    try:
        pdf_item = PDFFile.objects.get(pk=pk)
    except PDFFile.DoesNotExist:
        return Response({'error': 'pdf not found.'}, status=status.HTTP_404_NOT_FOUND)
    
    data = PDFFileSerializer(pdf_item).data
    return Response(data, status=status.HTTP_200_OK)



#endpoint to delete image
@api_view(['DELETE'])
def delete_image(request, pk):
    try:
        image_item = ImageFile.objects.get(pk=pk)
    except ImageFile.DoesNotExist:
        return Response({'error': 'image not found.'}, status=status.HTTP_404_NOT_FOUND)
    
    image_item.delete()
    return Response({'message': 'image deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)



#endpoint to delete pdf
@api_view(['DELETE'])
def delete_pdf(request, pk):
    try:
        pdf_item = PDFFile.objects.get(pk=pk)
    except PDFFile.DoesNotExist:
        return Response({'error': 'pdf not found.'}, status=status.HTTP_404_NOT_FOUND)
    
    pdf_item.delete()
    return Response({'message': 'pdf deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)