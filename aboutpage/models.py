from django.db import models

# Create your models here.


class Why_choose_us(models.Model):
    Question = models.CharField(max_length=50)
    Answer = models.TextField()

    def __str__(self):
        return self.Question


class Team(models.Model):
    Name = models.CharField(max_length=30)
    Designation = models.CharField(max_length=20)
    Photo = models.ImageField(upload_to='pics')

    def __str__(self):
        return self.Name