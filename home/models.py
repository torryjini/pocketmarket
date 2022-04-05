from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=32)
    price = models.PositiveIntegerField()
    image = models.ImageField(
        upload_to="post/images/%Y/%m/%d/%H/",
        null=True
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return  f"title: {self.title}"