from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from config.settings import AUTH_USER_MODEL


class Habit(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="название привычки",
    )
    owner = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="автор",
        null=True,
        blank=True,
    )
    place = models.CharField(
        max_length=50,
        verbose_name="место выполнения",
    )
    start_time = models.TimeField(
        auto_now=False,
        verbose_name="время начала выполнения"
    )
    is_enjoy = models.BooleanField(
        default=False,
        verbose_name="приятная привычка",
    )
    related_habit = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        verbose_name="связанная привычка",
        related_name="habits",
        null=True,
        blank=True,
    )
    period = models.PositiveSmallIntegerField(
        verbose_name="периодичность (дни)",
        default=1,
        validators=[MaxValueValidator(7), MinValueValidator(1)],
    )
    reward = models.CharField(
        max_length=50,
        verbose_name="вознаграждение",
    )
    duration = models.PositiveSmallIntegerField(
        verbose_name="время выполнения (с)",
        default=120,
        validators=[MaxValueValidator(120)],
    )
    is_public = models.BooleanField(
        default=False,
        verbose_name="публичная привычка",
    )
