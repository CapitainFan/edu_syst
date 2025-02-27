from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SchoolViewSet, StudentViewSet, TeacherViewSet, FormViewSet, UserViewSet
from .views import UserRegistrationView

router = DefaultRouter()
router.register(r'schools', SchoolViewSet, basename='schools')
router.register(r'students', StudentViewSet, basename='schstudentools')
router.register(r'teachers', TeacherViewSet, basename='teachers')
router.register(r'forms', FormViewSet, basename='forms')
router.register(r'users', UserViewSet, basename='users')


urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('', include(router.urls)),
]
