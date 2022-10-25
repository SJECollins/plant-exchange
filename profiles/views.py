from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Profile


class ProfileView(View):
    def get(self, request, user_id):
        user = get_object_or_404(Profile, id=user_id)
        template_name = 'profiles/profile.html'
        context = {'user': user}
        return render(request, template_name, context)

