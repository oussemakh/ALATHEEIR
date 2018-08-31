from django.contrib import admin
from .models import articles_News, articles_Analyse, articles_Tutorial

# Register your models here.
class AdminNews(admin.ModelAdmin):
    list_display =('title','date','slug',)
    list_display_links = ('date',)
    list_filter = ('date',)
    search_fields = ('title','date', 'slug',)
    list_editable = ('title','slug',)


admin.site.register(articles_News, AdminNews)



admin.site.register(articles_Analyse,AdminNews )





admin.site.register(articles_Tutorial,AdminNews)
