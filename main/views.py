from rest_framework import viewsets

from main.models import Habit
from main.serializers import HabitSerializer, HabitDetailSerializer


class HabitViewSet(viewsets.ModelViewSet):
    """ViewSet модели Habit."""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    # pagination_class = CustomPagination

    def get_serializer_class(self):
        """Выбор сериализатора в зависимости от запроса."""
        if self.action == "retrieve":
            return HabitDetailSerializer
        return HabitSerializer

    def perform_create(self, serializer):
        """Назначение владельца."""
        course = serializer.save()
        course.owner = self.request.user
        course.save()

    # def get_queryset(self):
    #     """Возвращает объекты пользователя."""
    #     if self.request.user.is_superuser:
    #         return Habit.objects.all()
    #     else:
    #         return Habit.objects.filter(owner=self.request.user.id)

    # def get_permissions(self):
    #     """Назначение разрешений."""
    #     if self.action == "create":
    #         self.permission_classes = (~IsModer,)
    #     elif self.action == "destroy":
    #         self.permission_classes = (~IsModer | IsOwner,)
    #     elif self.action in ["update", "retrieve"]:
    #         self.permission_classes = (IsModer | IsOwner,)
    #     return super().get_permissions()
