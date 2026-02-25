from django.db import models

# Create your models here.

class Banner(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='banner_images/')
    discount = models.IntegerField(default=1)
    info = models.CharField(max_length=255)
    status = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Banners'
        verbose_name = 'Banner'

class Categories(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Categories"
        verbose_name = "Category"

class Tags(models.Model):
    title = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Tags"
        verbose_name = "Tag"


class Blogs(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='blogs/')
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

