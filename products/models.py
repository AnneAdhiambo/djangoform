from django.db import models

# Create your models here.
class Product (models.Model):
    prod_name = models.CharField(max_length=100)
    prod_price =models.IntegerField()
    prod_img = models.ImageField(upload_to="products/")
    prod_category = models.CharField(max_length= 50)
    prod_qty =models.IntegerField()
    prod_desc = models.TextField()