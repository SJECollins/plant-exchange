from django.shortcuts import render, get_object_or_404
from django.views import View, generic
from django.views.generic.edit import CreateView, UpdateView
from plants.models import Plant
from .models import Profile, Message
from .forms import MessageForm


class ProfileView(View):
    def get(self, request, user_id):
        profile = get_object_or_404(Profile, user=user_id)
        template_name = 'profiles/profile.html'
        context = {'profile': profile}
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
        return Message.objects.filter(owner=self.request.user)


class MessageCreate(CreateView):
    model = Message
    fields = ['content',]
    template_name = 'profiles/new_message.html'
    success_url = '/exchange/'

    def form_valid(self, form):
        try:
            ad = Plant.objects.get(id=self.kwargs['plant_id'])
        except Plant.DoesNotExist:
            pass
        form.instance.ad = ad
        form.instance.receiver = ad.owner
        form.instance.sender = self.request.user
        return super().form_valid(form)


class MessageView(View):
    def get(self, request, msg_id, *args, **kwargs):
        queryset = Plant.objects.filter(id=msg_id.ad)
        message = get_object_or_404(Message, id=msg_id)
        template_name = 'profiles/message.html'
        context = {
            'message': message,
            'message_form': MessageForm(),
        }

    def post(self, request, msg_id, *args, **kwargs):
        queryset = Plant.objects.filter(id=msg_id.ad)
        message = get_object_or_404(Message, id=msg_id)
        template_name = 'profiles/message.html'
        context = {
            'message': message,
            'message_form': MessageForm(),
        }
        success_url = '/profiles/profile/'
        message_form = MessageForm(data=request.POST)

        if message_form.is_valid():
            message_form.instance.sender = request.user
            message_form = message_form.save(commit=False)
            message_form.instance.ad = message.ad
            message_form.instance.receiver = message.receiver
            commit.save()

        return render(request, template_name, context)


