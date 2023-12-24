from django.db import models
from django.contrib.auth import get_user_model

class Instructor(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='instuctor')
    bio = models.TextField()
    website = models.URLField(blank=True)
    specialisation = models.TextField()