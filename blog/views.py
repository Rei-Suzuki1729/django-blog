from django.core.exceptions import PermissionDenied
from django.views.generic import ListView,DetailView
from blog.models import Post

class PostList(ListView):
  model = Post
  template_name="blog/index.html" #追記
  context_object_name="posts" #追記

class PostDetail(DetailView):
  model=Post
  context_object_name="post"

  def get_object(self):
    post = super().get_object()
    if post.ispublished or self.requesr.user.is_authenticated:
      return post
    else:
      raise PermissionDenied


