from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from numpy import array
""" from django.forms import modelform_factory """
from picpet.models import Persona, Artista, Documento




# Create your views here.

def home(request):
    return render(request, 'home.html')

# -- inicio funcion iniciar sesion --
def iniciarSesion(request):
    return render(request, 'login.html')
# -- fin --

# -- inicio funcion validar sesion--
def validarSesion(request):
    if(request.method == 'POST'):
        persona = Persona.objects.get(email=request.POST['email'])
        
        if(persona.contrasenia == request.POST['contrasenia']):
            if(persona.tipo == "Cliente"):
                #return render(request, 'validarSesion.html', {'mensaje' : mensaje})
                homeArtista = {'borrar' : "", 'menuGestion' : "Mis Compras"}
                return render(request, 'homeUsuario.html', {'persona' : persona, 'homeArtista' : homeArtista})
            else:
                homeArtista = {'borrar' : " d-none", 'menuGestion' : "Mis pedidos"}
                return render(request, 'homeUsuario.html', {'persona' : persona, 'homeArtista' : homeArtista})
        else:
            respuestaValidacion = {'centrar' : "text-center",'clases' : "alert alert-danger mt-2", 'mensaje' : "Contraseña o correo equivocado"}
            #mensaje = "Inicio de sesion fracasado"
            return render(request, 'login.html', {'respuestaValidacion' : respuestaValidacion})
    else:
        print("error primer if")
        return render(request, 'login.html')
# -- fin --

# -- inicio funcion cuentas--
def cuentas(request):
    return render(request, 'cuentas.html')
# -- fin --

# -- inicio funcion registrar artista--
def registrarArtista(request):
    emails, nombresDeUsuario = emailsYusuarios(); #retorna dos arreglos    
        
    print(emails)
    print(nombresDeUsuario)
    return render(request, 'registrarArtista.html', {'emails' : emails, 'nombresDeUsuario' : nombresDeUsuario})
# -- fin --

# -- inicio funcion registrar persona--
def registrarPersona(request):
    
    emails, nombresDeUsuario = emailsYusuarios(); #retorna dos arreglos    
        
    print(emails)
    print(nombresDeUsuario)
    return render(request, 'registrarPersona.html', {'emails' : emails, 'nombresDeUsuario' : nombresDeUsuario})
# -- fin --

# -- inicio funcion insertar persona--
def insertarPersona(request):
    if(request.method == 'POST'):
        
        personaNueva = Persona(nombre=request.POST['nombre'], apellidoPaterno=request.POST['apellidoPaterno'], apellidoMaterno=request.POST['apellidoMaterno'], nombreUsuario=request.POST['nombreUsuario'], email=request.POST['email'], edad=request.POST['edad'], contrasenia=request.POST['contrasenia'])
        respuestaValidacion = {'centrar' : "text-center",'clases' : "alert alert-success mt-2", 'mensaje' : "Se registro correctamente", 'clasesBoton' : "btn btn-primary", 'boton' : "Regresar"}
        
        personaNueva.save()
        print(respuestaValidacion)
        emails, nombresDeUsuario = emailsYusuarios();
        return render(request, 'registrarPersona.html', {'respuestaValidacion' : respuestaValidacion, 'emails' : emails, 'nombresDeUsuario' : nombresDeUsuario})

    else:
        return render(request, 'registrarPersona.html')
# -- fin --

