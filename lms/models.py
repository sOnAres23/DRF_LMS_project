from django.db import models


class Course(models.Model):
    """Модель создания обучающего курса"""
    name = models.CharField(max_length=255, unique=True, verbose_name="Название курса")
    preview = models.ImageField(upload_to='lms/photos/', blank=True, null=True, verbose_name="Превью курса")
    description = models.TextField(max_length=800, blank=True, null=True, verbose_name="Описание курса",
                                   help_text="Введите своё описание курса")
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, blank=True, null=True, verbose_name="Владелец")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата последнего обновления")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class CourseSubscription(models.Model):
    """Модель создания подписки на Курс"""
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name="Пользователь подписки")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Курс подписки")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата подписки")

    class Meta:
        verbose_name = "Подписка на курс"
        verbose_name_plural = "Подписки на курс"
        unique_together = (
            "user",
            "course",
        )  # Уникальность подписки

    def __str__(self):
        return f"{self.user.email} подписан на {self.course.name}"


class Lesson(models.Model):
    """Модель создания урока урока курса"""
    name = models.CharField(max_length=255, unique=True, verbose_name="Название урока")
    description = models.TextField(max_length=800, blank=True, null=True, verbose_name="Описание курса",
                                   help_text="Введите краткое описание урока")
    preview = models.ImageField(upload_to="lms/photos", blank=True, null=True, verbose_name="Превью урока")
    video_link = models.URLField(blank=True, null=True, verbose_name="Ссылка на видео",
                                 help_text="Укажите ссылку на видео")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="lessons", verbose_name="Курс")
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, blank=True, null=True, verbose_name="Владелец")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
