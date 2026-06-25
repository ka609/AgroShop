from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Delivery
from .serializers import DeliverySerializer


class DeliveryViewSet(viewsets.ModelViewSet):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.role == 'client':
            return self.queryset.filter(order__client=user)

        if user.role == 'producteur':
            return self.queryset.filter(order__items__product__producer=user).distinct()

        return self.queryset