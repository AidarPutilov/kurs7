from django.urls import path
from rest_framework.routers import DefaultRouter

from main.apps import MainConfig
from main.views import HabitViewSet, HabitPublicListAPIView


app_name = MainConfig.name

router = DefaultRouter()
router.register(r"", HabitViewSet, basename="habits")

urlpatterns = [
    path("public/", HabitPublicListAPIView.as_view(), name="public_habits"),
    # path("lesson/<int:pk>/", LessonRetrieveAPIView.as_view(), name="lesson_retrieve"),
    # path("lesson/create/", LessonCreateAPIView.as_view(), name="lesson_create"),
    # path(
    #     "lesson/<int:pk>/delete/", LessonDestroyAPIView.as_view(), name="lesson_delete"
    # ),
    # path(
    #     "lesson/<int:pk>/update/", LessonUpdateAPIView.as_view(), name="lesson_update"
    # ),
    # path(
    #     "subscription/",
    #     SubscriptionAPIView.as_view(),
    #     name="subscription",
    # ),
] + router.urls
