from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver


RATING = (
    (1, '1 Stars'),
    (2, '2 Stars'),
    (3, '3 Stars'),
    (4, '4 Stars'),
    (5, '5 Stars')
)


# Create your models here.
class Project(models.Model):
    cohort_date = models.DateField('project date')
    name = models.CharField(max_length = 100)
    description = models.TextField(max_length = 250)
    teammate_role = models.TextField(max_length = 100, blank=True)
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
    tech1 = models.CharField(max_length = 200)
    tech2 = models.CharField(max_length = 200, blank=True)
    tech3 = models.CharField(max_length = 200, blank=True)
    tech4 = models.CharField(max_length = 200, blank=True)
    tech5 = models.CharField(max_length = 200, blank=True)
    tech6 = models.CharField(max_length = 200, blank=True)
    tech7 = models.CharField(max_length = 200, blank=True)
    tech8 = models.CharField(max_length = 200, blank=True)
    tech9 = models.CharField(max_length = 200, blank=True)
    tech10 = models.CharField(max_length = 200, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('image', kwargs={'pk':self.project.id})


class Review(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    pitchdeck_review = models.TextField('Pitch Deck Feedback', max_length = 250)
    pitchdeck_rating = models.IntegerField(
        'Pitch Deck Rating',
        choices = RATING,
    )
    content_review = models.TextField('Content Feedback',max_length = 250)
    content_rating = models.IntegerField(
        'Content Rating',
        choices = RATING,
    )
    UIUX_review = models.TextField('UI/UX Feedback', max_length = 250)
    UIUX_rating = models.IntegerField(
        'UI/UX Rating',
        choices = RATING,
    )
    clean_code_review = models.TextField('Code Feedback', max_length = 250)
    clean_code_rating = models.IntegerField(
        'Code Rating',
        choices = RATING,
    )
    presentation_review = models.TextField('Presentation Feedback', max_length = 250)
    presentation_rating = models.IntegerField(
        'Presentation Rating',
        choices = RATING,
    )

    def get_absolute_url(self):
        return reverse('project_detail', kwargs={'pk': self.project.id})

    # def __str__(self):
    #     return f"{self.get_rating_display()} on {self.review}"


class Image(models.Model):
    url1 = models.CharField(max_length = 200)
    url2 = models.CharField(max_length = 200, blank=True)
    url3 = models.CharField(max_length = 200, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


    def get_absolute_url(self):
        return reverse('project_detail', kwargs={'pk': self.project.id})


class User_Details(models.Model):
    first = models.CharField(max_length = 100, blank=True)
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    last = models.CharField(max_length = 100, blank=True)
    email = models.CharField(max_length=100, blank=True)
    specialty = models.CharField(max_length = 100, blank=True)
    cohort_date = models.DateField('cohort date', blank=True)
    project = models.ManyToManyField(Project, blank=True)
    git_hub_link = models.CharField(max_length = 250, blank=True)
    linkedin_link = models.CharField(max_length = 250, blank=True)
    portfolio_link = models.CharField(max_length = 250, blank=True)

    def __str__(self):
        return self.first
    def get_absolute_url(self):
        return reverse('gallery')
