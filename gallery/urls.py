from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url('^location/$',views.location_of_gallery,name='locationGallery'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.category_gallery,name = 'categoryGallery') 
]
