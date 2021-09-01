from django.db import models

# Create your models here.
class BlogPost(models.Model):
    post_title = models.CharField(max_length=300)
    publishing_date = models.DateTimeField(auto_now_add=True)
    post_text = models.TextField()
    post_image = models.ImageField(upload_to='blog_images/')