from django.contrib import admin

from lms.models import Course, Lesson
from users.models import Payments


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


@admin.register(Payments)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "pay_date", "paid_course", "paid_lesson", "amount", "payment_method")
    search_fields = ("paid_course",)
    list_filter = ("pay_date",)
