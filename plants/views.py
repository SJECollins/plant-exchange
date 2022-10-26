from django.shortcuts import render, get_object_or_404, reverse
from django.views import View, generic
from django.views.generic.edit import CreateView, UpdateView

from .models import Plant, Comment
from .forms import CommentForm


class IndexView(View):
    def get(self, request):
        template_name = 'plants/index.html'
        return render(request, template_name)


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