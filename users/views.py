from rest_framework.viewsets import ModelViewSet
from users.models import User

from users.serializer import UserSerializer
from rest_framework.permissions import IsAuthenticated


class UserViewSet(ModelViewSet):
    """ViewSet для модели USER"""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        """ Хэширование пароля при создании """

        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()
