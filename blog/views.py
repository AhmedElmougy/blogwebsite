from django.shortcuts import render
from django.views.generic import ListView,TemplateView,DetailView,DeleteView,UpdateView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404,redirect
from django.utils import timezone
from django.http import HttpResponseRedirect
from blog.forms import PostForm,CommentForm
from blog.models import Post,Comment


class IndexView(TemplateView):
    template_name = "index.html"

class aboutView(TemplateView):
    template_name = "about.html"    

class PostListView(ListView):
    model = Post
    template_name = "post_list.html"
    
    def get_queryset(self):
        return Post.objects.filter(published_at__lte=timezone.now()).order_by('-published_at')
    
class DraftListView(LoginRequiredMixin,ListView):
    login_url = '/accounts/login/'
    model = Post
    template_name = "draft_list.html"

    def get_queryset(self):
        return Post.objects.filter(published_at__isnull=True).order_by('created_at')

class PostCreateView(LoginRequiredMixin,CreateView):
    login_url = '/accounts/login/'
    model      = Post
    form_class = PostForm

    template_name = "post_form.html"

    def form_valid(self, form):
        form.instance.auther = self.request.user
        
        return super().form_valid(form)   

class PostUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/accounts/login/'
    model      = Post
    form_class = PostForm

    template_name = "post_form.html"    

class PostDeleteView(LoginRequiredMixin,DeleteView):
    login_url = '/accounts/login/'
    model      = Post
    success_url = reverse_lazy("blog:posts")
    template_name = "post_delete.html"

class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"


@login_required(login_url="/accounts/login/")
def post_publish(request,pk):
    post=get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect('blog:post_detail',pk=pk)

class CommentCreateView(LoginRequiredMixin,CreateView):
    login_url = '/accounts/login/'
    model      = Comment
    form_class = CommentForm

    template_name = "comment_form.html"

    def form_valid(self, form):
        form.instance.auther = self.request.user
        form.instance.post   = get_object_or_404(Post,pk=self.kwargs['post']) 
        return super().form_valid(form)


class CommentUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/accounts/login/'
    model      = Comment
    form_class = CommentForm

    template_name = "comment_form.html"    

class CommentDeleteView(LoginRequiredMixin,DeleteView):
    login_url = '/accounts/login/'
    model      = Comment
    template_name = "comment_delete.html"

    def get_success_url(self):
        comment_id = self.kwargs['pk']
        comment    = get_object_or_404(Comment,pk=comment_id)
        return reverse_lazy("blog:post_detail", kwargs={'pk': comment.post.pk})