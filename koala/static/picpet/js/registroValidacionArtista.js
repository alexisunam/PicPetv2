let dataEmails = window.data.emails;
let dataNombresDeUsuario =  window.data2.nombresDeUsuario;
console.log(data);
console.log(dataEmails[0]);
console.log(dataEmails[1]);
console.log(dataNombresDeUsuario[0]);
console.log(dataNombresDeUsuario[1]);

const formulario = document.getElementById("formulario");

const nombre = document.getElementById("nombre");
const apellidoPaterno = document.getElementById("apellidoPaterno");
const apellidoMaterno = document.getElementById("apellidoMaterno");
const nombreUsuario = document.getElementById("nombreUsuario");
const email = document.getElementById("email");
const edad = document.getElementById("edad");
const contrasenia = document.getElementById("contrasenia");
const confirmarContrasenia = document.getElementById("confirmarContrasenia");
const numeroCuenta = document.getElementById("numeroCuenta");
const uploadArchivo = document.getElementById("uploadArchivo");
const terminos = document.getElementById("terminos");

/* const alertSuccess = document.getElementById("alertSuccess"); */
const alertNombre = document.getElementById("alertNombre");
const alertApellidoPaterno = document.getElementById("alertApellidoPaterno");
const alertApellidoMaterno = document.getElementById("alertApellidoMaterno");
const alertNombreUsuario = document.getElementById("alertNombreUsuario");
const alertEmail = document.getElementById("alertEmail");
const alertEdad = document.getElementById("alertEdad");
const alertContrasenia = document.getElementById("alertContrasenia");
const alertConfirmarContrasenia = document.getElementById("alertConfirmarContrasenia");
const alertNumeroCuenta = document.getElementById("alertNumeroCuenta");
const alertUploadArchivo = document.getElementById("alertUploadArchivo");
const alertTerminos = document.getElementById("alertTerminos");

const regNombre = /^[A-Z]+[a-zÀ-ÿ]{1,40}$/;
const regNombreUsuario = /^[a-zA-Z0-9\_\-]{4,16}$/;
const regApellido = /^[A-Z]+[A-Za-zÀ-ÿ\s]{1,40}$/;
const regContrasenia = /^[a-zA-Z]+.{8,30}$/;
const regEmail = /^[a-z0-9]+(\.[_a-z0-9]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,20})$/;
const regEdad = /^[\d]{2,3}$/;
const regNumeroCuenta = /^[\d]{9}$/;

/* const pintarMensajeExito = () => {
    alertSuccess.classList.remove("d-none");
    alertSuccess.textContent = "Registro éxitoso";
}; */

const pintarMensajeError = (errores) => {
    errores.forEach((item) => {
        item.tipo.classList.remove("d-none");
        item.tipo.textContent = item.msg;
    });
};

