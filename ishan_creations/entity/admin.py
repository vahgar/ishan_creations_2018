from django.contrib import admin

# Register your models here.
from entity.models import City, Area, Locality, Business_Entity, Category

admin.site.register(City)
admin.site.register(Area)
admin.site.register(Locality)
admin.site.register(Business_Entity)
admin.site.register(Category)
