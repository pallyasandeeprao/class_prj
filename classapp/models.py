from django.db import models
from django.urls import reverse


# Create your models here.
class Product(models.Model):
    p_name=models.CharField(max_length=50)
    p_code=models.CharField(max_length=20, unique=True)
    p_quantity=models.IntegerField()
    p_exp_data=models.DateField()

    def __str__(self):
        return self.p_name
    def get_absolute_url(self):
        return reverse('dis')
