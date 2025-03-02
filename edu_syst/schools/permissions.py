from rest_framework import permissions

class IsAdminOrBelongsTo(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff or request.user.is_admin:
            return True
        return obj.user == request.user
    

class IsAdminOrBelongsToUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff or request.user.is_admin:
            return True
        return obj == request.user


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_superuser)


class IsStudentOrTeacher(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True

        is_student = obj.students.filter(user=request.user).exists()
        is_teacher = obj.class_teacher.user == request.user

        return is_student or is_teacher
