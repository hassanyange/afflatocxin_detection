from rest_framework import serializers
from main.models import Test
import base64
from django.core.files.base import ContentFile


class TestSerializer(serializers.ModelSerializer):
    sample_photo = serializers.CharField()
 


    class Meta:
        model = Test
        fields = '__all__'

    
    def create(self, validated_data):
        sample_photo_base64 = validated_data.pop('sample_photo')
        sample_photo = ContentFile(base64.b64decode(sample_photo_base64), name='sample_photo.jpg')
        validated_data['sample_photo'] = sample_photo
        return super().create(validated_data)