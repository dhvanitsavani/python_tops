from django.db import models

class User(models.Model):
    usertype = (
        ("buyer", "buyer"),
        ("seller", "seller")
    )
    fname = models.CharField(max_length=30, blank=False)
    lname = models.CharField(max_length=30, blank=False)
    email = models.EmailField(blank=False)
    mobile = models.PositiveIntegerField(blank=False)
    profile_picture = models.ImageField(upload_to='profile_picture/', blank=False)
    password = models.CharField(max_length=30, blank=False)
    user_type = models.CharField(max_length=30, blank=False, choices=usertype)

    def __str__(self):
        return self.fname+" "+self.lname
    
class Product(models.Model):
    category = (
        ('gearless', 'gearless'),
        ('3_gears', '3_gears'),
        ('6_gears', '6_gears')
    )
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    product_category = models.CharField(max_length=30, choices=category)
    product_name = models.CharField(max_length=30)
    product_price = models.PositiveIntegerField()
    product_image = models.ImageField(upload_to='product_image/')
    product_desc = models.TextField()

    def __str__(self):
        return self.seller.fname+" - "+self.product_name