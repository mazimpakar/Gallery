from django.test import TestCase
from .models import Image,Location,Category, 
# Create your tests here.


class ImageTestClass(TestCase):
    """
    Tests Image class and its functions
    """
    #Set up method
    def setUp(self):
        #creating a new location and saving it
        self.locale = Location(name='name', description='testing')
        self.locale.save_location()

        #creating a new category and saving it
        self.cat = Category(name='this', description='testing1')
        self.cat.save_cat()

        #creating an new image 
        self.image = Image(photo='test.jpg', name='name', description = 'this photo', location=self.locale, category = self.cat)

    def test_instance(self):
        self.assertTrue(isinstance(self.image, Image))

    def test_save_method(self):
        """
        Function to test an image and its details is being saved
        """
        self.image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def test_delete_method(self):
        """
        Function to test if an image can be deleted
        """
        self.image.save_image()
        self.image.delete_image()

    def test_update_method(self):
        """
        Function to test that an image's details can be updates
        """
        self.image.save_image()
        new_image = Image.objects.filter(photo='test.jpg').update(photo='hii.jpg')
        images = Image.objects.get(photo='hii.jpg')
        self.assertTrue(images.photo, 'hii.jpg')

    def test_get_image_by_id(self):
        """
        Function to test if you can get an image by its id
        """
        self.image.save_image()
        this_img= self.image.get_image_by_id(self.image.id)
        image = Image.objects.get(id=self.image.id)
        self.assertTrue(this_img, image)
       
    def test_filter_by_location(self):
        """
        Function to test if you can get an image by its location
        """
        self.image.save_image()
        this_img = self.image.filter_by_location(self.image.location_id)
        image = Image.objects.filter(location=self.image.location_id)
        self.assertTrue(this_img, image)

    def test_filter_by_category_name(self):
        """
        Function to test if you can get an image by its category name
        """
        self.image.save_image()
        images = Image.search_term('this')
        self.assertTrue(len(images)>0)
        
