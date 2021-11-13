from django.contrib import admin

from urlshortener.models import Shortener


class ShortenerAdmin(admin.ModelAdmin):
    pass


admin.site.register(Shortener, ShortenerAdmin)
