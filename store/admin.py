from django.contrib import admin

from .models import Item


class ItemAdmin(admin.ModelAdmin):
    list_display = ('title',  'slug', 'price',
                    'is_available', 'tag_list', 'image')
    search_fields = ('title', 'description', 'tags__name',)