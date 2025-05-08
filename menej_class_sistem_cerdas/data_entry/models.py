from django.db import models
from django import forms
from datetime import date


# Create your models here.
class Pengguna (models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    address_1 = models.TextField()
    address_2  = models.TextField(null=True, blank = True)
    city = models.CharField(max_length=20, help_text='Enter your city')
    state= models.TextField()
    zip_code= models.CharField(max_length = 7)
    tanggal_join = models.DateField(auto_now = True)
    foto = models.ImageField(upload_to='foto/', null=True, blank=True)

    class Meta:
        verbose_name = 'pengguna'

    def __str__(self):
        return self.email

class Content (models.Model):
    author = models.ForeignKey(Pengguna, on_delete=models.CASCADE, verbose_name='Author')
    date_created = models.DateField(auto_now=True)
    artikel = models.TextField(verbose_name='Artikel')
    set_view = models.BooleanField(default=False, verbose_name='Set View')



