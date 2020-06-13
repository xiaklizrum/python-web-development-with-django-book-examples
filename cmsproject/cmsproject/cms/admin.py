from django.contrib import admin
from cmsproject.cms.models import Story, Category


# Register your models here.


class StoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'status', 'created', 'modified')
    search_fields = ('title', 'content')
    list_filter = ('status', 'owner', 'created', 'modified')
    prepopulated_fields = {'slug': ('title',)}


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('label',)}


admin.site.register(Story, StoryAdmin)
admin.site.register(Category, CategoryAdmin)
