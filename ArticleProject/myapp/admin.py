from django.contrib import admin
from myapp.models import ArticleModel
# Register your models here.

class ArticleModelAdmin(admin.ModelAdmin):
    list_display=['Title','Description']
    
admin.site.register(ArticleModel,ArticleModelAdmin)