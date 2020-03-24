from django.db import models

# Create your models here.


class Gallery(models.Model):
    Title = models.CharField(max_length=30)
    Image = models.ImageField(upload_to='pics')

    def __str__(self):
        return self.Title



