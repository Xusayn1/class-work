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

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'product'
        verbose_name_plural = 'Products'
        verbose_name = 'Product'

    def __str__(self):
        return f'  | {self.title}'

class Author(models.Model):
    full_name = models.CharField(max_length=128)
    image = models.ImageField(upload_to='authors/')
    about = models.CharField(max_length=255)
    professions = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.full_name

    class Meta:
        db_table = 'authors'
        verbose_name = 'author'
        verbose_name_plural = 'authors'
