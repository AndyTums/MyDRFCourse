from rest_framework.viewsets import ModelViewSet

from habit.models import Habit
from habit.paginations import HabitPagination
from habit.serializer import HabitSerializer


class HabitViewSet(ModelViewSet):
    """ViewSet для модели HABIT"""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    pagination_class = HabitPagination
