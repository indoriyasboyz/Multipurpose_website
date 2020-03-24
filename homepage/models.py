from django.db import models

# Create your models here.


class Slider(models.Model):
    Title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='pics')

    def __str__(self):
        return self.Title


class Services(models.Model):
    Title = models.CharField(max_length=50)
    Description = models.CharField(max_length=50)
    Image = models.ImageField(upload_to='pics')

    def __str__(self):
        return self.Title


class Newscatgory(models.Model):
    Title = models.CharField(max_length=50)

    def __str__(self):
        return self.Title


class News(models.Model):
    Title = models.CharField(max_length=50)
    Description = models.TextField()
    category = models.ForeignKey(Newscatgory, on_delete=models.PROTECT, default=1)
    Date = models.DateField(auto_now_add=True)
    Author = models.CharField(max_length=20)
    Tags = models.CharField(max_length=60)
    Image = models.ImageField(upload_to='pics')

    def __str__(self):
        return self.Title