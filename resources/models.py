from django.db import models

# Create your models here.
class ResouceArticle(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey('core.Category', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='resource/articles/', null=True, blank=True)
    