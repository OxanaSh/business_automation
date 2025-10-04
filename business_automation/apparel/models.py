import datetime
import random

from django.db import models



class TypeOfApparel(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}/'

class ColourOfApparel(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}/'

class SizeOfApparel(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}/'

class Warehouse(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}/'


class Pack(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    date_sold = models.DateTimeField(null=True, blank=True)
    barcode = models.CharField(max_length=255, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        ordering = ('-date_added',)




class Apparel(models.Model):
    type = models.ForeignKey(TypeOfApparel, related_name='types', on_delete=models.CASCADE)
    code_name = models.CharField(max_length=255)
    #slug = models.SlugField()
    colour = models.ForeignKey(ColourOfApparel, related_name='colours', on_delete=models.CASCADE)
    size = models.ForeignKey(SizeOfApparel, related_name='sizes', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    date_added = models.DateTimeField(auto_now_add=True)
    date_sold = models.DateTimeField(null=True, blank=True)
    warehouse = models.ForeignKey(Warehouse, related_name='warehouses', on_delete=models.CASCADE)
    barcode = models.CharField(max_length=255, null=True, blank=True)
    brand = models.CharField(max_length=255, null=True, blank=True)
    pack = models.ForeignKey(Pack, related_name='apparels', null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-date_added',)

    def __str__(self):
        return self.code_name



