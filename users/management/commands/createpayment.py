from django.core.management import BaseCommand

from lms.models import Course
from users.models import Payments, User


class Command(BaseCommand):
    """Команда создания объекта оплаты курса"""
    def handle(self, *args, **options):
        Payments.objects.create(
            user=User.objects.get(pk=1),
            paid_course=Course.objects.get(pk=1),
            amount="100$",
            payment_method="Наличными"
        )  # Создаем оплату курса
        self.stdout.write(self.style.SUCCESS("Successfully created payment!"))
