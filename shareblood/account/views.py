from rest_framework import viewsets

from rest_framework import permissions
from rest_framework.permissions import AllowAny

from .models import CustomAccount
from .serializers import CustomAccountSerializer


class IsStaffOrTargetUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return view.action == 'retrieve' or request.user.is_staff

    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or obj == request.user


class AccountView(viewsets.ModelViewSet):
    serializer_class = CustomAccountSerializer
    model = CustomAccount

    def get_permissions(self):
        return (AllowAny() if self.request.method == 'POST'
                else IsStaffOrTargetUser()),

    def get_queryset(self):
        return CustomAccount.objects.all()
