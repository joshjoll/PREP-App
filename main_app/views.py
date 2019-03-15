from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.views.generic import ListView, DetailView
from .models import Project, Technology, Review, Image, User

# Create your views here.

# Display Landing Page
def landing(request):
    return render(request, 'landing.html')
# Display Index Page of all projects
class Index(ListView):
    model = Project
    fields = '__all__'

# Display project details. Limit to logged in
class Project_Detail(DetailView):
    model = Project
# Loads new project form page, Limit to logged in
# CBV
class New_Project(CreateView):
    model = Project
# Saves project form, redirects to details page. Limit to logged in
# CBV not needed?
def save_new_project(request):
    return HttpResponse("save_new_project")
# Loads page to update project. Limit to logged in
# CBV
class Update_Project(UpdateView):
    model = Project
# Updates project instance. Limit to logged in
# CBV Not Needed?
def update_project(request):
    return HttpResponse("update_project")


# Loads new review Page. Limit to logged in
# CBV
def add_review(request):
    return HttpResponse("add_review")
# Saves review, redirect to detail page. Limit to logged in
# needed?
def save_review(request):
    return HttpResponse("save_review")
# Loads consolidated review page. Limit to team members
# CBV model template
def consolidated_review(request):
    return HttpResponse("consolidated_review")

# Display User Profile Page. Limit to logged in
class Profile(DetailView):
    model = User
    fields = '__all__'
# Loads sign up page
# CBV
def new_user_form(request):
    return HttpResponse("new_user_form")
# Saves new users, redirects to index page
def save_user(request):
    return HttpResponse("save_user")

# Complicated. Lets users search for their cohort, then select a class member and add them to a project. From owner detail page, redirects to owner detail page. Limit to logged in
def add_new_teammate(request):
    return HttpResponse("add_new_teammate")
