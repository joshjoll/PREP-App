from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User


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
    project_name = models.CharField(max_length = 100)
    description = models.TextField(max_length = 250)
<<<<<<< HEAD
    teammate_role = models.TextField(max_length = 100)
=======
<<<<<<< HEAD
    teammate_role = models.TextField(max_length = 100)
=======
    teamate_role = models.TextField(max_length = 100)
>>>>>>> 95e11ba0bc8d5f53b700f03aac50154da8de2d58
>>>>>>> e059525dc69609e0ca9d61b52dcf95c01c431e56
    feedback = models.TextField(max_length = 250)
    git_hub_link = models.CharField(max_length = 250)
    deployed_app_link = models.CharField(max_length = 250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

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
    #This needs reconfigured, else tech will only be applied to user creating the project. Maybe accessed through projects for the user

    def get_absolute_url(self):
        return reverse('image', kwargs={'pk':self.project.id})


class Review(models.Model):
<<<<<<< HEAD
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    review = models.TextField(max_length = 250)
    rating = models.CharField(
        max_length=1,
=======
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
>>>>>>> e059525dc69609e0ca9d61b52dcf95c01c431e56
        choices = RATING,
    )

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.project.id})

    # def __str__(self):
    #     return f"{self.get_rating_display()} on {self.review}"

class Image(models.Model):
    url1 = models.CharField(max_length = 200)
    url2 = models.CharField(max_length = 200, blank=True)
    url3 = models.CharField(max_length = 200, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.project.id})

<<<<<<< HEAD
class User_details(models.Model):
    # first = models.CharField(max_length = 100)
    # last = models.CharField(max_length = 100)
    # email = models.CharField(max_length=100)
    # password = models.CharField(max_length=100)
    specialty = models.CharField(max_length = 100)
    cohort_date = models.DateField('cohort date')
    # project = models.ManyToManyField(Project)
    git_hub_link = models.CharField(max_length = 250)
    linkedin_link = models.CharField(max_length = 250)
    portfolio_link = models.CharField(max_length = 250)
=======
class User_Details(models.Model):
    first = models.CharField(max_length = 100)
    last = models.CharField(max_length = 100)
    email = models.CharField(max_length=100)
    specialty = models.CharField(max_length = 100)
    cohort_date = models.DateField('cohort date')
    project = models.ManyToManyField(Project)
    git_hub_link = models.CharField(max_length = 250, blank=True)
    linkedin_link = models.CharField(max_length = 250, blank=True)
    portfolio_link = models.CharField(max_length = 250, blank=True)
>>>>>>> e059525dc69609e0ca9d61b52dcf95c01c431e56

    def __str__(self):
        return self.first