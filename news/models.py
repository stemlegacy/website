from django.db import models
from django import template

# Create your models here.
class event(models.Model):
    event_name = models.CharField(max_length=300)
    event_type = models.CharField(max_length=300)
    event_place = models.CharField(max_length=300)
    event_date = models.CharField(max_length=300)

    def __str__(self):
        return self.event_name + "-" + self.event_place
class speaker(models.Model):
    event = models.ForeignKey(event,on_delete=models.CASCADE)
    speaker_name = models.CharField(max_length=300)
    speaker_type = models.CharField(max_length=300)

    def __str__(self):
        return self.speaker_name
class memberss(models.Model):
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250 , default="")
    jop = models.CharField(max_length=250)
    pic = models.FileField()

    def __str__(self):
        return self.name

class images(models.Model):
    image = models.ImageField()
    place = models.CharField(max_length=250,default="")
    eventt = models.CharField(max_length=250,default="")


