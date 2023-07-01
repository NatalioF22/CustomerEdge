from django.contrib import admin
from .models import Record

# Register your models here.
admin.site.register(Record)

class RecordAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','address','phone','email','state','zip_code')
    ordering = ('first_name',)
    search_fields =  ('first_name','last_name','address','phone','email','state','zip_code')