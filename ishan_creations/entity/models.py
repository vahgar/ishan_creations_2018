from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name

class Area(models.Model):
    name = models.CharField(max_length=200, blank=True)
    city = models.ForeignKey(City, blank=False)

    def __str__(self):
        return self.name

class Locality(models.Model):
    name = models.CharField(max_length=200, blank=True)
    area = models.ForeignKey(Area)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("entity:category_wise", kwargs={'id':self.id})



class Business_Entity(models.Model):

    name = models.CharField(max_length=200,blank=True);
    profile = models.CharField(max_length=4096,blank=True,null=True);
    services = models.CharField(max_length=4096,blank=True,null=True);
    timings = models.CharField(max_length=150,blank=True,null=True);
    contact_person = models.CharField(max_length=150,blank=True,null=True);
    address = models.CharField(max_length=1000,blank=True,null=True);
    mobile = models.CharField(max_length=20,blank=True,null=True);
    whatsapp = models.CharField(max_length=10,blank=True,null=True)
    Email = models.EmailField(max_length=70,blank=True,null=True)
    website = models.CharField(max_length=70,default="#")
    social_media = models.CharField(max_length=300,default="#")
    customer_rating = models.FloatField(blank=True,null=True,)
    # city = models.ForeignKey(City,blank=True,null=True)
    # area = models.ForeignKey(Area,blank=True,null=True)
    # locality = models.ForeignKey(Street,blank=True,null=True)
    category = models.ForeignKey(Category,blank=True,null=True)
    # subcategory = models.ForeignKey(SubCategory,blank=True,null=True)
    # subsubcategory = models.ForeignKey(SubsubCategory,blank=True,null=True)
    image_1 = models.FileField(upload_to = 'entity_pics/', blank = True, null=True)



    def __str__(self):
    	return self.name

    def get_absolute_url(self):
        return reverse("entity:entity_full", kwargs={'id':self.id})


class Display_pics(models.Model):
    images = models.ImageField(upload_to = 'entity_pics/', blank = True, null=True)
    entity = models.ForeignKey(Business_Entity)

    
