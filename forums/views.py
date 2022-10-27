from django.shortcuts import render
from django.core.paginator import Paginator
from django.views import View, generic

from .models import Forum, Discussion, Post

class ForumList(generic.ListView):
    model = Forum
    queryset = Forum.objects.get()
    template_name = 'forums/forum_list.html'
    

class ForumView(generic.ListView):
    def get(self, request, forum_id, *args, **kwargs):
        forum = get_object_or_404(Forum, id=forum_id)
        discussions = forum.discussions.all().annotate(latest_reply=Max('posts__created_on')).order_by('-latest_reply')
        paginator = Paginator(discussion, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        template_name = 'forums/forum.html'
        context = {
            'forum': forum,
            'page_obj': page_obj,
        }

        return render(request, template_name, context)
