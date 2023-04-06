from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Community(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_communities')
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='community_images', null=True, blank=True)
    followers = models.ManyToManyField(User, related_name='followed_communities', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Communities'

    def get_absolute_url(self):
        return reverse('questions:community_detail', kwargs={'slug': self.slug})


class Group(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_groups')
    description = models.TextField(null=True, blank=True)
    group_icon = models.ImageField(upload_to='group/profile_images', null=True, blank=True)
    cover_image = models.ImageField(upload_to='group/cover_images', null=True, blank=True)
    members = models.ManyToManyField(User, related_name='joined_groups', blank=True)
    community = models.ForeignKey(Community, on_delete=models.CASCADE, null=True, blank=True, related_name='groups')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    class Meta:
        ordering = ('-created_at',)

    def get_absolute_url(self):
        return reverse('questions:group_detail', kwargs={'slug': self.slug})

class Question(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField()
    category = models.ForeignKey('core.Category', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='questions')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, blank=True, related_name='questions')
    community = models.ForeignKey(Community, on_delete=models.CASCADE, null=True, blank=True, related_name='questions')
    tags = models.ManyToManyField('core.Tag', related_name='questions', blank=True)
    # likes = models.ManyToManyField(User, related_name='liked_questions', through='QuestionLike')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
            return self.title
    class Meta:
        ordering = ('-created_at',)

class Answer(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answers')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
            return f"Reply to {self.question.user.username}'s question"
    class Meta:
        ordering = ('-created_at',)

# class QuestionLike(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)

