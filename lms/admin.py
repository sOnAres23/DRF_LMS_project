from django.contrib import admin

from lms.models import Course, Lesson


@admin.register(Course)
class RecipientMailingAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description", "preview")
    list_filter = ("name",)
    search_fields = ("name",)


@admin.register(Lesson)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description", "preview", "video_link", "course")
    search_fields = ("name",)
    list_filter = ("name",)
