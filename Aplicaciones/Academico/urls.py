from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('agregarCurso/', views.registarCurso),
    path('editarCurso/<int:id>/', views.editarCurso),
    path('edicionCurso/<int:id>/', views.edicionCurso, name='edicionCurso'),  # Asegúrate de agregar el nombre
    path('eliminarCurso/<int:id>/', views.eliminarCurso),
]
