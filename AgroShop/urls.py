from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from accounts.views import RegisterView, LogoutView, UserViewSet, UserSettingsViewSet, NotificationViewSet
from products.views import CategoryViewSet, ProductViewSet
from orders.views import OrderViewSet, OrderItemViewSet
from payments.views import PaymentViewSet
from delivery.views import DeliveryViewSet

router = DefaultRouter()

router.register('users', UserViewSet, basename='users')
router.register('settings', UserSettingsViewSet, basename='settings')
router.register('notifications', NotificationViewSet, basename='notifications')

router.register('categories', CategoryViewSet, basename='categories')
router.register('products', ProductViewSet, basename='products')

router.register('orders', OrderViewSet, basename='orders')
router.register('order-items', OrderItemViewSet, basename='order-items')

router.register('payments', PaymentViewSet, basename='payments')
router.register('deliveries', DeliveryViewSet, basename='deliveries')

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include(router.urls)),

    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/logout/', LogoutView.as_view(), name='logout'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]