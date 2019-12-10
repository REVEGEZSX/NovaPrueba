from django.db import models

from django.utils.safestring import mark_safe
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Rol (models.Model):
    Tipo_Usuario = models.CharField(max_length=45)
    Estado = models.BooleanField(null=True)
    def __str__ (self):
        return self.Tipo_Usuario

class Usuario (models.Model):
    Nombre_Usuario = models.CharField(max_length=45)
    Contraseña = models.CharField(max_length=45)
    Rol = models.ForeignKey('Rol', on_delete=models.CASCADE)
    Estado = models.BooleanField(null=True)

    def __str__ (self):
        return self.Nombre_Usuario

class Genero (models.Model):
    Tipo_Genero = models.CharField(max_length=45)

    def __str__ (self):
        return self.Tipo_Genero


class Tipo_Profesional (models.Model):
    Especialidad = models.CharField(max_length=45)
    def __str__ (self):
        return self.Especialidad


class Profesional (models.Model):
    Nombre = models.CharField(max_length=45)
    Apellido = models.CharField(max_length=45)
    Identificacion = models.CharField(max_length=45)
    Telefono = models.CharField(max_length=45)
    Email = models.CharField(max_length=45)
    Direccion = models.CharField(max_length=45)
    Estado = models.BooleanField(null=True, default=True)
    Genero = models.ForeignKey('Genero', on_delete=models.CASCADE)
    Foto = models.ImageField('Cargar imagen',upload_to='fotos/', default = 'fotos/profile.png', blank=True, null=True)
    Usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    Tipo_Profesional = models.ForeignKey('Tipo_Profesional', on_delete=models.CASCADE)

    def __str__(self):
        return "{}, {}".format(self.Nombre,self.Apellido, self.Identificacion)
    
    def Mostrar_foto(self):
        if self.Foto:
            return mark_safe('<img src="{0}" width="80" height="90" alt="Foto" style="border-radius: 5px">'.format(self.Foto.url)) #135X140 #<a href="{0}"><img src="{0}" width="100" height="110" alt="Sin foto"></a>
        else:
            return mark_safe('<img src="{% static "fotos/profile.png" %}" width="90" height="70" alt="Usuario sin foto" style="border-radius: 5px"/>')

    Mostrar_foto.short_description = 'Foto'
class Paciente (models.Model):
    Nombre = models.CharField(max_length=45)
    Apellido = models.CharField(max_length=45)
    Identificacion = models.CharField(max_length=45)
    Telefono = models.CharField(max_length=45)
    Email = models.EmailField(max_length=45)
    Direccion = models.CharField(max_length=45)
    Estado = models.BooleanField(null=True, default=True)
    Foto = models.ImageField('Cargar imagen',upload_to='fotos/', default = 'fotos/profile.png', blank=True, null=True)
    Genero = models.ForeignKey('Genero', on_delete=models.CASCADE)
    Usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)

    def __str__(self):
        return "{}, {}".format(self.Nombre,self.Apellido, self.Identificacion)

    def Mostrar_foto(self):
        if self.Foto:
            return mark_safe('<img src="{0}" width="80" height="90" alt="Foto" style="border-radius: 5px">'.format(self.Foto.url)) #135X140 #<a href="{0}"><img src="{0}" width="100" height="110" alt="Sin foto"></a>
        else:
            return mark_safe('<img src="{% static "fotos/profile.png" %}" width="90" height="70" alt="Usuario sin foto" style="border-radius: 5px"/>')

    Mostrar_foto.short_description = 'Foto'
    
class Administrador (models.Model):
    Nombre = models.CharField(max_length=45)
    Apellido = models.CharField(max_length=45)
    Identificacion = models.CharField(max_length=45)
    Telefono = models.CharField(max_length=45)
    Email = models.EmailField(max_length=45)
    Direccion = models.CharField(max_length=45)
    Estado = models.BooleanField(null=True, default=True)
    Foto = models.ImageField('Cargar imagen',upload_to='fotos/', default = 'fotos/profile.png', blank=True, null=True)
    Genero = models.ForeignKey('Genero', on_delete=models.CASCADE)
    Usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)


    def __str__(self):
        return "{}, {}".format(self.Nombre,self.Apellido, self.Identificacion)

    def Mostrar_foto(self):
        if self.Foto:
            return mark_safe('<img src="{0}" width="80" height="90" alt="Foto" style="border-radius: 5px">'.format(self.Foto.url)) #135X140 #<a href="{0}"><img src="{0}" width="100" height="110" alt="Sin foto"></a>
        else:
            return mark_safe('<img src="{% static "fotos/profile.png" %}" width="90" height="70" alt="Usuario sin foto" style="border-radius: 5px"/>')

    Mostrar_foto.short_description = 'Foto'
    

class Registrar_Cita (models.Model):
    Fecha = models.DateField()
    Hora = models.TimeField()
    Descripcion = models.CharField(max_length=200)
    Estado = models.BooleanField(null=True, default=True)
    Paciente = models.ForeignKey('Paciente', on_delete=models.CASCADE)
    Profesional = models.ForeignKey('Profesional', on_delete=models.CASCADE)

class Consulta (models.Model):
    Fecha = models.DateField()
    Hora = models.DateTimeField()
    Descripcion = models.CharField(max_length=1000)
    Estado = models.BooleanField(null=True, default=True)
    Cita = models.ForeignKey('Registrar_Cita', on_delete=models.CASCADE)

class Detalle_Enfermedad(models.Model):
    Tipo = models.CharField(max_length=45)
    Estado = models.BooleanField(null=True, default=True)

class Enfermedad (models.Model):
    Gravedad = models.CharField(max_length=45)
    Nombre = models.CharField(max_length=45)
    Estado = models.BooleanField(null=True, default=True)
    Consulta = models.ForeignKey('Consulta', on_delete=models.CASCADE)
    Detalle_Enfermedad = models.ForeignKey('Detalle_Enfermedad', on_delete=models.CASCADE)

