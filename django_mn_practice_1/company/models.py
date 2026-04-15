from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    department = models.CharField(max_length=20)
    mobile = models.PositiveIntegerField()
    profile_picture = models.ImageField(upload_to='profile_picture/')
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.name