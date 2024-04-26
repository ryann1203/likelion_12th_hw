from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    writer = models.CharField(max_length=30)
    weather = models.CharField(max_length=30, default='')
    body = models.TextField()
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to = "post/", blank=True, null=True)

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:20]