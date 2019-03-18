from django.shortcuts import render,redirect
from .models import Image,Category,Location
from django.http import Http404

# Create your views here.
def gallery(request):
    images = Image.objects.all()
    locations = Location.objects.all()
    return render(request,'all-gallery/gallery.html',{'images':images,'locations':locations})

def display_location(request):
    try:
        location = Location.objects.get(id = location_id)
        photos = Image.objects.filter(image_location = location.id)
    except:
        raise Http404()
    return render(request,'all-gallery/location-gallery.html',{'location':location,'images':images})

def search_results(request):
    if 'image' in request.GET and request.GET['image']:
        search_input = request.GET.get('image')
        searched_images = Image.search_by_category(search_input)
        message = f"{search_input}"

        return render(request, 'search.html', {"message":message, "images":searched_images})

    else:
        message = "Please input something in the search field"
        return render(request, 'search.html', {'message':message})
def display_images_categories(request):    
    images = Image.image_categories()

    return render(request, 'category.html', {"images":images}) 

def display_images_locations(request):    
    images = Image.image_locations()

    return render(request, 'location.html', {"images":images}) 

