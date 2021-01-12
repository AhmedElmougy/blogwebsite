from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    
    title  = models.CharField(max_length=200)
    img    = models.ImageField(upload_to='post_pics', blank=True)
    body   = models.TextField()
    auther = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    published_at =models.DateField(blank=True,null=True)
    

    def publish(self):
        self.published_at = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse("blog:post_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title

class Comment(models.Model):
    post   = models.ForeignKey("blog.Post",related_name='comments' ,on_delete=models.CASCADE)
    auther = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    text   = models.TextField() 
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.text
    
    def get_absolute_url(self):
        return reverse("blog:post_detail", kwargs={"pk": self.post.id})
