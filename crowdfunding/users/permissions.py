from rest_framework import permissions
from .models import CustomUser


class IsOwnerOrReadOnly(permissions.BasePermission):
  def has_permission(self, request, view):
    if request.method in permissions.SAFE_METHODS:
      return True
    return self.id == request.user.id
  
class IsSuperUser(permissions.IsAdminUser):
  def has_permission(self, request, view):
    return bool(request.user and request.user.is_superuser)
  

class IsSuperUserOrCurrentUser(permissions.BasePermission):
  def has_permission(self, request, view):
    # Only allow currently logged in user to view their own detail
    isCurrentUser = request.user.id == int(view.kwargs.get('pk'))
    return isCurrentUser or request.user.is_superuser