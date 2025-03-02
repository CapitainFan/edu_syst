from rest_framework import viewsets
from .models import User, Teacher, Student, School, Form
from .serializers import UserSerializer, TeacherSerializer, StudentSerializer, SchoolSerializer, FormSerializer
from .permissions import IsAdminOrReadOnly, IsAdminOrBelongsToUser, IsStudentOrTeacher, IsAdminOrBelongsTo
from rest_framework import generics
from rest_framework.permissions import (SAFE_METHODS, AllowAny,
                                        IsAuthenticated, IsAdminUser,
                                        IsAuthenticatedOrReadOnly)
from .serializers import UserRegistrationSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminOrBelongsToUser]


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAdminOrBelongsTo]


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAdminOrBelongsTo]


class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    permission_classes = [IsAdminOrReadOnly]

    @action(detail=True, methods=['get'])
    def get_list_of_students(self, request, pk=None):
        school = self.get_object()
        students = school.get_all_students()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def get_list_of_forms(self, request, pk=None):
        school = self.get_object()
        forms = school.get_all_forms()
        serializer = FormSerializer(forms, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def get_list_of_teachers(self, request, pk=None):
        school = self.get_object()
        teachers = school.get_all_teachers()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)


class FormViewSet(viewsets.ModelViewSet):
    queryset = Form.objects.all()
    serializer_class = FormSerializer
    permission_classes = [IsStudentOrTeacher]

    @action(detail=True, methods=['get'])
    def get_list_of_students(self, request, pk=None):
        form = self.get_object()
        students = form.get_all_students()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
