from rest_framework.serializers import ModelSerializer, SerializerMethodField

from lms.models import Course, Lesson


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseDetailSerializer(ModelSerializer):
    lessons_count = SerializerMethodField()
    lessons_info = LessonSerializer(many=True, read_only=True)

    def get_lessons_count(self, obj):
        # метод для подсчета количества уроков курса

        return obj.lessons.count()

    class Meta:
        model = Course
        fields = ('name', 'description', 'preview', 'count_lessons', 'lessons_info')
