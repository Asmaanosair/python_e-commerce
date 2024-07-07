from typing import Iterable
from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify
from django.core.exceptions import ValidationError



# def validate_name_length(value):
#     if len(value) < 1 or len(value) > 50:
#         raise ValidationError("The name must be between 1 and 50 characters long.")

# Create your models here.
class Category(models.Model):
    id = models.BigAutoField
    name = models.CharField(null=True, max_length=100)
    active = models.BooleanField(default=False)
    slug = models.SlugField(default="", blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
      return reverse("show_category", args=[self.slug])
    def del_absolute_url(self):
      return reverse("del_category", args=[self.id])
    def __str__(self) :
       return f"{self.name}"
    
    


  
    