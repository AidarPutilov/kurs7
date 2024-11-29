from django.core.management import BaseCommand
from main.models import Habit
from users.models import User


class Command(BaseCommand):
    """Заполнение Базы данных."""

    def handle(self, *args, **kwargs):

        # Владелецы данных
        user1 = User.objects.get(email="igor@sky.pro")
        user2 = User.objects.get(email="ivan@sky.pro")
        user3 = User.objects.get(email="irina@sky.pro")

        # Привычки user1
        enjoy_habit1 = Habit.objects.create(
            name="Полистать Тик-Ток",
            owner=user1,
            place="Не важно",
            start_time="12:00",
            is_enjoy=True,
            period=1,
            duration=120,
            is_public=True,
        )
        Habit.objects.create(
            name="Позвонить близкому человеку",
            owner=user1,
            place="Не важно",
            start_time="12:00",
            is_enjoy=False,
            period=1,
            duration=120,
            is_public=True,
            related_habit=enjoy_habit1,
        )
        Habit.objects.create(
            name="Глубокое дыхание",
            owner=user1,
            place="Не важно",
            start_time="12:00",
            is_enjoy=False,
            period=1,
            reward="Конфета",
            duration=120,
            is_public=False,
        )

        # Привычки user2
        enjoy_habit2 = Habit.objects.create(
            name="Полистать Шорты Ютюб",
            owner=user2,
            place="Не важно",
            start_time="12:00",
            is_enjoy=True,
            period=2,
            duration=120,
            is_public=True,
        )
        Habit.objects.create(
            name="Посмотреть на звёзды",
            owner=user2,
            place="Не важно",
            start_time="23:00",
            is_enjoy=False,
            period=1,
            duration=120,
            is_public=True,
            related_habit=enjoy_habit2,
        )
        Habit.objects.create(
            name="Наблюдать закат солнца",
            owner=user2,
            place="Не важно",
            start_time="18:00",
            is_enjoy=False,
            period=1,
            reward="Шоколад",
            duration=120,
            is_public=False,
        )

        # Привычки user3
        enjoy_habit3 = Habit.objects.create(
            name="Полистать Телеграм",
            owner=user3,
            place="Не важно",
            start_time="12:00",
            is_enjoy=True,
            period=1,
            duration=120,
            is_public=True,
        )
        Habit.objects.create(
            name="Завтракать в первые полчаса после сна",
            owner=user3,
            place="Дома",
            start_time="7:00",
            is_enjoy=False,
            period=1,
            duration=120,
            is_public=False,
            related_habit=enjoy_habit3,
        )
        Habit.objects.create(
            name="Гулять перед сном",
            owner=user3,
            place="Дома",
            start_time="20:00",
            is_enjoy=False,
            period=1,
            reward="Печенье",
            duration=120,
            is_public=True,
        )
