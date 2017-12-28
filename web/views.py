from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView


class IndexView(TemplateView):
    #TODO: Hookup templates for the website homepage
    pass


class SignInView(View):

    #TODO: first time signin using facebook, and redirects to profile view
    def get(self, request):
        return render(request, 'signin.html')


class ProfileView(View):
    #TODO: update user profile
    pass


class RegisterView(View):
    #TODO: create a new user to handle clients and personnels
    pass


class RequestView(View):
    #TODO: book a cleaning service
    pass


class DashboardView(View):
    #TODO: user services
    pass
