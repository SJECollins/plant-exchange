import cloudinary.uploader
from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from django.views import View, generic
from django.views.generic.edit import CreateView, UpdateView
from django.db.models import Q
from plants.models import Plant
from .models import Profile, Message
from .forms import MessageForm


class ProfileView(View):
    def get(self, request, user_id):
        profile = get_object_or_404(Profile, user=user_id)
        plants = Plant.objects.filter(owner=user_id).order_by('-added_on')
        template_name = 'profiles/profile.html'
        context = {
            'profile': profile,
            'plants': plants,
            }
        return render(request, template_name, context)


class ProfileUpdate(UpdateView):
    model = Profile
    fields = ['name', 'location', 'about_me', 'interested_in']
    template_name = 'profiles/update_profile.html'


class MailboxList(generic.ListView):
    model = Message
    context_object_name = 'messages'
    template_name = 'profiles/mailbox.html'
    paginate_by = 20

    def get_queryset(self):
        return Message.objects.filter(Q(sender=self.request.user) | Q(receiver=self.request.user))


class MessageCreate(CreateView):
    model = Message
    fields = ['content',]
    template_name = 'profiles/new_message.html'
    success_url = '/exchange/'

    def get_context_data(self, **kwargs):
        context = super(MessageCreate, self).get_context_data(**kwargs)
        context['plant_id'] = self.kwargs['plant_id']
        return context

    def form_valid(self, form):
        form.instance.sender = self.request.user
        form.instance.ad = Plant.objects.get(id=self.kwargs['plant_id'])
        form.instance.receiver = form.instance.ad.owner
        context = {
            'plant_id': self.kwargs['plant_id']
        }
        return super(MessageCreate, self).form_valid(form)


class MessageView(View):
    def get(self, request, msg_id, *args, **kwargs):
        message = get_object_or_404(Message, id=msg_id)
        user = self.request.user
        if message.receiver == user:
            message.read = True
            message.save()
        template_name = 'profiles/message.html'
        context = {
            'message': message,
            'message_form': MessageForm(),
        }

        return render(request, template_name, context)

    def post(self, request, msg_id, *args, **kwargs):
        message = get_object_or_404(Message, id=msg_id)
        if message.replied == False:
            message.replied = True
            message.save()
        template_name = 'profiles/message.html'
        context = {
            'message': message,
            'message_form': MessageForm(),
        }
        message_form = MessageForm(data=request.POST)

        if message_form.is_valid():
            message_form.instance.sender = request.user
            message_form = message_form.save(commit=False)
            message_form.ad = message.ad
            message_form.receiver = message.sender
            message_form.save()
            return HttpResponseRedirect('/profiles/mailbox/')

        return render(request, template_name, context)
