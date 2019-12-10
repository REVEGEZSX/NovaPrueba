from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import UpdateView,CreateView,DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from .models import *

from django.views import View
from django.shortcuts import redirect

def NovAtention (request):
    return render(request,"apps/NovAtention.html")

def InicioSesion (request):
    return render(request,"apps/iniciosesion.html")

#ListView

class PacienteList(ListView):
    model = Paciente
    template_name = 'apps/informePacientes.html'



class CitasList(ListView):
    model = Registrar_Cita
    template_name = 'apps/InformeCitas.html'

class IniciarConsultaList(ListView):
    model = Consulta
    template_name = 'apps/IniciarConsulta.html'


class EmpleadosList(ListView):
    model = Profesional
    template_name = 'apps/InformeEmpleados.html'

#CreateView

class Registrar_CitaCreate(CreateView):
    model = Registrar_Cita
    fields = ['Fecha','Hora','Descripcion','Paciente','Profesional']
    template_name = 'apps/RegistrarCita.html'
    success_url = reverse_lazy('inicio')

class Registrar_Usuario(CreateView):
    model = Usuario
    fields = ['Nombre_Usuario','Contraseña','Rol']
    template_name = 'apps/Usuario.html'
    success_url = reverse_lazy('inicio')

class RegistrarPacienteCreate(CreateView):
    model = Paciente
    fields = ['Nombre','Apellido','Identificacion','Telefono','Email','Direccion','Genero','Usuario','Foto']
    template_name = 'apps/RegistrarPacientes.html'
    success_url = reverse_lazy('Registrar_paciente')

class RegistrarEmpleadoCreate(CreateView):
    model = Profesional
    fields = ['Nombre','Apellido','Identificacion','Telefono','Email','Direccion','Genero','Usuario','Tipo_Profesional','Foto']
    template_name = 'apps/RegistrarEmpleado.html'
    success_url = reverse_lazy('inicio')

#UpdateView

class PacienteUpdate(UpdateView):
    model = Paciente 
    fields = ['Nombre','Apellido','Identificacion','Telefono','Email','Direccion','Genero','Usuario','Foto']
    template_name = 'apps/ActualizarPaciente.html'
    success_url = reverse_lazy('info_paciente')

class EmpleadoUpdate(UpdateView):
    model = Profesional 
    fields = ['Nombre','Apellido','Identificacion','Telefono','Email','Direccion','Genero','Usuario','Tipo_Profesional','Foto']
    template_name = 'apps/ActualizarEmpleado.html'
    success_url = reverse_lazy('Informe_empleados')

class EliminarPacienteList(View):
     def get(self, request, pk):
        pass
         

     def post(self, request, pk):
         print("Estoy en el post")
         p = Paciente.objects.get(pk=pk)
         p.Estado = False
         p.save()
         return redirect('info_paciente')

class TerminarConsultaView(View):
     def get(self, request, pk):
        pass
         

     def post(self, request, pk):
         print("Estoy en el post")
         p = Registrar_Cita.objects.get(pk=pk)
         p.Estado = False
         p.save()
         return redirect('ListaConsulta')

class ConsultaView(ListView):
    model = Registrar_Cita
    template_name = 'apps/ConsultasPendientes.html'


class EliminarEmpleadoList(View):
     def get(self, request, pk):
        pass
         

     def post(self, request, pk):
         print("Estoy en el post")
         j = Profesional.objects.get(pk=pk)
         j.Estado = False
         j.save()
         return redirect('Informe_empleados')


