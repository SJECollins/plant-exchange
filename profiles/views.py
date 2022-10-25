from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView
from .models import Profile


class ProfileView(View):
    def get(self, request, user_id):
        profiles = Profile.objects.all()
        profile = get_object_or_404(profiles, user=user_id)
        template_name = 'profiles/profile.html'
        context = {'profile': profile}
        return render(request, template_name, context)


class ProfileCreate(CreateView):
    model = Profile
    fields = ['name', 'location', 'about_me', 'interested_in']
    template_name = 'profiles/update_profile.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProfileUpdate(UpdateView):
    model = Profile
    fields = ['name', 'location', 'about_me', 'interested_in']
    template_name = 'profiles/update_profile.html'
