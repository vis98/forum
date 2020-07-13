from django.db import models
from members.models import user
from django.urls import reverse

class Post(models.Model):
    title=models.CharField(max_length=100)
    body=models.TextField(max_length=1000)
    '''slug = models.SlugField(unique=True,null=True)'''
    author=models.ForeignKey(user,on_delete=models.CASCADE)

    def __str__(self):
        return self.title + '|'+ str(self.author)

    '''def save(self, *args, **kwargs):
        self.slug = self.slug or slugify(self.title)
        super().save(*args, **kwargs)'''


    def get_absolute_url(self):
        return reverse("posts:post-details", kwargs={"id": self.id})        