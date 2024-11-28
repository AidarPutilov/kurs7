from rest_framework import serializers
# from materials.validators import validate_youtube_link

from main.models import Habit


class HabitSerializer(serializers.ModelSerializer):
    """Сериализатор для Habit."""

    class Meta:
        model = Habit
        fields = (
            "id",
            "name",
            "owner",
            "place",
            "start_time",
            "is_enjoy",
            "related_habit",
            "period",
            "reward",
            "duration",
            "is_public",
        )


class HabitDetailSerializer(serializers.ModelSerializer):
    """Сериализатор для RETRIVE Habit."""

    class Meta:
        model = Habit
        fields = "__all__"
