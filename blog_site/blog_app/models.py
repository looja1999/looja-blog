from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.
#Post model 
class Post(models.Model):
    author = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now())
    published_date = models.DateTimeField(blank=True, null=True)

    #Publish post
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    #Approve Comment
    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

    #Absolute urL
    def get_absolute_url(self):
        return reverse('post_detail', kwargs={ 'pk':self.pk })
    
    #Return string
    def __str__(self):
        return self.title

#Comment model
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=100)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now())
    approved_comment = models.BooleanField(default=False)

    #Approve Comment
    def approve(self):
        self.approved_comment = True
        self.save()
    
    #Absolute_url
    def get_absolute_url(self):
        return reverse('post_list')

    #Return string
    def __str__(self):
        return self.text

#Approve comments

