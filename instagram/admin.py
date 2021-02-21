from django.contrib import admin
from . import models


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ["message"]
    list_display = ["pk", "message", "author"]
