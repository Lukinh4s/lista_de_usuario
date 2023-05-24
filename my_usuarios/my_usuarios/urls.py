from django.contrib import admin
from django.urls import path, include
from usuarios.views import  UserCreateAPIView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('users', UserCreateAPIView, basename='users')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
