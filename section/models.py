from django.db import models

# Create your models here.
class Section (models.Model) :
    id = models.BigAutoField
    name=models.CharField(null=True,max_length=225)
    active=models.BooleanField(default=False)
    slug=models.SlugField(default="",blank=True)
    category = models.ForeignKey("category", verbose_name=("category"), on_delete=models.CASCADE, related_name="models")