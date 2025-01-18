from django.db import models

from users.models import User


class Habit(models.Model):
    """ Модель Привычки """

    METHOD_CHOICE = [

        ('daily', 'Ежедневная'),
        ('weekly', 'Еженедельная'),
        ('monthly', 'Ежемесячная')
    ]

    title = models.CharField(max_length=100, verbose_name="Название")
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Владелец")
    place = models.CharField(max_length=100, blank=True, null=True, verbose_name="Место выполнения")
    time = models.CharField(max_length=100, blank=True, null=True, verbose_name="Время выполнения")
    action = models.CharField(max_length=100, blank=True, null=True, verbose_name="Действие")
    period = models.CharField(default="daily", choices=METHOD_CHOICE, verbose_name="Переодичность")
    reward = models.CharField(max_length=100, blank=True, null=True, verbose_name="Вознагрождение")
    time_to_do = models.CharField(max_length=50, blank=True, null=True, verbose_name="Время на выполнение")
    is_public = models.BooleanField(default=False, blank=True, null=True, verbose_name="Публичность")

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"

    def __str__(self):
        return f"{self.title if self.title else self.action})"
