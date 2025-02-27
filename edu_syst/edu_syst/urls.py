from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('schools.urls')),
    path('admin/', admin.site.urls),
]