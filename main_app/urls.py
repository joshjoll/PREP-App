from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing' ),
    path('projects/', views.Index.as_view(), name='index' ),
    path('projects/<int:project_id>', views.Project_Detail.as_view(), name='project_detail' ),
    path('projects/new/', views.New_Project.as_view(), name='new_project' ),
    path('', views.save_new_project, name='save_new_project' ),
    path('projects/<int:project_id>/update', views.Update_Project.as_view(), name='update_project' ),
    path('', views.update_project, name='update_project' ),
    path('', views.add_new_teammate, name='add_new_teammate' ),
    path('reviews/<int:project_id/new/', views.add_review, name='add_review' ),
    path('', views.save_review, name='save_review' ),
    path('reviews/<int:project_id>/team_reviews/', views.consolidated_review, name='consolidated_review' ),
    path('user/', views.Profile, name='profile' ),
    path('user/new/', views.new_user_form, name='new_user_form' ),
    path('', views.save_user, name='save_user' ),
]
