# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from usuarios.models import Usuario
from notas.models import Nota
from cursos.models import Curso, Inscripcion
from django.shortcuts import get_object_or_404
from django.forms import modelform_factory
from django.forms import ModelForm

# @login_required
# def dashboard(request):
#     if request.user.rol == 'administrador':
#         return render(request, 'dashboard_admin.html')
#     elif request.user.rol == 'profesor':
#         return render(request, 'dashboard_profesor.html')
#     elif request.user.rol == 'estudiante':
#         return render(request, 'dashboard_estudiante.html')
#     else:
#         return redirect('login')

@login_required
def dashboard(request):
    if request.user.rol == 'administrador':
        return redirect('dashboard_admin')
    elif request.user.rol == 'profesor':
        return redirect('dashboard_profesor')
    elif request.user.rol == 'estudiante':
        return redirect('dashboard_estudiante')
    else:
        return redirect('login')

@login_required
def dashboard_admin(request):
    cursos = Curso.objects.all().select_related('profesor')
    profesores = Usuario.objects.filter(rol='profesor')
    data = []

    for curso in cursos:
        estudiantes = Usuario.objects.filter(
            rol='estudiante',
            inscrito__curso=curso
        ).distinct()
        data.append({
            'curso': curso,
            'profesor': curso.profesor,
            'estudiantes': estudiantes
        })

    return render(request, 'dashboard_admin.html', {
        'cursos_info': data,
        'profesores': profesores
    })

# @login_required
# def dashboard_profesor(request):
#     cursos = Curso.objects.filter(profesor=request.user)
#     return render(request, 'dashboard_profesor.html', {'cursos': cursos})


@login_required
def dashboard_profesor(request):
    cursos = Curso.objects.filter(profesor=request.user)

    if request.method == 'POST':
        inscripcion_id = request.POST.get('inscripcion_id')
        nota1 = request.POST.get('nota1')
        nota2 = request.POST.get('nota2')

        inscripcion = get_object_or_404(Inscripcion, id=inscripcion_id, curso__profesor=request.user)

        nota, created = Nota.objects.get_or_create(inscripcion=inscripcion)
        nota.nota1 = nota1
        nota.nota2 = nota2
        nota.save()

        return redirect('dashboard_profesor')

    return render(request, 'dashboard_profesor.html', {
        'cursos': cursos,
    })

@login_required
def ver_curso_profesor(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id, profesor=request.user)
    inscripciones = Inscripcion.objects.filter(curso=curso).select_related('estudiante')
    return render(request, 'curso_profesor.html', {'curso': curso, 'inscripciones': inscripciones})

@login_required
def dashboard_estudiante(request):
    inscripciones = Inscripcion.objects.filter(estudiante=request.user).select_related('curso', 'nota')
    return render(request, 'dashboard_estudiante.html', {'inscripciones': inscripciones})

@login_required
def panel_lunoz(request):
    return render(request, 'pages/index.html')

