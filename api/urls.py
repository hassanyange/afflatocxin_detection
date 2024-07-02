from django.urls import path
from .views import TestDataView


urlpatterns = [

    path('test-data/', TestDataView.as_view(), name='test-data')
]