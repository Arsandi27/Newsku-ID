from django.db import models
from django.urls import reverse


class Category (models.Model):
    name = models.CharField(max_length=200)
    category_image = models.ImageField(upload_to='imgs/')

    class Meta:
         verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class News(models.Model):
     category = models.ForeignKey(Category,on_delete=models.CASCADE)
     title = models.CharField(max_length=300)
     image = models.ImageField(upload_to='imgs/',null=True)
     detail = models.TextField()
     add_time = models.DateTimeField(auto_now_add=True)
    
     def get_absolute_url(self):
        return reverse('detail_news', args=[str(self.id)])
     
     def get_related_news(self):
        return News.objects.filter(category=self.category).exclude(id=self.id)[:3]

     class Meta:
         verbose_name_plural = 'news'


     def __str__(self):
        return self.title
     
from django.contrib.auth.models import AbstractUser
from django.db import models




        

