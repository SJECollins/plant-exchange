import cloudinary.uploader

from django.shortcuts import render, get_object_or_404, reverse
from django.views import View, generic
from django.views.generic.edit import CreateView, UpdateView

from plantblog.models import BlogPost
from forums.models import Discussion, Post
from .models import Plant, Comment
from .forms import CommentForm


class IndexView(View):
    def get(self, request):
        blog_post = BlogPost.objects.latest()
        discussion = Discussion.objects.latest()
        post = Post.objects.latest()
        ad = Plant.objects.latest()
        template_name = 'plants/index.html'
        context = {
            'blog_post': blog_post,
            'discussion': discussion,
            'post': post,
            'ad': ad,
        }
        return render(request, template_name, context)


class PlantList(generic.ListView):
    model = Plant
    queryset = Plant.objects.all().order_by('-status', '-added_on')
    template_name = 'plants/exchange.html'
    paginate_by = 10


class AddPlant(CreateView):
    model = Plant
    fields = ['title', 'category', 'description', 'will_trade_for', 'image',]
    template_name = 'plants/add_plant.html'
    success_url = '/exchange/'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('plants:plant_detail', args=(self.object.id,))


class PlantUpdate(UpdateView):
    model = Plant
    fields = ['title', 'category', 'description', 'will_trade_for', 'image', 'status',]
    template_name = 'plants/edit_plant.html'

    def get_success_url(self):
        return reverse('plants:plant_detail', args=(self.object.id,))


class PlantDetail(View):
    def get(self, request, plant_id, *args, **kwargs):
        plant = get_object_or_404(Plant, id=plant_id)
        comments = plant.comments.all()
        template_name = 'plants/plant_detail.html'
        context = {
            'plant': plant,
            'comments': comments,
            'comment_form': CommentForm(),
        }

        return render(request, template_name, context)

    def post(self, request, plant_id, *args, **kwargs):
        plant = get_object_or_404(Plant, id=plant_id)
        comments = plant.comments.all()
        template_name = 'plants/plant_detail.html'
        context = {
            'plant': plant,
            'comments': comments,
            'comment_form': CommentForm(),
        }

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.name = request.user
            comment_form = comment_form.save(commit=False)
            comment_form.ad = plant
            comment_form.save()
        else:
            comment_form = CommentForm()

        return render(request, template_name, context)