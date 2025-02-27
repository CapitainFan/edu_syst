from .models import Student, Teacher, School, Form
from .serializers import SchoolSerializer, FormSerializer, TeacherSerializer, StudentSerializer
from rest_framework import permissions
from rest_framework import renderers
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from .permissions import IsAdminOrReadOnly, IsStudentOrTeacherOnlyRead, IsAdminOrBelongsToUser
from rest_framework.permissions import (SAFE_METHODS, AllowAny,
                                        IsAuthenticated, IsAdminUser,
                                        IsAuthenticatedOrReadOnly)


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAdminOrBelongsToUser]


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAdminOrBelongsToUser]


class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    permission_classes = [IsAdminOrReadOnly]

    # /schools/{pk}/get_list_of_students/
    @action(detail=True, methods=['get'])
    def get_list_of_students(self, request, pk=None):
        school = self.get_object()
        students = school.get_all_students()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)


class FormViewSet(viewsets.ModelViewSet):
    queryset = Form.objects.all()
    serializer_class = FormSerializer
    permission_classes = [IsStudentOrTeacherOnlyRead]



'''
http://127.0.0.1:8000/schools/1/get_list_of_students/

* Добавить функцию которая при создаии Form, 
автоматически добавляла связь OneToOne (class_teacher)
для класса Teacher в поле form


* Разобраться с правами доступа 


* Добавить логин и ригистрацию


* Добавить эндпоинты на отображение всех учеников/учителей для клссов/школ

'''