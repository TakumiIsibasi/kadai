from django.db import models
from user.models import CustomUser

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='post_images/')  # 画像のアップロード先を 'post_images/' に修正
    description = models.CharField(max_length=255, blank=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
