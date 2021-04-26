from .models import Post
def get_posts(request):
    posts = Post.objects.all()
    return {'posts': posts}
