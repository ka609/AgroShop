from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Payment
from .serializers import PaymentSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.role == 'client':
            return self.queryset.filter(order__client=user)

        if user.role == 'producteur':
            return self.queryset.filter(order__items__product__producer=user).distinct()

        return self.queryset