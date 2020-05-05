from django.db import models


# Create your models here.
class Gallery(models.Model):
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title
