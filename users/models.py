from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse

# Create your models here.

GENDER_CHOICES = (
    ('male', 'male'),
    ('female', 'female'),
    ('other', 'other')
)

class Follower(models.Model):
    user_from = models.ForeignKey('auth.User',related_name='rel_from_set', on_delete=models.CASCADE)
    user_to = models.ForeignKey('auth.User', related_name='rel_to_set', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    class Meta:
        ordering = ('-created_at',)
    def __str__(self):
        return f'{self.user_from} follows {self.user_to}'

LANGUAGE_CHOICES = (
    #languages in Kenya and nigeria
    ('English', 'English'),
    ('Kiswahili', 'Kiswahili'),
    ('Yoruba', 'Yoruba'),
    ('Igbo', 'Igbo'),
)   
class Profile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name='profile')
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='other')
    age = models.PositiveSmallIntegerField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    language_preference = models.CharField(max_length=100, choices=LANGUAGE_CHOICES, default='English')
    followers = models.ManyToManyField(Follower, blank=True)
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
        return reverse('users:user_profile', kwargs={'username': self.user.username})
    

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

# Model for collecting users health data and interests
class HealthData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='health_data')
    height = models.DecimalField(max_digits=5, decimal_places=2,help_text="Height in Centimeters (e.g. 175.2)")
    weight = models.DecimalField(max_digits=5, decimal_places=2,help_text="Weight in kilograms (e.g. 70.5)")
    systolic_bp = models.PositiveIntegerField(help_text="Systolic blood pressure in mmHg (e.g. 120)")
    diastolic_bp = models.PositiveIntegerField(help_text="Diastolic blood pressure in mmHg (e.g. 80)")
    heart_rate = models.PositiveIntegerField(help_text="Heart rate in beats per minute (e.g. 70)")
    status = models.CharField(max_length=200,blank=True,null=True,help_text="Current health status (e.g. diabetes, asthma, etc.)")
    allergies = models.CharField(max_length=200,blank=True,null=True,help_text="Known allergies (e.g. pollen, dust, etc.)")
    interests = models.CharField(max_length=100,blank=True,null=True,help_text="Interests and hobbies (e.g. sports, music, etc.)")
    take_alcohol = models.BooleanField(default=False)
    smoke = models.BooleanField(default=False)
    is_disabled = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance,)