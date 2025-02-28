from rest_framework import serializers
from .models import User, Teacher, Student, School, Form
from django.contrib.auth import get_user_model

User = get_user_model()


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    school_id = serializers.PrimaryKeyRelatedField(
        queryset=School.objects.all(),
        required=False,  # Поле необязательное
        allow_null=True  # Разрешить NULL
    )
    form_id = serializers.PrimaryKeyRelatedField(
        queryset=Form.objects.all(),
        required=False,  # Поле необязательное
        allow_null=True  # Разрешить NULL
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'user_type', 'school_id', 'form_id')

    def create(self, validated_data):
        user_type = validated_data.pop('user_type')
        school = validated_data.pop('school_id', None)  # Если поле не передано, будет None
        form = validated_data.pop('form_id', None)     # Если поле не передано, будет None

        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            user_type=user_type
        )

        if user_type == 'student':
            Student.objects.create(
                user=user,
                last_name='',  # Заполните эти поля по необходимости
                first_name='',
                middle_name='',
                school=school,  # Может быть None
                form=form      # Может быть None
            )
        elif user_type == 'teacher':
            Teacher.objects.create(
                user=user,
                last_name='',
                first_name='',
                middle_name='',
                subject='',
                school=school  # Может быть None
            )

        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'user_type')


class TeacherSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Teacher
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Student
        fields = '__all__'


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'


class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = '__all__'
