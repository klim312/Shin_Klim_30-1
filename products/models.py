from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title


class Products(models.Model):
    img = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=128)
    description = models.TextField(blank=True, null=True)
    rate = models.FloatField()
    category = models.ManyToManyField(Category)
    create_data = models.DateTimeField(auto_now_add=True, null=True)
    modified_data = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.CharField(max_length=255)
    products = models.ForeignKey(Products, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.text}-> {self.products.title}'



