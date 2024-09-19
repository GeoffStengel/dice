from django.contrib import admin

# Register your models here.
from .models import HomePage, PetProfile, AboutPage

admin.site.register(HomePage)
admin.site.register(PetProfile)
admin.site.register(AboutPage)