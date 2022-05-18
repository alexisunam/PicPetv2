from django.shortcuts import render
from django.http import HttpResponse
""" from django.forms import modelform_factory """
from picpet.models import Persona




# Create your views here.
def home(request):
    return render(request, 'home.html')

def iniciarSesion(request):
    return render(request, 'login.html')

def validarSesion(request):
    if(request.method == 'POST'):
        email = request.POST['email']
        password = request.POST['contrasenia']
        emailPersona = Persona.objects.get(email=email)
        pswPersona = emailPersona.contrasenia
        if(pswPersona == password):
            mensaje = "Inicio de sesion exitoso"
            return render(request, 'validarSesion.html', {'mensaje' : mensaje})
        else:
            mensaje = "Inicio de sesion fracasado"
            return render(request, 'validarSesion.html', {'mensaje' : mensaje})
    else:
        print("error primer if")
        return render(request, 'login.html')

def cuentas(request):
    return render(request, 'cuentas.html')

def registrarArtista(request):
    return render(request, 'registrarArtista.html')

def registrarPersona(request):
    return render(request, 'registrarPersona.html')


def insertarPersona(request):
    if(request.method == 'POST'):
        
        personaNueva = Persona(nombre=request.POST['nombre'], apellidoPaterno=request.POST['apellidoPaterno'], apellidoMaterno=request.POST['apellidoMaterno'], nombreUsuario=request.POST['nombreUsuario'], email=request.POST['email'], edad=request.POST['edad'], contrasenia=request.POST['contrasenia'])
        if personaNueva.save() == True:
            personaNueva.save()
            return render(request, 'registrarPersona.html')
        else:
            print("NO se guardo")
            return render(request, 'registrarPersona.html')
    else:
        return render(request, 'registrarPersona.html')
    
def readPersonas(request):
    personas = Persona.objects.order_by('nombre')

    return render(request, 'readPersonas.html', {'personas' : personas})