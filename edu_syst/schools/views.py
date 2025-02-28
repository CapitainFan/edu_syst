from rest_framework import viewsets
from .models import User, Teacher, Student, School, Form
from .serializers import UserSerializer, TeacherSerializer, StudentSerializer, SchoolSerializer, FormSerializer
from .permissions import IsAdminOrReadOnly, IsAdminOrBelongsToUser, IsStudentOrTeacherOnlyRead
from rest_framework import generics, permissions
from .serializers import UserRegistrationSerializer
from rest_framework.decorators import action


class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]  # [IsAdminOrBelongsToUser]


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [permissions.AllowAny]  # [IsAdminOrBelongsToUser]


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.AllowAny]  # [IsAdminOrBelongsToUser]


class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    permission_classes = [permissions.AllowAny]  # [IsAdminOrReadOnly]

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
    permission_classes = [permissions.AllowAny]  # [IsStudentOrTeacherOnlyRead]

    @action(detail=True, methods=['get'])
    def get_list_of_students(self, request, pk=None):
        form = self.get_object()
        students = form.get_all_students()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)


'''
http://127.0.0.1:8000/schools/1/get_list_of_students/

* Добавить функцию которая при создаии Form, 
автоматически добавляла связь OneToOne (class_teacher)
для класса Teacher в поле form


* Разобраться с правами доступа 


* Добавить логин


* Добавить эндпоинты на отображение всех учеников/учителей для клссов/школ

'''