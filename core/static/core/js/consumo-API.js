$( document ).ready(function() {
});

window.onload = function() {
    
      // Consulta fecha de hoy

      var fecha = Date();

      let date = new Date();
      
        let day = date.getDate();

        if(day < 10){
            day = '0' + day;
        }

        let month = date.getMonth() + 1;

        if(month < 10){
            month = '0' + month;
        }

        let year = date.getFullYear();
        var fechafinal;

        fechafinal = day + '-' + month + '-' +year;
    

        console.log(fechafinal);

      // API consulta dolar

      $.getJSON('https://mindicador.cl/api/dolar/' + fechafinal, function(data) {
        console.log(fechafinal)
        $("<p/>", {
            html: 'Indicadores Económicos del dia de hoy: El valor actual del Dólar Observado es $' + data.serie[0].valor + ' Fecha Ultima Actualización ' + data.serie[0].fecha
        }).appendTo(".valorDolar");
    }).fail(function() {
        console.log('Error al consumir la API!');
    }); 
    
    //Cargamos la lista de proveedores
    if($('#tab2Test').length > 0){
        $.getJSON('http://127.0.0.1:8000/api/proveedores_lista', function(data) {
            var html = '';
            var i;
            for (i = 0; i < data.length; i++) {
            html += '<tr>' +
                '<td>' + data[i].rut + '</td>' +
                '<td>' + data[i].nombre + '</td>' +
                '<td>' + data[i].telefono + '</td>' +
                '<td>' + data[i].direccion + '</td>' +
                '<td>' + data[i].email + '</td>' +
                '<td>' + data[i].pais + '</td>' +
                '<td>' + data[i].password + '</td>' +
                '<td>' + data[i].moneda + '</td>' +
                '<td><a href="/form-proveedores-mod/' + data[i].rut + '" class="btn btn-info btn-sa">Modificar</a></td>' +
                '<td><a href="/form-proveedores-del/' + data[i].rut + '" class="btn btn-danger btn-sa">Eliminar</a></td>' +
                '</tr>';
            }
            $('#tab2Test tbody').html(html);

            }).fail(function() {
            console.log('Error al consumir la API!');
        });
    }

  }

