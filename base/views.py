from unicodedata import category
from django.shortcuts import render
from .models import Image, Category

# Create your views here.
def home(request):
    images = Image.objects.all()
    categorys = Category.objects.all()
    context = {'images':images,'categorys':categorys}
    return render(request, 'home.html' ,context)
