from django.contrib import admin
from .models import Animal, RescueCenter, Contact

admin.site.register(Animal)
admin.site.register(RescueCenter)
admin.site.register(Contact)