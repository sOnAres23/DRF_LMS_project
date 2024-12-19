from django.urls import path
from rest_framework.routers import DefaultRouter

from users import views

app_name = 'users'

router = DefaultRouter()
router.register(r'users', views.UserViewSet, basename='users')

urlpatterns = [
    path("payments/", views.PaymentListAPIView.as_view(), name="payments_list"),

] + router.urls
