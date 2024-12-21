from django.shortcuts import render, redirect
from .models import Curso
from django.contrib import messages

# Create your views here.

def home(request):
    Cursoslistado = Curso.objects.all()
    messages.success(request, 'Cursos Registrados')
    return render(request, 'index.html', {'cursos': Cursoslistado})

# Agregar Cursos
def registarCurso(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre', '').strip()
        creditos = request.POST.get('creditos', '').strip()
        horas = request.POST.get('horas', '').strip()
        
        if nombre and creditos.isdigit() and horas.isdigit():
            Curso.objects.create(
                nombre=nombre,
                creditos=int(creditos),
                horas=int(horas)
            )
        messages.success(request, 'Curso Registrado')
        return redirect('/')

# Mostrar Cursos que se editaran
    
def editarCurso(request, id):
    curso = Curso.objects.get(id=id)
    messages.success(request, 'Curso a Editar')
    return render(request, 'editarCurso.html', {'curso': curso})

# Editar Cursos

def edicionCurso(request, id):
    if request.method == 'POST':
        nombre = request.POST.get('nombre', '').strip()
        creditos = request.POST.get('creditos', '').strip()
        horas = request.POST.get('horas', '').strip()
        
        curso = Curso.objects.get(id=id)
        curso.nombre = nombre
        curso.creditos = int(creditos)
        curso.horas = int(horas)
        curso.save()
        messages.success(request, 'Curso Editado')
        return redirect('/')
    else:
        curso = Curso.objects.get(id=id)
        return render(request, 'editarCurso.html', {'curso': curso})

   

# Eliminar Cursos

def eliminarCurso(request, id):
    Curso.objects.get(id=id).delete()
    messages.success(request, 'Curso Eliminado')
    return redirect('/')
