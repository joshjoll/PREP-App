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
def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
# Display Index Page of all projects
class gallery(ListView):
    model = Project
    template_name = 'projects/gallery.html'

# Display project details. Limit to logged in
class Project_Detail(DetailView):
    model = Project
# Loads new project form page, Needs to limit to logged in
# CBV
class New_Project(CreateView):
    model = Project
    fields= '__all__'


# Loads upon submit of New_Project form
class Add_Technology(CreateView):
    model = Technology
    fields= ['tech_type']
    def form_valid (self, form):
        form.instance.project = project = Project.objects.get(id=self.kwargs.get('pk'))
        return super(Add_Technology, self).form_valid(form)
        return reverse('image', kwargs={'pk': form.instance.project.id})


# Loads upon submit of Add_Technology form
class Add_Image(CreateView):
    model = Image
    fields= ['url']
    def form_valid (self, form):
        form.instance.project = project = Project.objects.get(id=self.kwargs.get('pk'))
        return super(Add_Image, self).form_valid(form)
        return reverse('detail', kwargs={'pk': form.instance.project.id})
# Loads page to update project. Limit to logged in
# CBV
def Update_Project(request, project_id):
    project = Project.objects.get(id=project_id)
    review = project.review.all()

    return render(request, 'projects/update.html', {
    'project': project,
    'review': review,
    })

#REVIEW RELATED VIEWS

# Loads new review Page. Limit to logged in
# CBV
class new_review(CreateView):
    model = Review
    fields= ['review', 'rating']
    def form_valid (self, form):
        form.instance.project = project = Project.objects.get(id=self.kwargs.get('pk'))
        return super(new_review, self).form_valid(form)
        return reverse('detail', kwargs={'pk': form.instance.project.id})

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
