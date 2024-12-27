from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView, \
    get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from lms.models import Course, Lesson, CourseSubscription
from lms.paginators import MyCustomPagination
from lms.serializers import CourseSerializer, LessonSerializer, CourseDetailSerializer, CourseSubscriptionSerializer
from users.permissions import IsAdmin, IsOwner, IsModer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    pagination_class = MyCustomPagination

    def get_serializer_class(self):
        if self.action == "retrieve":
            return CourseDetailSerializer
        else:
            return CourseSerializer

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = (IsModer | IsAdmin, )
        elif self.action in ['update', 'retrieve']:
            self.permission_classes = (IsModer | IsOwner | IsAdmin, )
        elif self.action == 'destroy':
            self.permission_classes = (IsModer, IsOwner | IsAdmin)
        return super().get_permissions()


class SubscriptionCourseAPIView(ListAPIView):
    queryset = CourseSubscription.objects.all()
    serializer_class = CourseSubscriptionSerializer

    def post(self, request, *args, **kwargs):
        user = self.request.user
        course_id = self.request.data.get("course")
        course_item = get_object_or_404(Course, pk=course_id)

        subs_item = CourseSubscription.objects.filter(user=user, course=course_item)

        if subs_item.exists():
            subs_item.delete()
            message = "Подписка отключена"
        else:
            CourseSubscription.objects.create(user=user, course=course_item)
            message = "Подписка включена"
        return Response({"message": message})


class LessonCreateApiView(CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAdmin | IsOwner]

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()


class LessonListApiView(ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAdmin | IsModer | IsOwner]
    pagination_class = MyCustomPagination


class LessonUpdateApiView(UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAdmin | IsModer | IsOwner]


class LessonRetrieveApiView(RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAdmin | IsModer | IsOwner]


class LessonDestroyApiView(DestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAdmin | IsOwner]
