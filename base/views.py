from unicodedata import category
from django.shortcuts import render
from .models import Image, Category
from django.db.models import Q

# Create your views here.
def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    images = Image.objects.filter(
        Q(name__icontains=q) |
        Q(category__name__icontains=q) |
        Q(description__icontains=q)
    )

    categorys = Category.objects.all()

    context = {'images':images,'categorys':categorys}
    return render(request, 'home.html' ,context)
