
$(document).ready(function(){

    // ocultar todos los div que tengan class "alert" y se encuentren
    // dentro de un elemento cuyo id es "formulario-contacto".
    $("#formulario-contacto span.alert").hide();

    // función encargada de verificar si el valor del parámetro fieldValue
    // es vacío y mostrar o esconder, según corresponda, el mensaje en el
    // div de alerta asociado al campo indicado en el parámetro fieldName.
    function validarCampoVacio(fieldValue, fieldId) {
        
        if (fieldValue.trim().length == 0) {
            $("#"+fieldId).addClass("error-campo-formulario");
            $("label[for='"+fieldId+"'] span.alert").html("El campo no puede ser vacío");
            $("label[for='"+fieldId+"'] span.alert").show();
            $("label[for='"+fieldId+"'] span.alert").fadeOut( 5000 )

            return false;
        } else {
            $("#"+fieldId).removeClass("error-campo-formulario");
            $("label[for='"+fieldId+"'] span.alert").hide();

            return true;
        }
    }

    // asocia en el evento blur del elemento de formulario con id "fieldTipoContacto" la llamada a la
    // función de validar si el campo es vacío.
    $("#fieldTipoContacto").change(function(){
        valorIngresado = $(this).val();
        console.log("No ha seleccionado un tipo de contacto: '"+valorIngresado+"'");

        validarCampoVacio(valorIngresado, "fieldTipoContacto");
    });

    // asocia en el evento blur del elemento de formulario con id "fieldNombre" la llamada a la
    // función de validar si el campo es vacío.
    $("#fieldNombre").blur(function(){
        valorIngresado = $(this).val();
        console.log("El usuario ha dejado el campo nombre con el valor: '"+valorIngresado+"'");

        validarCampoVacio(valorIngresado, "fieldNombre");
    });
   
    // asocia en el evento blur del elemento de formulario con id "fieldEmail" la llamada a la
    // función de validar si el campo es vacío.
    $("#fieldEmail").blur(function(){
        valorIngresado = $(this).val();
        console.log("El usuario ha dejado el campo e-mail con el valor: '"+valorIngresado+"'");

        validarCampoVacio(valorIngresado, "fieldEmail");
    });

    // asocia en el evento blur del elemento de formulario con id "fieldFechaNacimiento" la llamada a la
    // función de validar si el campo es vacío.
    $("#fieldFechaNacimiento").blur(function(){
        valorIngresado = $(this).val();
        console.log("El usuario ha dejado el campo fechaNacimiento con el valor: '"+valorIngresado+"'");

        validarCampoVacio(valorIngresado, "fieldFechaNacimiento");
    });

    // asocia en el evento blur del elemento de formulario con id "fieldRut" la llamada a la
    // función de validar si el campo es vacío.
    $("#fieldRut").blur(function(){
        valorIngresado = $(this).val();
        console.log("El usuario ha dejado el campo RUT vacío: + '"+valorIngresado+"'");

        validarCampoVacio(valorIngresado, "fieldRut");
    });

    // asocia en el evento blur del elemento de formulario con id "fieldComentario" la llamada a la
    // función de validar si el campo es vacío.
    $("#fieldComentario").blur(function(){
        valorIngresado = $(this).val();
        console.log("El usuario ha dejado el campo comentario con el valor: '"+valorIngresado+"'");

        validarCampoVacio(valorIngresado, "fieldComentario");
    });

    $(":submit").click(function(event) {
        error = false;

        $("input, textarea, select").each(function() {
            value = $(this).val();
            fieldId = $(this).attr("id");

            if (!validarCampoVacio(value, fieldId)) {
                error = true;
            }
        })

        if (error) {
            event.preventDefault();
            return false;
        }

        return true;
    })
});


