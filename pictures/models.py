from django.db import models

from .choices import MOOD_CHOICES, TREND_CHOICES
# Create your models here.


class Trend(models.Model):
    title = models.CharField(max_length=40,choices=TREND_CHOICES)
    trend_descrition = models.TextField()

    object = models.Manager()

    def __str__(self):
        return self.title

class Example_Trend_Posters(models.Model):
    trend = models.ForeignKey(Trend,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='example_trend_posters/')

class Painter(models.Model):
    full_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(auto_now=False,auto_now_add=False,null=True)
    date_of_death = models.DateField(auto_now=False,auto_now_add=False,null=True)
    about_painter = models.TextField()
    
    object = models.Manager()

    def __str__(self):
        return self.full_name

class Picture(models.Model):
    title = models.CharField(max_length=200)
    painter = models.ForeignKey(Painter,on_delete=models.CASCADE )
    writing_time = models.PositiveSmallIntegerField()
    trend = models.ForeignKey(Trend,on_delete=models.CASCADE)
    descrition = models.TextField()
    image = models.ImageField(upload_to='pictures_images/')
    mood = models.CharField(max_length=25, choices=MOOD_CHOICES) 

    object = models.Manager()

    def __str__(self):
        return self.title