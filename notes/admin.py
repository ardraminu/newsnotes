from django.contrib import admin

from.models import Category,Notes

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('image_tag','title','description','url')
    search_fields = ('title',)
admin.site.register(Category, CategoryAdmin)


class NotesAdmin(admin.ModelAdmin):
    list_display = ('note_title','content')
    search_fields = ('note_title',)
    list_filter = ('cat',)
    list_per_page = 5
admin.site.register(Notes, NotesAdmin)