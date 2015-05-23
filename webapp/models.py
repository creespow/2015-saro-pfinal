from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class event(models.Model):
    title          = models.CharField(max_length = 500, null=True)    
    price          = models.CharField(max_length = 500, null=True)
    long_duration  = models.IntegerField(null=True)
    date           = models.CharField(max_length = 500)
    time           = models.CharField(max_length = 500, null=True)
    url            = models.URLField(null=True)
    place          = models.CharField(max_length = 500, null=True)
    event_type     = models.CharField(max_length = 500, null=True)
    #points         = models.CharField(max_length = 500, null=True)
    

class user_choices(models.Model):
    user            = models.CharField(max_length = 200, null=True)    
    user_title      = models.CharField(max_length = 200, null=True)
    selected_event  = models.ManyToManyField(event, through='choice')
    background      = models.CharField(max_length = 200, null=True)
    font_colour     = models.CharField(max_length = 200, null=True)
    font_size       = models.CharField(max_length = 200, null=True)

class choice (models.Model):
    conten = models.ForeignKey(event)
    username = models.ForeignKey(user_choices)
    choose_date = models.CharField(max_length = 200)