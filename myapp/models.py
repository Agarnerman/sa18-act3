from django.db import models
from django.core.validators import MinValueValidator

class Product(models.Model):
  name = models.CharField(max_length=255)
  price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
  description = models.TextField()
