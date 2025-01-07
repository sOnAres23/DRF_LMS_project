from datetime import timedelta

from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone

from config.settings import EMAIL_HOST_USER
from lms.models import Course, CourseSubscription
from users.models import User


@shared_task
def send_course_update_email(course_id):
    """Задача по отправке писем с сообщением об обновлении курса"""
    course = Course.objects.get(id=course_id)
    subscriptions = CourseSubscription.objects.none()
    if timezone.now() - course.updated_at > timedelta(hours=8):
        subscriptions = CourseSubscription.objects.filter(course_id=course_id)

    if subscriptions.exists():
        for subscription in subscriptions:
            print(f"Отправка письма на {subscription.user.email}")
            send_mail(
                "Обновление курса",
                f"Курс {subscription.course.name} был обновлён.",
                EMAIL_HOST_USER,
                [
                    subscription.user.email,
                ],
                fail_silently=False,
            )
    else:
        print(f"Уведомление не отправлено, курс был обновлен менее 8 часов назад")


@shared_task
def block_inactive_users():
    """Задача по блокировке пользователей не активных в течение месяца"""
    month_ago = timezone.now() - timedelta(days=30)
    inactive_users = User.objects.filter(last_login__lt=month_ago, is_active=True)
    inactive_users.update(is_active=False)
    print(f"Статуc пользователя изменен")
