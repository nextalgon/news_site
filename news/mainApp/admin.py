from django.contrib import admin
from .models import Category, NewTopic


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name",)


class TopicAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


admin.site.register(Category, CategoryAdmin)
admin.site.register(NewTopic, TopicAdmin)
