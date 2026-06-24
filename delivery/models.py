from django.db import models
from orders.models import Order
import uuid


class Delivery(models.Model):

    TYPE_CHOICES = (
        ('pickup', 'Retrait à la ferme-école'),
        ('home', 'Livraison à domicile'),
    )

    STATUS_CHOICES = (
        ('pending', 'En attente'),
        ('preparing', 'Préparation'),
        ('ready', 'Prête au retrait'),
        ('in_transit', 'En cours de livraison'),
        ('delivered', 'Livrée'),
    )

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    order = models.OneToOneField(
        Order,
        on_delete=models.CASCADE,
        related_name='delivery'
    )

    delivery_type = models.CharField(
        max_length=20,
        choices=TYPE_CHOICES
    )

    delivery_address = models.TextField(
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    pickup_date = models.DateTimeField(
        blank=True,
        null=True
    )

    delivered_at = models.DateTimeField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"Livraison {self.order.id}"