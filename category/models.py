from typing import Iterable
from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
class Category(models.Model):
    id = models.BigAutoField
    name = models.CharField(null=True, max_length=50,validators=[MinValueValidator(1),MaxValueValidator(50)])
    active = models.BooleanField(default=False)
    slug = models.SlugField(default="", blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("show_category", args=[self.id])

  
    