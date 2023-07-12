from django.contrib import admin
from .models import Person, Organisation, CreativeWork, Service, WebAPI, SoftwareApplication


# Register your models here.
admin.site.register(Person)
admin.site.register(Organisation)
admin.site.register(CreativeWork)
admin.site.register(Service)
admin.site.register(WebAPI)
admin.site.register(SoftwareApplication)
