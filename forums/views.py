from django.shortcuts import render, get_object_or_404, reverse
from django.core.paginator import Paginator
from django.views import View, generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db.models import Max

from .models import Forum, Discussion, Post
from .forms import PostForm

class ForumList(generic.ListView):
    model = Forum
    queryset = Forum.objects.all()
    template_name = 'forums/forum_list.html'
    

class ForumView(generic.ListView):
    def get(self, request, forum_id, *args, **kwargs):
        forum = get_object_or_404(Forum, id=forum_id)
        discussions = forum.discussions.all().annotate(latest_reply=Max('posts__created_on')).order_by('-latest_reply')
        paginator = Paginator(discussions, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        template_name = 'forums/forum.html'
        context = {
            'forum': forum,
            'page_obj': page_obj,
        }

        return render(request, template_name, context)


class TopicCreate(CreateView):
    model = Discussion
    fields = ['title', 'description', 'image', ]
    template_name = 'forums/new_thread.html'
    success_url = '/forums/'

    def get_context_data(self, **kwargs):
        context = super(TopicCreate, self).get_context_data(**kwargs)
        context['forum_id'] = self.kwargs['forum_id']
        return context

    def form_valid(self, form):
        form.instance.creator = self.request.user
        form.instance.forum = Forum.objects.get(id=self.kwargs['forum_id'])
        context = {'forum_id': self.kwargs['forum_id']}
        return super(TopicCreate, self).form_valid(form)


class TopicEdit(UpdateView):
    model = Discussion
    fields = ['title', 'description', 'image',]
    
    def get_success_url(self):
        topic_id = self.kwargs['topic_id']
        return reverse('/forums/view_topic/', kwargs={'topic_id': topic_id})


class TopicDelete(DeleteView):
    model = Discussion

    def get_success_url(self):
        topic_id = self.kwargs['topic_id']
        topic = get_object_or_404(Discussion, topic_id)
        return reverse('/forums/forum/', kwargs={'forum_id': topic.forum.id})


class TopicView(View):
    def get(self, request, topic_id, *args, **kwargs):
        discussion = get_object_or_404(Discussion, id=topic_id)
        posts = discussion.posts.all()
        template_name = 'forums/thread.html'
        context = {
            'discussion': discussion,
            'posts': posts,
            'reply_form': PostForm(),
        }

        post_form = PostForm(data=request.POST)

        if post_form.is_valid():
            post_form.instance.creator = request.user
            post_form = post_form.save(commit=False)
            post_form.discussion = discussion
            post_form.save()
        else:
            post_form = PostForm()

        return render(request, template_name, context)

