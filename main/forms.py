from django import forms
from .models import Crop, Test

class CropForm(forms.ModelForm):
    class Meta:
        model = Crop
        fields = ['name']

class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ['crop', 'sample_id', 'gps_location', 'aflatoxin_level', 'sample_photo']
