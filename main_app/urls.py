from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home' ),
    path('about/', views.about, name='about' ),
    path('projects/', views.gallery.as_view(), name='gallery' ),
    path('projects/<int:pk>/', views.Project_Detail.as_view(), name='detail' ),
    path('projects/new/', views.New_Project.as_view(), name='new_project' ),
    path('projects/<int:pk>/technology/', views.Add_Technology.as_view(), name='technology' ),
    path('projects/<int:pk>/image/', views.Add_Image.as_view(), name='image' ),
    path('projects/<int:pk>/update/', views.Update_Project, name='update_project' ),
    path('', views.add_new_teammate, name='add_new_teammate' ),
    path('reviews/<int:pk>/new/', views.new_review.as_view(), name='new_review' ),
    path('reviews/<int:pk>/team_reviews/', views.consolidated_review, name='consolidated_review' ),
    path('user/', views.Profile, name='profile' ),
    path('user/new/', views.signup, name='register' ),
    path('', views.save_user, name='save_user' ),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup', views.signup, name='signup'),
]
