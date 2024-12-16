from django.urls import path
from rest_framework.routers import DefaultRouter

from lms import views

app_name = 'lms'

router = DefaultRouter()
router.register(r'courses', views.CourseViewSet, basename='courses')

urlpatterns = [path("lesson/create/", views.LessonCreateApiView.as_view(), name="lesson_create"),
               path("lessons/", views.LessonListApiView.as_view(), name="lessons_list"),
               path("lesson/update/<int:pk>/", views.LessonUpdateApiView.as_view(), name="lesson_update"),
               path("lesson/<int:pk>/", views.LessonRetrieveApiView.as_view(), name="lesson_detail"),
               path("lesson/delete/<int:pk>/", views.LessonDestroyApiView.as_view(), name="lesson_delete"),

               ] + router.urls
