from django.conf.urls import url 
from blog_app import views 

urlpatterns =[
    url(r'^$', views.PostListView.as_view(),name='post_list'),
    url(r'^about/', views.AboutView.as_view(), name='about'),
    
    url(r'^(?P<pk>\d+)/$', views.PostDetailView.as_view(), name='post_detail'),
    url(r'^post/create/$', views.PostCreateView.as_view(), name='post_create'),
    url(r'^post/(?P<pk>\d+)/update/$', views.PostUpdateView.as_view(), name='post_update'),
    url(r'^post/(?P<pk>\d+)/delete/$', views.PostDeleteView.as_view(), name='post_delete'),
    url(r'^post/draft/$', views.DraftListView.as_view(), name='post_draft_list'),
    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    
    url(r'^comment/(?P<pk>\d+)/approve/$', views.approve_comment, name='approve_comment'),
    url(r'^comment/(?P<pk>\d+)/delete/$', views.remove_comment, name='remove_comment')  
]