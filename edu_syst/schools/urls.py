from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SchoolViewSet, StudentViewSet, TeacherViewSet, FormViewSet

router = DefaultRouter()
router.register(r'schools', SchoolViewSet, basename='schools')
router.register(r'students', StudentViewSet, basename='schstudentools')
router.register(r'teachers', TeacherViewSet, basename='teachers')
router.register(r'forms', FormViewSet, basename='forms')


urlpatterns = [
    path('', include(router.urls)),
]
