from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import JsonResponse
from .models import ImageModel
# Create your views here.


def home(request):
    context = {}
    return render(request,'home.html',context)

def preloader(request):
    data = {}
    images = request.FILES.getlist('images')
    imagelist = []
    for image in images:
        created = ImageModel.objects.create(image=image)
        imagelist.append(created)
    data['include'] = render_to_string('images.html', {'imagelist':imagelist}, request)
    return JsonResponse(data)