from django.db import models
from django.urls import reverse
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    description = models.TextField()
    category = models.ForeignKey('core.Category', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='resource/articles/', null=True, blank=True)
    tags = models.ManyToManyField('core.Tag', blank=True)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)
        verbose_name_plural = 'Resource Articles'

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('resources:article_details', kwargs={'slug': self.slug})
class Video(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    category = models.ForeignKey('core.Category', on_delete=models.CASCADE)
    video = models.URLField()
    tags = models.ManyToManyField('core.Tag', blank=True)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)
        verbose_name_plural = 'Resource Videos'

    def __str__(self):
        return self.title
    
    def get_video_key(self):
        key = self.video.split('/')[-1]
        return f"https://www.youtube.com/embed/{key}"
    
class Document(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    category = models.ForeignKey('core.Category', on_delete=models.CASCADE)
    cover_image = models.ImageField(upload_to='resource/documents/images/')
    document = models.FileField(upload_to='resource/documents/')
    tags = models.ManyToManyField('core.Tag', blank=True)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)
        verbose_name_plural = 'Resource Documents'

    def __str__(self):
        return self.title
    