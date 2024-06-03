from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.
class Category(models.Model):
    name = models.CharField(null=True, max_length=50,validators=[MinValueValidator(1),MaxValueValidator(50)])
    active = models.BooleanField(default=False)
    