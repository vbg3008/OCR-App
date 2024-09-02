from django.db import models

class ExtractedText(models.Model):
    image_name = models.CharField(max_length=255)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image_name
