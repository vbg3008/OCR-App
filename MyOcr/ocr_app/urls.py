from django.urls import path
from .views import upload_image, capture_image

urlpatterns = [
    path('', upload_image, name='upload_image'),
    path('capture/', capture_image, name='capture_image'),
]
