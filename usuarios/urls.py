from django.urls import path
from .views import (
    dashboard, dashboard_admin, dashboard_profesor,
    dashboard_estudiante, ver_curso_profesor, panel_lunoz
)

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('admin-dashboard/', dashboard_admin, name='dashboard_admin'),
    path('profesor-dashboard/', dashboard_profesor, name='dashboard_profesor'),
    path('estudiante-dashboard/', dashboard_estudiante, name='dashboard_estudiante'),
    path('curso/<int:curso_id>/profesor/', ver_curso_profesor, name='ver_curso_profesor'),
    path('lunoz/', panel_lunoz, name='panel_lunoz'), # Url de prueba
]
