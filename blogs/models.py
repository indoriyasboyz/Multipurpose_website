from django.db import models

# Create your models here.


class Blogtags(models.Model):
    Title = models.CharField(max_length=50)

    def __str__(self):
        return self.Title


class Blogs(models.Model):
    Title = models.CharField(max_length=30)
    Date = models.DateField(auto_now_add=True)
    S_Description = models.TextField()
    L_Description = models.TextField()
    Tags = models.ForeignKey(Blogtags, on_delete=models.PROTECT, default=1)
    Author = models.CharField(max_length=50)
    Image = models.ImageField(upload_to='pics')

    def __str__(self):
        return self.Title