formulario.addEventListener("submit", (e) => {
    if(validarCampos() == false) {
        e.preventDefault();

        /* alertSuccess.classList.add("d-none"); */
        const errores = [];
    
        // validar nombre
        if (!regNombre.test(nombre.value) || !nombre.value.trim()) {
            nombre.classList.add("is-invalid");
    
            errores.push({
                tipo: alertNombre,
                msg: "Formato no válido campo nombre, solo letras, este debe iniciar con mayuscula",
            });
        
        } else {
            nombre.classList.remove("is-invalid");
            nombre.classList.add("is-valid");
            alertNombre.classList.add("d-none");
        }
    
      //validar apellido paterno
        if (!regApellido.test(apellidoPaterno.value) ||
        !apellidoPaterno.value.trim()) {
            apellidoPaterno.classList.add("is-invalid");
    
            errores.push({
                tipo: alertApellidoPaterno,
                msg: "Campo invalido debe iniciar con una mayuscula, este puede incluir espacios pero no numeros o caracteres especiales",
            });
    
        } else {
            apellidoPaterno.classList.remove("is-invalid");
            apellidoPaterno.classList.add("is-valid");
            alertApellidoPaterno.classList.add("d-none");
        }
    
        //validar apellido Materno
        if (!regApellido.test(apellidoMaterno.value) || !apellidoMaterno.value.trim()) {
        apellidoMaterno.classList.add("is-invalid");
    
            errores.push({
                tipo: alertApellidoMaterno,
                msg: "Campo invalido debe iniciar con una mayuscula, este puede incluir espacios pero no numeros o caracteres especiales",
            });
    
        } else {
            apellidoMaterno.classList.remove("is-invalid");
            apellidoMaterno.classList.add("is-valid");
            alertApellidoMaterno.classList.add("d-none");
        }
    
        // validar nombre de usuario
        if (!regNombreUsuario.test(nombreUsuario.value) || !nombreUsuario.value.trim()) {
            nombreUsuario.classList.add("is-invalid");
    
            errores.push({
                tipo: alertNombreUsuario,
                msg: "Escriba un nombre de usuario válido",
            });

        } else if(dataNombresDeUsuario.includes(nombreUsuario.value) == true) {
            nombreUsuario.classList.add("is-invalid");
    
            errores.push({
                tipo: alertNombreUsuario,
                msg: "Este nombre de usuario ya existe",
            });

        } else {
            nombreUsuario.classList.remove("is-invalid");
            nombreUsuario.classList.add("is-valid");
            alertNombreUsuario.classList.add("d-none");
        }
    
        // validar email
        if (!regEmail.test(email.value) || !email.value.trim()) {
            email.classList.add("is-invalid");
    
            errores.push({
                tipo: alertEmail,
                msg: "Escriba un correo válido",
            });
    
        } else if(dataEmails.includes(email.value) == true){

            email.classList.add("is-invalid");
    
            errores.push({
                tipo: alertEmail,
                msg: "El correo ya esta registrado",
            });

        } else {
            
            email.classList.remove("is-invalid");
            email.classList.add("is-valid");
            alertEmail.classList.add("d-none");  
        }
    
        // validar edad
        if (!regEdad.test(edad.value) || !edad.value.trim()) {
            edad.classList.add("is-invalid");
    
            errores.push({
                tipo: alertEdad,
                msg: "Escriba una edad valida, 10+",
            });
    
        } else {
            edad.classList.remove("is-invalid");
            edad.classList.add("is-valid");
            alertEdad.classList.add("d-none");
        }
    
      // validar contrasenia
        if (!regContrasenia.test(contrasenia.value) || !contrasenia.value.trim()) {
        contrasenia.classList.add("is-invalid");
    
            errores.push({
                tipo: alertContrasenia,
                msg: "Escriba una contraseña valida, minimo 9 caracteres",
            });
        } else {
            contrasenia.classList.remove("is-invalid");
            contrasenia.classList.add("is-valid");
            alertContrasenia.classList.add("d-none");
        }
    
        // validar contrasenia 2
        if (contrasenia.value !== confirmarContrasenia.value || !confirmarContrasenia.value.trim()) {
            confirmarContrasenia.classList.add("is-invalid");
    
            errores.push({
                tipo: alertConfirmarContrasenia,
                msg: "La contraseña no coinciden",
            });
        } else {
            confirmarContrasenia.classList.remove("is-invalid");
            confirmarContrasenia.classList.add("is-valid");
            alertConfirmarContrasenia.classList.add("d-none");
        }
    
        // validar numero de cuenta
        if (!regNumeroCuenta.test(numeroCuenta.value) || !numeroCuenta.value.trim()) {
            numeroCuenta.classList.add("is-invalid");
        
                errores.push({
                    tipo: alertNumeroCuenta,
                    msg: "Escriba un numero de cuenta valido, debe ser de 9 caracteres",
                });
        } else {
                numeroCuenta.classList.remove("is-invalid");
                numeroCuenta.classList.add("is-valid");
                alertNumeroCuenta.classList.add("d-none");
        }

        // validar Archivo
        if (!uploadArchivo.value) {
            uploadArchivo.classList.add("is-invalid");
        
                errores.push({
                    tipo: alertUploadArchivo,
                    msg: "Debe seleccionar un archivo",
                });
        } else {
                uploadArchivo.classList.remove("is-invalid");
                uploadArchivo.classList.add("is-valid");
                alertUploadArchivo.classList.add("d-none");
        }

        // validar terminos
        if (terminos.checked == false) {
            terminos.classList.add("is-invalid");
    
            errores.push({
                tipo: alertTerminos,
                msg: "Debe aceptar los terminos y condiciones",
            });
    
        } else {
            terminos.classList.remove("is-invalid");
            terminos.classList.add("is-valid");
            alertTerminos.classList.add("d-none");
        }

        if (errores.length !== 0) {
            pintarMensajeError(errores);
            return;
        }
        console.log(validarCampos());
    }
        console.log("Formulario enviado con éxito");
        /* console.log("validarCampos()");
        pintarMensajeExito(); */
});



function validarCampos() {
    if(!regNombre.test(nombre.value) || !nombre.value.trim() || !regApellido.test(apellidoPaterno.value) ||
    !apellidoPaterno.value.trim() || !regApellido.test(apellidoMaterno.value) || !apellidoMaterno.value.trim() ||
    !regNombreUsuario.test(nombreUsuario.value) || !nombreUsuario.value.trim() || !regEmail.test(email.value) ||
    !email.value.trim() || !regEdad.test(edad.value) || !edad.value.trim() || !regContrasenia.test(contrasenia.value) ||
    !contrasenia.value.trim() || !regContrasenia.test(confirmarContrasenia.value) || !confirmarContrasenia.value.trim() ||
    terminos.checked == false || dataEmails.includes(email.value) == true || dataNombresDeUsuario.includes(nombreUsuario.value) == true || !regNumeroCuenta.test(numeroCuenta.value) || !numeroCuenta.value.trim() || !uploadArchivo.value) {
        return false;
    } else {
        return true;
    }
}