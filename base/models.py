from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Image(models.Model):
    image = models.ImageField(upload_to='image/',default='Image')
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    location = models.ForeignKey(Location , on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    updated = models.DateTimeField(auto_now=True) 
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated','-created']

    def __str__(self):
        return self.name

    def save_image(self):
        '''
        method to save the image
        '''
        self.save()
    
    @classmethod
    def search_by_category(cls, search_term):
        '''
        method to search image by its category
        '''
        image = cls.objects.filter(category__icontains = search_term)
        return image
    @classmethod
    def filter_by_location(cls, search_term):
        '''
        method to filter images by their location
        '''
        image = cls.objects.filter(location__icontains = search_term)
        return image 

