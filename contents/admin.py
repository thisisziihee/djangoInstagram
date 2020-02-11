from django.contrib import admin
from contents.models import Content, Image


class ImageInline(admin.TabularInline):
    model = Image


class ContentAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
    list_display = ('user', 'created_at', )


class ImageAdmin(admin.ModelAdmin):
    pass


admin.site.register(Content, ContentAdmin)
admin.site.register(Image, ImageAdmin)