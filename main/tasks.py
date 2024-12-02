from datetime import timedelta

from celery import shared_task
from django.utils import timezone

from main.models import Habit
from main.services import send_telegram_message


@shared_task
def send_telegram_reminder():
    """Фоновая задача, отправляет сообщение в Телеграм."""

    habits = Habit.objects.all()
    current_time = timezone.now()

    for habit in habits:
        tg_chat_id = habit.owner.tg_chat_id
        if tg_chat_id and not habit.is_enjoy:

            flag = False
            if not habit.send_time:
                flag = True
            elif habit.send_time < current_time:
                flag = True

            if flag:
                message = (f"Задание на сегодня: {habit.name},"
                           f" место: {habit.place},"
                           f" время: {habit.start_time}")
                if habit.reward:
                    message += f"\nЗа выполнение: {habit.reward}"
                if habit.related_habit:
                    message += (f"\nЗа выполнение: {habit.related_habit},"
                                f" место: {habit.related_habit.place},"
                                f" время: {habit.related_habit.start_time}")
                send_telegram_message(tg_chat_id, message)
                habit.send_time = current_time + timedelta(days=habit.period)
                habit.save()
