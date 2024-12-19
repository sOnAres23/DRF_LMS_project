from django.db import models


class Course(models.Model):
    """Модель создания обучающего курса"""
    name = models.CharField(max_length=255, unique=True, verbose_name="Название курса")
    preview = models.ImageField(upload_to='lms/photos/', blank=True, null=True, verbose_name="Превью курса")
    description = models.TextField(max_length=800, blank=True, null=True, verbose_name="Описание курса",
                                   help_text="Введите своё описание курса")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    """Модель создания урока урока курса"""
    name = models.CharField(max_length=255, unique=True, verbose_name="Название урока")
    description = models.TextField(max_length=800, blank=True, null=True, verbose_name="Описание курса",
                                   help_text="Введите краткое описание урока")
    preview = models.ImageField(upload_to="lms/photos", blank=True, null=True, verbose_name="Превью урока")
    video_link = models.URLField(blank=True, null=True, verbose_name="Ссылка на видео",
                                 help_text="Укажите ссылку на видео")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="lessons", verbose_name="Курс")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
