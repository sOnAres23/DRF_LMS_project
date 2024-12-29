from django.contrib.auth.models import AbstractUser
from django.db import models

from lms.models import Course, Lesson


class User(AbstractUser):
    """Модель создания и регистрации пользователя"""
    username = None
    email = models.EmailField(unique=True, verbose_name='Ваша почта')
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    phone_number = models.CharField(max_length=15, blank=True, null=True, verbose_name='Номер телефона')
    avatar = models.ImageField(upload_to='users/avatars/', blank=True, null=True, verbose_name='Фото(необязательно)')
    city = models.CharField(max_length=50, blank=True, null=True, verbose_name='Город проживания')
    token = models.CharField(max_length=100, verbose_name="Токен", blank=True, null=True,)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        permissions = []


class Payments(models.Model):
    """Модель создания платежей пользователь"""

    CASH = "Наличные"
    TRANSFER = "Перевод на счет"

    STATUS_CHOICES = [
        (CASH, "Наличные"),
        (TRANSFER, "Перевод на счет"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь", related_name="payments")
    pay_date = models.DateField(verbose_name="Дата платежа", auto_now_add=True)
    paid_course = models.ForeignKey(Course, on_delete=models.CASCADE, blank=True, null=True,
                                    verbose_name="Оплаченный курс")
    paid_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, blank=True, null=True,
                                    verbose_name="Оплаченный урок")
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Сумма платежа")
    payment_method = models.CharField(max_length=30, choices=STATUS_CHOICES, default=TRANSFER,
                                      verbose_name="Метод оплаты")
    session_id = models.CharField(max_length=255, verbose_name="ID сессии",
                                  help_text="Укажите ID сессии для перевода на счет", blank=True, null=True,)
    link = models.URLField(max_length=400, verbose_name="Ссылка на оплату",
                           help_text="Укажите ссылку на оплату", blank=True, null=True,)

    def __str__(self):
        return f"Платеж {self.amount} от {self.user}"

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"
