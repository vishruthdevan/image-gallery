from django.shortcuts import render
from django.urls import reverse
from .models import Category, Photo
# Create your views here.

def gallery(request):
    categories = Category.objects.all()
    photos = Photo.objects.all()
    context = {'categories' : categories, 'photos' : photos}
    print(reverse('photo', args=['69']))
    return render(request, 'photos/gallery.html', context)

def addPhoto(request):
    return render(request, 'photos/add.html')

def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request, 'photos/photo.html', {'photo':photo})