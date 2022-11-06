from django.contrib import admin
from .models import *
# Register your models here.
class ClientAdmin(admin.ModelAdmin):
    list_display=['id', 'client_name','created_at','created_by']
admin.site.register(Client,ClientAdmin)

class ProjectAdmin(admin.ModelAdmin):
    list_display=['id', 'name']
admin.site.register(Project,ProjectAdmin)