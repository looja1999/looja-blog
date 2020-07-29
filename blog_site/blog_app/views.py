from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import (  TemplateView, ListView, DetailView
                                    , CreateView, UpdateView, DeleteView
)
from django.contrib.auth import login,logout,authenticate
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect

from blog_app.models import Post,Comment
from blog_app.forms import PostForm, CommentForm
# Create your views here.

#About view 
class AboutView(TemplateView):
    template_name = 'about.html'

#Post list view - 
class PostListView(ListView):
    model = Post
    
    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

#Detail View
class PostDetailView(DetailView):
    model = Post

#Create view 
class PostCreateView(CreateView, LoginRequiredMixin):
    model = Post
    login_url = '/login/'
    redirect_field_name = 'blog_app/post_detail.html'

    form_class = PostForm

#Upgrade view 
class PostUpdateView(UpdateView, LoginRequiredMixin):
    model = Post
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'

    form_class = PostForm

#Delete view 
class PostDeleteView(DeleteView, LoginRequiredMixin):
    model = Post
    success_url = reverse_lazy('post_list')

#Draft List 
class DraftListView(ListView, LoginRequiredMixin):
    model = Post
    def get_queryset(self):
        return Post.objects.filter( published_date__isnull=True).order_by('created_date')

#Add comment to post
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else: 
        form = CommentForm()
    return render(request, 'blog_app/comment_form.html', {
        'form':form
    })

#Approve comment
@login_required
def approve_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect( 'post_detail', pk=comment.post.pk)

#Remove Comment
@login_required
def remove_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect( 'post_detail', pk=post_pk )

#Post Publish
@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=post.pk)

#Login in
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('post_list'))
        else: 
            return HttpResponse("User is invalid")
    else: 
        return render( request, 'registration/login.html' )

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('post_list'))
