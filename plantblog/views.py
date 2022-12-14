from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import BlogPost
from .forms import CommentForm


class PostList(generic.ListView):
    model = BlogPost
    queryset = BlogPost.objects.filter(status=1).order_by('-created_on')
    template_name = 'plantblog/post_list.html'
    paginate_by = 5


class PostDetail(View):

    def get(self, request, post_id, *args, **kwargs):
        queryset = BlogPost.objects.filter(status=1)
        post = get_object_or_404(queryset, id=post_id)
        comments = post.comments.all().order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        template_name = 'plantblog/post_detail.html'
        context = {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm(),            
        }

        return render(request, template_name, context)

    def post(self, request, post_id, *args, **kwargs):
        queryset = BlogPost.objects.filter(status=1)
        post = get_object_or_404(queryset, id=post_id)
        comments = post.comments.all().order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        template_name = 'plantblog/post_detail.html'
        context = {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm(),            
        }

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.author = request.user.profile.name
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(request, template_name, context)


class PostLike(View):

    def post(self, request, post_id):
        post = get_object_or_404(BlogPost, id=post_id)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('plantblog:post', args=[post_id]))