from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import School, Form, Teacher, Student
from django.contrib.auth.models import User


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'city', 'amount_of_students', 'amount_of_teachers')
    list_filter = ('country', 'city')
    search_fields = ('name', 'city', 'country')
    readonly_fields = ('get_all_students', 'get_all_teachers', 'get_all_forms')

    def get_all_students(self, obj):
        return ", ".join([str(student) for student in obj.get_all_students()])
    get_all_students.short_description = 'Students'

    def get_all_teachers(self, obj):
        return ", ".join([str(teacher) for teacher in obj.get_all_teachers()])
    get_all_teachers.short_description = 'Teachers'

    def get_all_forms(self, obj):
        return ", ".join([str(form) for form in obj.get_all_forms()])
    get_all_forms.short_description = 'Forms'


@admin.register(Form)
class FormAdmin(admin.ModelAdmin):
    list_display = ('grade', 'letter', 'school', 'class_teacher')
    list_filter = ('school', 'grade')
    search_fields = ('grade', 'letter', 'school__name')
    raw_id_fields = ('class_teacher',)

    def get_all_students(self, obj):
        return ", ".join([str(student) for student in obj.get_all_students()])
    get_all_students.short_description = 'Students'


class TeacherAdmin(UserAdmin):
    list_display = ('username', 'last_name', 'first_name', 'middle_name', 'subject', 'school')
    list_filter = ('school', 'subject')
    search_fields = ('last_name', 'first_name', 'middle_name', 'subject', 'school__name')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('last_name', 'first_name', 'middle_name', 'date_of_birth', 'subject', 'school', 'form')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    filter_horizontal = ('groups', 'user_permissions')


class StudentAdmin(UserAdmin):
    list_display = ('username', 'last_name', 'first_name', 'middle_name', 'form', 'school')
    list_filter = ('school', 'form')
    search_fields = ('last_name', 'first_name', 'middle_name', 'form__grade', 'form__letter', 'school__name')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('last_name', 'first_name', 'middle_name', 'date_of_birth', 'form', 'school')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    filter_horizontal = ('groups', 'user_permissions')


admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.unregister(User)