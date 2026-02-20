from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        db_table = 'category'
        verbose_name_plural = 'Categories'
        verbose_name = 'Category'

    def __str__(self):
         return f'  {self.title}'

class Product(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='product_images')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    discount = models.FloatField()
    info = models.TextField()

    class Meta:
        db_table = 'product'
        verbose_name_plural = 'Products'
        verbose_name = 'Product'

    def __str__(self):
        return f'  | {self.title}'