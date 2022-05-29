from django.shortcuts import render
from .models import Image, Location
from django.db.models import Q

# Create your views here.
def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    images = Image.objects.filter(
        Q(name__icontains=q) |
        Q(category__name__icontains=q) |
        Q(description__icontains=q) |
        Q(location__name__icontains=q)
    )

    locations = Location.objects.all()

    context = {'images':images,'locations':locations}
    return render(request, 'home.html' ,context)
