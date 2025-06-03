from django.contrib import admin
from testapp.models import BlogModel
# Register your models here.
class BlogModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','content','image','author']
admin.site.register(BlogModel,BlogModelAdmin)
