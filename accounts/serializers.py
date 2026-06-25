from rest_framework import serializers
from .models import User, UserSettings, Notification


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'role',
            'phone'
        ]

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password'],
            role=validated_data.get('role', 'client'),
            phone=validated_data.get('phone')
        )
        return user


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'phone',
            'role',
            'profile_image',
            'address',
            'created_at'
        ]


# =========================
# ⚙️ USER SETTINGS
# =========================

class UserSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSettings
        fields = [
            'id',
            'user',
            'email_notifications',
            'push_notifications',
            'dark_mode',
            'language',
            'updated_at'
        ]


# =========================
# 🔔 NOTIFICATIONS
# =========================

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = [
            'id',
            'user',
            'title',
            'message',
            'notification_type',
            'is_read',
            'created_at'
        ]

