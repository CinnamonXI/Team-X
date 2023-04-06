from django.db import models
from django.contrib.auth.models import User

class Community(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
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


class Group(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)
    group_icon = models.ImageField(upload_to='group/profile_images', null=True, blank=True)
    cover_image = models.ImageField(upload_to='group/cover_images', null=True, blank=True)
    members = models.ManyToManyField(User, related_name='joined_groups', blank=True)
    community = models.ForeignKey(Community, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    class Meta:
        ordering = ('-created_at',)

class Question(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField()
    category = models.ForeignKey('core.Category', on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, blank=True)
    community = models.ForeignKey(Community, on_delete=models.CASCADE, null=True, blank=True)
    tags = models.ForeignKey('core.Tag', on_delete=models.CASCADE, null=True, blank=True)
    # likes = models.ManyToManyField(User, related_name='liked_questions', through='QuestionLike')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
            return self.title
    class Meta:
        ordering = ('-created_at',)

class Answer(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
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

