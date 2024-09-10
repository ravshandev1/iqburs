from django.db import models
from main.validators import custom_file_path, img_validator


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, models.CASCADE, 'products')
    image = models.ImageField(upload_to=custom_file_path, validators=[img_validator])
    sum_one_product = models.CharField(max_length=100)
    sum_five_product = models.CharField(max_length=100)
    iso_number = models.CharField(max_length=100)
    size_image = models.ImageField(upload_to=custom_file_path, validators=[img_validator])
    stock = models.BooleanField(default=False)
    size = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Info(models.Model):
    product = models.ForeignKey(Product, models.CASCADE, 'infos')
    key = models.CharField(max_length=100)
    value = models.CharField(max_length=100)

    def __str__(self):
        return self.key


class Thanks(models.Model):
    product = models.ForeignKey(Product, models.CASCADE, 'thanks')
    text = models.TextField()

    def __str__(self):
        return self.text
