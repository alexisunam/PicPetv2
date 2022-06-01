from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=255)
    apellidoPaterno = models.CharField(max_length=255)
    apellidoMaterno = models.CharField(max_length=255)
    nombreUsuario = models.CharField(max_length=20)
    email = models.CharField(max_length=25)
    edad = models.IntegerField()
    tipo = models.CharField(max_length=7, default='Cliente')
    contrasenia = models.CharField(max_length=32)
    
    def __str__(self):
        return f'Persona {self.id} : {self.nombre} {self.apellidoPaterno} {self.apellidoMaterno} {self.nombreUsuario} {self.email} {self.edad} {self.tipo} {self.contrasenia}'

class Documento(models.Model):
    titulo = models.CharField(max_length=255)
    subirArchivo = models.FileField(upload_to="Uploaded Files/")
    dateTimeOfUpload = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'Documento {self.id} : {self.titulo} {self.subirArchivo} {self.dataTimeOfUpload}'

class Artista(Persona):
    numeroCuenta = models.CharField(max_length=9)
    archivo = models.ForeignKey(Documento, on_delete=models.RESTRICT, null=False)
    def __str__(self):
        return f'Artista {self.id} : {self.numeroCuenta}'
    
class Blog(models.Model):
    titulo = models.CharField(max_length=50)
    intro = models.TextField(max_length=60, default='No hay descripcion')
    autor = models.ForeignKey(Artista, on_delete=models.CASCADE, null=False)
    cuerpo = models.CharField(max_length=200)
    subirImagen = models.ImageField(upload_to="Uploaded Images/")
    dateTimeOfUploadImage = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'Blog {self.id} : {self.titulo} {self.autor.nombreUsuario} {self.cuerpo} {self.subirImagen} {self.dateTimeOfUploadImage}'
    