# -- inicio funcio insertar artista--
def insertarArtista(request):
    if(request.method == 'POST'):
        print(request)
        
        documentoTitulo = (request.POST['nombre'] + request.POST['apellidoPaterno'] + request.POST['apellidoMaterno'])
        documentoSubido = request.FILES['uploadArchivo'] 
        documentoNuevo = Documento(titulo=documentoTitulo, subirArchivo=documentoSubido)
        
        if documentoNuevo.titulo == (request.POST['nombre'] + request.POST['apellidoPaterno'] + request.POST['apellidoMaterno']):

            artistaNuevo = Artista( numeroCuenta=request.POST['numeroCuenta'], archivo=documentoNuevo, nombre=request.POST['nombre'], apellidoPaterno=request.POST['apellidoPaterno'], apellidoMaterno=request.POST['apellidoMaterno'], nombreUsuario=request.POST['nombreUsuario'], email=request.POST['email'], edad=request.POST['edad'], tipo="Artista", contrasenia=request.POST['contrasenia'])
        else:
            emails, nombresDeUsuario = emailsYusuarios();
            respuestaValidacion = {'centrar' : "text-center",'clases' : "alert alert-danger mt-2", 'mensaje' : "Hubo un error en el registro", 'clasesBoton' : "", 'boton' : ""}
            return render(request, "registrarArtista.html", {'respuestaValidacion' : respuestaValidacion, 'emails' : emails, 'nombresDeUsuario' : nombresDeUsuario})
                
        if artistaNuevo.numeroCuenta == request.POST['numeroCuenta']:
            
            documentoNuevo.save()
            artistaNuevo.save()
            print("Se logro")
            #files = Documento.objects.all()
            respuestaValidacion = {'centrar' : "text-center",'clases' : "alert alert-success mt-2", 'mensaje' : "Se registro correctamente", 'clasesBoton' : "btn btn-primary", 'boton' : "Regresar"}
            emails, nombresDeUsuario = emailsYusuarios();
            return render(request, 'registrarArtista.html', {'respuestaValidacion' : respuestaValidacion, 'emails' : emails, 'nombresDeUsuario' : nombresDeUsuario})
        else:
            print("tercer validacion fallo")
            emails, nombresDeUsuario = emailsYusuarios();
            respuestaValidacion = {'centrar' : "text-center",'clases' : "alert alert-danger mt-2", 'mensaje' : "Hubo un error en el registro", 'clasesBoton' : "", 'boton' : ""}
            return render(request, "registrarArtista.html", {'respuestaValidacion' : respuestaValidacion, 'emails' : emails, 'nombresDeUsuario' : nombresDeUsuario})
                
    else: 
        """ emails, nombresDeUsuario = emailsYusuarios(); """
        return render(request, 'registrarArtista.html')
# -- fin --

# -- inicio funcion read personas--    
def readPersonas(request):
    personas = Persona.objects.order_by('nombre')

    return render(request, 'readPersonas.html', {'personas' : personas})
# -- fin --


# -- inicio funcion mostra usuario--
def mostrarUsuario(request, id):
    persona = get_object_or_404(Persona, pk=id)
    
    return render(request, 'verDatosUsuario.html' ,{'persona' : persona})
# -- fin --

# -- inicio funcion actualizar usuario--
def actualizarUsuario(request, id):
    persona = get_object_or_404(Persona, pk=id)
    if(request.method == 'POST'):
        persona.nombre = request.POST['nombre']
        persona.apellidoPaterno = request.POST['apellidoPaterno']
        persona.apellidoMaterno = request.POST['apellidoMaterno']
        persona.nombreUsuario = request.POST['nombreUsuario']
        persona.edad = request.POST['edad']
        
        if not request.POST['nuevaContrasenia']:
            persona.save()
        else:
            if(request.POST['nuevaContrasenia'] == request.POST['confirmarContrasenia']):
                persona.contrasenia = request.POST['nuevaContrasenia']
                persona.save()
                

# -- inicio funcion miHome--
def myHome(request, id):
    persona = get_object_or_404(Persona, pk=id)
    if(persona.tipo == "Artista"):
        homeArtista = {'borrar' : " d-none", 'menuGestion' : "Mis pedidos"}
        return render(request, 'homeUsuario.html', {'persona' : persona, 'homeArtista' : homeArtista})
    else:
        homeArtista = {'borrar' : "", 'menuGestion' : "Mis Compras"}
        return render(request, 'homeUsuario.html', {'persona' : persona, 'homeArtista' : homeArtista})    
# -- fin --


# -- inicio funcion emailsYusuarios, regresa dos arreglos--
def emailsYusuarios():
    personas = Persona.objects.all();
    emailsArreglo = list();
    nombresUsuariosArreglo = list();
    for emailPersona in personas:
        emailsArreglo.append(emailPersona.email)
        
    for nombreUsuarioPersona in personas:
        nombresUsuariosArreglo.append(nombreUsuarioPersona.nombreUsuario)
    
    return emailsArreglo, nombresUsuariosArreglo