from django.contrib import admin
from pastebin.pastebin.models import Paste

# Register your models here.


class PasteAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'title', 'poster', 'syntax', 'timestamp')
    list_filter = ('timestamp', 'syntax')


admin.site.register(Paste, PasteAdmin)
