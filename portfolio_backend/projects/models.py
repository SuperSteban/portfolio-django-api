from django.db import models
import os
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    img = models.ImageField(upload_to='project_img', null=True, blank=True)
    description = models.TextField()
    pinned = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def delete(self, *args, **kwargs):
        if self.img:  
            if os.path.isfile(self.img.path):  
                os.remove(self.img.path)  
        super().delete(*args, **kwargs)
    
