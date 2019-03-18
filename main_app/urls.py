from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing' ),
    path('projects/', views.Index.as_view(), name='index' ),
    path('projects/<int:project_id>/', views.Project_Detail.as_view(), name='project_detail' ),
    path('projects/new/', views.New_Project.as_view(), name='new_project' ),
    path('projects/<int:project_id>/update/', views.Update_Project.as_view(), name='update_project' ),
    path('', views.add_new_teammate, name='add_new_teammate' ),
    path('reviews/<int:project_id/new/', views.new_review.as_view(), name='new_review' ),
    path('reviews/<int:project_id>/team_reviews/', views.consolidated_review, name='consolidated_review' ),
    path('user/', views.Profile, name='profile' ),
    path('user/new/', views.signup, name='signup' ),
    path('', views.save_user, name='save_user' ),
]
