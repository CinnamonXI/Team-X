from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model
# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse

GENDER_CHOICES = (
    ('male', 'male'),
    ('female', 'female'),
    ('other', 'other')
)

class Profile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name='profile')
    slug = models.SlugField(max_length=158, unique=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='other')
    image = models.ImageField(upload_to='users/profiles/', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('users:profile', kwargs={'slug': self.slug})

class Team(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='users/teams/')
    is_active = models.BooleanField(default=True)
    order = models.PositiveSmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('order',)

class Follower(models.Model):
    user_from = models.ForeignKey('auth.User',related_name='rel_from_set', on_delete=models.CASCADE)
    user_to = models.ForeignKey('auth.User', related_name='rel_to_set', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    class Meta:
        ordering = ('-created_at',)
    def __str__(self):
        return f'{self.user_from} follows {self.user_to}'


user_model = get_user_model()
user_model.add_to_class('following',  models.ManyToManyField('self', through=Follower, related_name='followers', symmetrical=False))

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(
            user=instance,
            slug=slugify(instance.username)
            )