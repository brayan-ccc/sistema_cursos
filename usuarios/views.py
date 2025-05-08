from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from cursos.models import Curso, Inscripcion
from usuarios.models import Usuario

# Create your views here.
# Decorador (a esta vista solo puedes entrar si iniciaste sesión)
@login_required
def dashboard(request):
    if request.user.rol == 'administrador':
        return render(request,'dashboard_admin.html')
    elif request.user.rol == 'profesor':
        return render(request,'dashboard_profesor.html')
    elif request.user.rol == 'estudiante':
        return render(request,'dashboard_estudiante.html')
    else:
        return redirect('login')   

@login_required
def dashboard_admin(request):
    cursos = Curso.objects.all()

    profesores = Usuario.objects.filter(rol='profesor')

    data = []

    for curso in cursos:
        estudiantes = Usuario.objects.filter(rol='estudiante',inscrito__curso=curso)
        data.append({
            'curso':curso,
            'profesor':curso.profesor,
            'estudiantes': estudiantes
        })

    return render(request, 'dashboard_admin.html',{ 'cursos_info':data, 'profesores':profesores })



@login_required
def dashboard_profesor(request):
    cursos = Curso.objects.filter(profesor=request.user)
    return render(request, 'dashboard_profesor.html',{'cursos':cursos})

@login_required
def dashboard_estudiante(request):
    inscripciones = Inscripcion.objects.filter(estudiante=request.user).select_related('curso','nota')

    return render(request,'dashboard_estudiante.html',{'inscripciones':inscripciones})
