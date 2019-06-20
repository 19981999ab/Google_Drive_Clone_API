from rest_framework import permissions

SAFE_METHODS = ("GET", "POST")


class IsOwnerorReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        print(view.kwargs)
        try:
            user_profile = Profile.objects.get(pk=view.kwargs["pk"])
        except:
            return False

        if request.user == user_profile:
            return True

        return False
