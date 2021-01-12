from django.conf.urls import url
from django.urls import path
from blog import views
app_name = 'blog'

urlpatterns = [
    path('posts/',views.PostListView.as_view(),name='posts'),
    path('drafts/',views.DraftListView.as_view(),name='drafts'),
    path('new_post/',views.PostCreateView.as_view(),name='new_post'),
    path('post/<int:pk>/',views.PostDetailView.as_view(),name='post_detail'),
    path('post_edit/<int:pk>/',views.PostUpdateView.as_view(),name='post_edit'),
    path('post_delete/<int:pk>/',views.PostDeleteView.as_view(),name='post_delete'),
    path('post_publish/<int:pk>/',views.post_publish,name='post_publish'),
    path('new_comment/<int:post>/<int:auther>/',views.CommentCreateView.as_view(),name='new_comment'),
    path('comment_edit/<int:pk>/',views.CommentUpdateView.as_view(),name='comment_edit'),
    path('comment_delete/<int:pk>/',views.CommentDeleteView.as_view(),name='comment_delete'),
]
