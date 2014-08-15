// var frm = $('#miformulario');
// frm.submit(function () {
//     $.ajax({
//         type: frm.attr('method'),
//         url: frm.attr('action'),
//         data: frm.serialize(),
//         success: function (data) {
//             $('#filaVacia').val('');
//         	$('#listaCursos').html('');
//         	for (var i = 0; i < data.length ; i++) {
//         		$('#listaCursos').append("<tr><td><h5>" + parseInt(i+1) + "</h5></td><td><h5>"+ data[i].fields.nombre + "</h5></td><td><button class='btn btn-primary'>Editar</button> <button class='btn btn-danger'>Eliminar</button></td></tr>");
//             }
//             console.log(data.mensaje);
//         },
//         error: function(data) {
//             console.log("ERROR!!!");
//         }
//     });
//     return false;
// });

var botonCurso = $("#btnCurso");
botonCurso.click(function(){
    var valor = $("#idCurso").val();
    if(valor != ""){
        $("#btnCurso").html("Registrar");
        $("button[name='eliminar']").prop('disabled', false);
    }
});

function editarCurso(idCurso){
    $("button[name='eliminar']").prop('disabled', true);
    $.ajax({
        type: "POST",
        url: idCurso,
        data: {"tipo" : "Editar", 'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()},
        success: function (data) {
            $('#id_nombre').val(data[0].fields.nombre);
            $('#id_descripcion').val(data[0].fields.descripcion);
            $('#idCurso').val(idCurso);
            $('#btnCurso').html('Editar');
        },
        error: function(data) {
            console.log("ERROR!!!");
        }
    });
}

function eliminarCurso(idCurso){
    if (confirm("Desea eliminar el curso?")) {
        $.ajax({
            type: "POST",
            url: idCurso,
            data: {"tipo" : "Eliminar", 'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()},
            success: function (data) {
                $('#listaCursos').html('');
                var html = "";
                for (var i = 0; i < data.length ; i++) {
                    html += "<tr>";
                        html += "<td>";
                            html += "<h5>";
                                html += parseInt(i+1);
                            html += "</h5>";
                        html += "</td>";
                        html += "<td>";
                            html += "<h5>";
                                html += data[i].fields.nombre;
                            html += "</h5>";
                        html += "</td>";
                        html += "<td>";
                            html += "<button class='btn btn-primary' name='editar' onclick='editarCurso(" + data[i].pk + ")'>";
                                html += "Editar";
                            html += "</button> ";
                            html += "<button class='btn btn-danger' name='eliminar' onclick='eliminarCurso(" + data[i].pk + ")'>";
                                html += "Eliminar";
                            html += "</button>";
                        html += "</td>";
                    html += "</tr>";
                }
                $('#listaCursos').append(html);
            },
            error: function(data) {
                console.log("ERROR!!!");
            }
        });
    }
}