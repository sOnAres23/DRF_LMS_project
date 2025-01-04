from rest_framework.serializers import ModelSerializer, SerializerMethodField

from lms.models import Course, Lesson, CourseSubscription
from lms.validators import validate_link_to_video


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [validate_link_to_video]


class CourseDetailSerializer(ModelSerializer):
    lessons_count = SerializerMethodField(label="Количество уроков")
    lessons_info = LessonSerializer(many=True, read_only=True, label="Информация по урокам")
    is_subscribed = SerializerMethodField(label="Наличие подписки")

    def get_lessons_count(self, obj):
        # метод для подсчета количества уроков курса

        return obj.lessons.count()

    def get_is_subscribed(self, obj):
        user = self.context.get("request").user
        if user.is_authenticated:
            return CourseSubscription.objects.filter(user=user, course=obj).exists()
        return False

    class Meta:
        model = Course
        fields = ('name', 'description', 'preview', 'owner', 'lessons_count', 'lessons_info', 'is_subscribed')


class CourseSubscriptionSerializer(ModelSerializer):
    class Meta:
        model = CourseSubscription
        fields = '__all__'
