from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

PROJECT_STATUS = (
        ('Completed', 'Complete'),
        ('Ongoing', 'Ongoing'),
    )

class Post(models.Model):
    title = models.CharField(max_length=100, help_text="Title the post will bear")
    content = models.TextField(help_text="The actual Blog Post")
    url = models.URLField(help_text="Any outside link", blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog-home')

class Projects(models.Model):
    title = models.CharField(max_length=100, help_text="Title of the project")
    idea = models.CharField(max_length=100, blank=True, null=True, help_text="The idea behind the project")
    technologies = models.CharField(max_length=100, blank=True, null=True, help_text="The technologies which have made the project")
    date_started = models.DateTimeField(default=timezone.now)
    git_link = models.URLField(blank=True, null=True, help_text="GitHub link to the project")
    project_link = models.URLField(blank=True, null=True, help_text="The website of the project online")
    status = models.CharField(max_length=100, choices=PROJECT_STATUS, default='completed', help_text="Status of the project")
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('project-detail', kwargs={'pk':self.pk})

class Messages(models.Model):
    name = models.CharField(max_length=100, help_text="Please enter your full name")
    email = models.EmailField(help_text="Please enter your email")
    message = models.TextField(help_text="Please enter your message")
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        message = 'message submitted successfully. Wait for response in your email'
        return reverse('blog-home')