from django.contrib import admin
from .models import car
from django.utils.html import format_html
# Register your models here.

class CarAdmin(admin.ModelAdmin):

    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius:10px;" />'.format(object.car_photo.url))

    thumbnail.short_description ='Car Image'

    list_display =('id','thumbnail','car_title','city','color','model','year','created_date','is_featured')
    list_display_links =('id','thumbnail','car_title')
    search_fields =('car_title','model','year','color')
    list_filter =('city','model','year')


admin.site.register(car,CarAdmin)
