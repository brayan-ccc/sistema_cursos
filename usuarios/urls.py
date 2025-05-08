from django.urls import path
from .views import dashboard,dashboard_admin,dashboard_profesor


urlpatterns = [
    path('', dashboard,name='dashboard'),
    path('admin-dashboard/', dashboard_admin, name='dashboard_admin'),
    path('profesor-dashboard/', dashboard_admin, name='dashboard_profesor'),
    path('estudiante-dashboard/', dashboard_admin, name='estudiante_admin'),
]
