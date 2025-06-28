from django.shortcuts import render
from django.urls import reverse
# Create your views here.

def gallery(request):
    print(reverse('photo', args=['69']))
    return render(request, 'photos/gallery.html')

def addPhoto(request):
    return render(request, 'photos/add.html')

def viewPhoto(request, pk):
    return render(request, 'photos/photo.html')