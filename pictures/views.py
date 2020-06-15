from django.shortcuts import render
from .models import Picture,Painter,Trend
from django.http import HttpRequest
import random 
# Create your views here.

def index_view(req:HttpRequest):
    paints = Picture.object.all()
    random_paints = random.sample(paints,5)
    Aivazovsky = Painter.object.get(full_name='Aivazovsky, Ivan Konstantinovich')
    
    return render(req , 'index.html',{'random_paints':random_paints},)