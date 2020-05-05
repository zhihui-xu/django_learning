from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Gallery


def home(request):
    gallery_list = Gallery.objects.all()
    return render(request, "home.html", {"gallerys": gallery_list})
