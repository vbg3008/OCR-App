from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import ImageUploadForm
from .models import ExtractedText
from PIL import Image
import pytesseract
import cv2
import base64
import io


def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = request.FILES['image']
            img = Image.open(image)
            text = pytesseract.image_to_string(img)

            # Save extracted text to the database
            extracted_text = ExtractedText(image_name=image.name, text=text)
            extracted_text.save()

            return render(request, 'result.html', {'text': text})
    else:
        form = ImageUploadForm()
    
    return render(request, 'upload.html', {'form': form})

@csrf_exempt
def capture_image(request):
    if request.method == 'POST':
        image_data = request.POST.get('image')

        if image_data:
            # Decode the base64 image data
            image_data = image_data.split(',')[1]
            image = base64.b64decode(image_data)

            # Convert the binary image data to a PIL image
            img = Image.open(io.BytesIO(image))
            
            # Process the image with Tesseract OCR
            text = pytesseract.image_to_string(img)

            # Save the extracted text to the database
            extracted_text = ExtractedText(image_name="webcam_capture", text=text)
            extracted_text.save()

            return render(request, 'result.html', {'text': text})

    return render(request, 'capture.html')