from django.db import models

# Create your models here.
class UserProduct(models.Model):
    # documentation : https://docs.djangoproject.com/en/2.1/ref/models/fields/

    #product info
    product_title = models.CharField(max_length=100)
    product_description = models.TextField()
    product_price = models.PositiveIntegerField() # from 0-2147483647
    price_negotiable = models.CharField(max_length=50) # No or Yes or little
    product_usage_age = models.CharField(max_length=200) # brand_new or 7 days or 6 months
    product_warranty = models.CharField(max_length=100) # 1 year or 4 months or none

    # Create a directory in project directory (same location of manage.py file)
    product_image = models.FileField(upload_to = 'product_image/', default = 'product_image/no_image.png')

    # seller info
    seller_name = models.CharField(max_length=200)
    seller_location = models.CharField(max_length=200)
    seller_email = models.EmailField(max_length=254)
    seller_phone = models.CharField(max_length=30)
    seller_city = models.CharField(max_length = 100)

    date_published = models.DateTimeField(auto_now=True)
    product_display_last_date = models.DateField(auto_now=False, auto_now_add=False) # date after which this product would not be shown in website.

    def __str__(self):
        return self.product_title