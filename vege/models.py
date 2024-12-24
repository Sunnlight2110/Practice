from django.db import models

class Recipe (models.Model):
   recipe_name = models.CharField(max_length=20)
   recipe_description = models.TextField()
   recipe_image = models.ImageField(upload_to='recipe_photos', height_field=None, width_field=None, max_length=None)
   
   def __str__(self):
      return self
