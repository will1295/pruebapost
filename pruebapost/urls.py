from django.contrib import admin
from django.urls import path
from app_libros import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.inicio),
    path('add_form/',views.get_nombre),
]
