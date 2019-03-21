from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User


RATING = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5')
)

# Create your models here.
class Project(models.Model):
    cohort_date = models.DateField('project date')
    name = models.CharField(max_length = 100)
    description = models.TextField(max_length = 250)
    teamate_role = models.TextField(max_length = 100)
    feedback = models.TextField(max_length = 250)
    git_hub_link = models.CharField(max_length = 250)
    deployed_app_link = models.CharField(max_length = 250)

    def get_absolute_url(self):
        return reverse('technology', kwargs={'pk':self.id})

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-cohort_date']


class Technology(models.Model):
    tech_type = models.TextField(max_length = 250)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    #This needs reconfigured, else tech will only be applied to user creating the project. Maybe accessed through projects for the user

    def get_absolute_url(self):
        return reverse('image', kwargs={'pk':self.project.id})


class Review(models.Model):
    review = models.TextField(max_length = 250)
    rating = models.CharField(
        max_length=1,
        choices = RATING,
    )
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.project.id})

    def __str__(self):
        return f"{self.get_rating_display()} on {self.review}"

class Image(models.Model):
    url = models.CharField(max_length = 200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.project.id})

class User(models.Model):
    first = models.CharField(max_length = 100)
    last = models.CharField(max_length = 100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    specialty = models.CharField(max_length = 100)
    cohort_date = models.DateField('cohort date')
    project = models.ManyToManyField(Project)
    git_hub_link = models.CharField(max_length = 250)
    linkedin_link = models.CharField(max_length = 250)
    deployed_app_link = models.CharField(max_length = 250)

    def __str__(self):
        return self.first