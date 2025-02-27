from rest_framework import permissions

class IsAdminOrBelongsToUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff or request.user.is_admin:
            return True
        return obj.user == request.user


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_superuser)


class IsStudentOrTeacherOnlyRead(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        elif (request.user in obj.get_all_students()) or (request.user is obj.class_teacher):
            return (request.method in permissions.SAFE_METHODS)
        else:
            return False


class IsStudentOrTeacher(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return (
            request.user in obj.get_all_students()
            or request.user is obj.class_teacher)
