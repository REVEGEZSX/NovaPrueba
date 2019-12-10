from django.contrib import admin
from django.urls import path
from .views import *


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   path('', NovAtention, name ='inicio'),
   path('Iniciar/', InicioSesion, name ='iniciar'),
   path('iniciasesion/',LoginView.as_view(template_name='accounts/login.html'), name='login' ),
   path('logoutsesion/',LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
   #Informes
    path('InformePacientes/', PacienteList.as_view(), name ='info_paciente'),
    path('InformeCitas/', CitasList.as_view(), name ='info_citas'),
    path('InformeEmpleados/', EmpleadosList.as_view(), name ='Informe_empleados'),
    path('Consulta/', IniciarConsultaList.as_view(), name ='Consulta'),
    path('Lista/Consulta/', ConsultaView.as_view(), name ='ListaConsulta'),

    path('Usuario', Registrar_Usuario.as_view(), name ='Usuario'),

    #Poner en estado false
    path('Empleado/Eliminar/<int:pk>', EliminarEmpleadoList.as_view(), name ='eliminar_Empleado'),
    path('Paciente/Eliminar/<int:pk>', EliminarPacienteList.as_view(), name ='eliminar_Paciente'),
    #Registros
    path('RegistroCita/', Registrar_CitaCreate.as_view(), name = 'Registrar_cita'),
    path('RegistroPaciente/', RegistrarPacienteCreate.as_view(), name = 'Registrar_paciente'),
    path('RegistroEmpleados/', RegistrarEmpleadoCreate.as_view(), name = 'Registrar_empleado'),
    #Actualizar
    path('EditarPaciente/<int:pk>', PacienteUpdate.as_view(), name = 'editar_paciente'),
    path('EditarEmpleado/<int:pk>', EmpleadoUpdate.as_view(), name = 'editar_empleado'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
