from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.views.generic import ListView, DetailView
#maybe don't need
from django import forms
#Auth related imports
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
#Model imports
from .models import Project, Technology, Review, Image, User
from django.contrib.auth.models import User

# Create your views here.

#PROJECT RELATED VIEWS
# Display Landing Page
def landing(request):
    return render(request, 'landing.html')
# Display Index Page of all projects
class Index(ListView):
    model = Project

# Display project details. Limit to logged in
class Project_Detail(DetailView):
    model = Project
# Loads new project form page, Limit to logged in
# CBV
class New_Project(CreateView):
    model = Project
    fields= '__all__'
    success_url = 'projects/<int:project_id>/'
# Loads page to update project. Limit to logged in
# CBV
class Update_Project(UpdateView):
    model = Project
    fields= '__all__'
    success_url = 'projects/<int:project_id>/'

#REVIEW RELATED VIEWS

# Loads new review Page. Limit to logged in
# CBV
class new_review(CreateView):
    model = Project
    fields= '__all__'
    success_url = 'projects/<int:project_id>/'
# Loads consolidated review page. Limit to team members
# CBV model template
def consolidated_review(request, project_id):
    rev = Review.objects.filter(id=project_id)
    return render(request, "consolidated_review",{ 'review': rev })

#USER RELATED VIEWS
#
from django.contrib.auth import login
# from django.contrib.auth.forms import user_creat_form
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.mixins import login_RequiredMixin
# Display User Profile Page. Limit to logged in
class Profile(DetailView):
    model = User
# Loads sign up page
# CBV

# class UserCreateForm(UserCreationForm):
#     extra_field = forms.CharField(required=True)
#
#     class Meta:
#         model = User
#         fields = ("andrey",)
#
#     def save(self, commit=True):
#         user = super(UserCreateForm, self).save(commit=False)
#         user.extra_field = self.cleaned_data["extra_field"]
#         if commit:
#             user.save()
#         return user

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid credentials - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)
# Saves new users, redirects to index page
def save_user(request):
    return HttpResponse("save_user")

# Complicated. Lets users search for their cohort, then select a class member and add them to a project. From owner detail page, redirects to owner detail page. Limit to logged in
def add_new_teammate(request, project_id, username):
    find_user = User.objects.get(name=userid).project.add(project_id)
    return HttpResponse("add_new_teammate")
