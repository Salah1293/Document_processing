from rest_framework import serializers
from .models import *


class ImageFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageFile
        fields = ['id', 'image_item', 'name']



class PDFFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PDFFile
        fields = ['id', 'pdf_item','name', 'pages']
 