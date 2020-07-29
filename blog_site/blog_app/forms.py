from django import forms 
from blog_app.models import Post, Comment

#Post form 
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('author','title','text')

#Comment form 
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author','text')

