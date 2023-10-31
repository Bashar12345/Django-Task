from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Task
from .models import Photo


class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "priority", "created_at", "updated_at")
    list_filter = ("priority",)
    search_fields = ("title", "description")
    ordering = ("-priority",)


class PhotoAdmin(admin.ModelAdmin):
    list_display = ("task", "caption", "created_at", "updated_at")
    list_filter = ("task",)
    search_fields = ("caption",)


admin.site.register(Photo, PhotoAdmin)
admin.site.register(Task, TaskAdmin)
