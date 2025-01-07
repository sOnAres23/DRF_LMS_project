from django.contrib import admin

from lms.models import Course, Lesson, CourseSubscription
from users.models import Payments


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description", "preview")
    list_filter = ("name",)
    search_fields = ("name",)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description", "preview", "video_link", "course")
    search_fields = ("name",)
    list_filter = ("name",)


@admin.register(Payments)
class PaymentsAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "pay_date", "paid_course", "paid_lesson", "amount", "payment_method", "link")
    search_fields = ("paid_course",)
    list_filter = ("pay_date",)


@admin.register(CourseSubscription)
class CourseSubscriptionAdmin(admin.ModelAdmin):
    list_display = ("user", "course", "created_at")
    search_fields = ("user",)
    list_filter = ("created_at",)
