from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=50)
    writer = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    weather = models.CharField(max_length=30, default='')
    body = models.TextField()
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to = "post/", blank=True, null=True)
    tags = models.ManyToManyField(Tag, related_name='posts', blank=True)
    like = models.ManyToManyField(User, related_name='likes', blank=True)
    like_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:20]
    
class Comment(models.Model):
    content = models.TextField()
    pub_date = models.DateTimeField()
    writer = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, null=False, blank=False, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, related_name='comments', blank=True)

    def __str__(self):
        return self.post.title + " : " + self.content[:20] + " by " + self.writer.profile.nickname