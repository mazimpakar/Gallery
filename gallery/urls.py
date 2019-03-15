from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^location/$',views.location_of_gallery,name='locationGallery'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.category_gallery,name = 'categoryGallery') 
]
