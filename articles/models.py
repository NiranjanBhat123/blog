from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(upload_to='article_images/',blank=True,null=True)
    video = models.FileField(blank=True,null=True)
    
    
    def __str__(self):
        return str(self.title)
    

    
    
