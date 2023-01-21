from django.contrib import admin
from .models import Articles,Comment

admin.site.register(Comment)
# Register your models here.
@admin.register(Articles)
class ArticleAdmin(admin.ModelAdmin):
    list_display=["title","autor","created_date"]
    list_display_links=["title","autor","created_date"]
    search_fields =["title"]
    list_filter=["created_date"]
    class Meta():
        model=Articles
        
            