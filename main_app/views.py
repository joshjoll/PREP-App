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
from .models import Project, Technology, Review, Image, User_details
from django.contrib.auth.models import User

# Create your views here.

#PROJECT RELATED VIEWS
# Display Landing Page
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')
# Display Index Page of all projects
def gallery(request):
    projects = Project.objects.all()
    return render(request, 'projects/gallery.html', {'projects': projects})
# class gallery(ListView):
#     model = Project
#     fields= ['name', 'teammate_role']
#     template_name = 'projects/gallery.html'

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
    fields= ['tech1', 'tech2', 'tech3', 'tech4', 'tech4', 'tech5', 'tech6', 'tech7', 'tech8', 'tech9', 'tech10']
    def form_valid (self, form):
        form.instance.project = project = Project.objects.get(id=self.kwargs.get('pk'))
        return super(Add_Technology, self).form_valid(form)
        return reverse('image', kwargs={'pk': form.instance.project.id})


# Loads upon submit of Add_Technology form
class Add_Image(CreateView):
    model = Image
    fields= ['url1', 'url2', 'url3']
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
    fields= ['pitchdeck_review', 'pitchdeck_rating', 'content_review', 'content_rating', 'UIUX_review', 'UIUX_rating', 'clean_code_review', 'clean_code_rating', 'presentation_review', 'presentation_rating',]
    def form_valid (self, form):
        form.instance.project = project = Project.objects.get(id=self.kwargs.get('pk'))
        return super(new_review, self).form_valid(form)
        return reverse('detail', kwargs={'pk': form.instance.project.id})

# Loads consolidated review page. Limit to team members
# CBV model template
def consolidated_review(request, pk):
    rev = Review.objects.filter(project=pk)
    project = Project.objects.get(id=pk)
    return render(request, "consolidated_review.html", { 'review': rev, 'project': project })

#USER RELATED VIEWS
#
# from django.contrib.auth import login
# from django.contrib.auth.forms import user_creat_form
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.mixins import login_RequiredMixin
# Display User Profile Page. Limit to logged in
class Profile(DetailView):
    model = User_details
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
            return redirect('gallery')
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
    find_user = User.objects.get(name=userid)
    find_user.project.add(project_id)
    return redirect("add_new_teammate")
    # on detail template: {% if user.project.id = pk %}Display team view stuff {% else %} Display review stuff
