from django.db import models

# Create your models here.


class Product(models.Model):
    CATEGORY_CHOICES=[
        ("mobile","Mobile"),
        ('clothing','Clothing'),
        ('electronics','Electronics')
    ]
    title = models.CharField(max_length=250, unique=True)
    model = models.CharField(max_length=250, unique=True)
    description = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=4)
    stock = models.IntegerField()
    product_img=models.ImageField(upload_to='product_images/',blank=True,null=True)
    Category=models.CharField(max_length=20,choices=CATEGORY_CHOICES,default='mobile')

    def __str__(self):
        return f"{self.title}"
