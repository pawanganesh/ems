from django.db import models

# Create your models here.
class Position(models.Model):
    position = models.CharField(max_length=50)

    def __str__(self):
        return self.position

class Employee(models.Model):
    fullname = models.CharField(max_length=50)
    mobile = models.CharField(max_length=20)
    img = models.ImageField(upload_to='img')
    position = models.ForeignKey(Position,on_delete=models.CASCADE)

    def delete(self, *args, **kwargs):
        self.img.delete() #https://matthiasomisore.com/uncategorized/django-delete-file-when-object-is-deleted/
        super().delete(*args, **kwargs)

"""
Allow user to changr profile picture 
https://stackoverflow.com/questions/13565218/allow-user-to-change-its-picture-django/15115988
"""