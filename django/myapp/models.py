from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    mobile = models.PositiveIntegerField()
    remarks = models.TextField()

    def __str__(self):
        return self.name
    
class Users(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    email = models.EmailField()
    mobile = models.PositiveIntegerField()
    address = models.TextField()
    password = models.CharField(max_length=20)
    profile_picture = models.ImageField(upload_to="profile_picture/")

    def __str__(self):
        return self.fname+" "+self.lname