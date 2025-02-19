from django.db import models
import os
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    img = models.ImageField(upload_to='blog_img', null=True, blank=True)
    description = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def delete(self, *args, **kwargs):
        if self.image:  
            if os.path.isfile(self.image.path):  
                os.remove(self.image.path)  
        super().delete(*args, **kwargs)