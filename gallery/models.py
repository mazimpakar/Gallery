from django.db import models
import datetime as dt
# Create your models here.
class Location(models.Model):
    """
    Class that contains location details of the image posted
    """
    name = models.CharField(max_length = 30)
    description = models.TextField()

    def __str__(self):
        return self.name

    def save_location(self):
        self.save()

    def del_location(self):
        self.delete()
class Category(models.Model):
    """
    Class that contains the category details of the image posted
    """
    name = models.CharField(max_length = 30)
    description = models.TextField()

    def __str__(self):
        return self.name

    def save_cat(self):
        self.save()

    def del_cat(self):
        self.delete()

class Image(models.Model):
    photo = models.ImageField(upload_to = 'images/',blank=True,)
    image_name = models.CharField(max_length =30)
    description = models.CharField(max_length =30)
    location = models.ForeignKey(Location,max_length=140,on_delete =models.CASCADE, blank=True, null=True) 
    category = models.ForeignKey(Category,max_length=140,on_delete =models.CASCADE,  blank=True, null=True) 

    
    def __str__(self):
        return self.name

    def save_image(self):
        self.save()   

    def delete_image(self):
        Image.objects.filter(id = self.pk).delete() 
    
    def update_image(self, **kwargs):
        self.objects.filter(id = self.pk).update(**kwargs)       

    @classmethod
    def all_images(cls):
        images = cls.objects.all()
        return iamges 

    @classmethod
    def image_locations(cls):
        images = cls.objects.order_by('location')
        return images 

    @classmethod
    def image_categories(cls):
        images = cls.objects.order_by('category')
        return image 

    @classmethod
    def get_image(cls, id):
        image = cls.objects.get(id=id)
        return image

    @classmethod
    def search_by_category(cls, search_input):
        image = cls.objects.filter(category__name__icontains=search_input)
        return image      

    class Meta:
        ordering = ['image_name']