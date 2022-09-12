
$(document).ready(function() {
    $('#data').DataTable({
            select: 'multi',
            responsive: true,
            autoWidth: false,
            "language": {
            "lengthMenu": "_MENU_ Filas por pagina",
            "zeroRecords": "No tenemos datos - Lo sentimos",
            "info": "Pagina _PAGE_ de _PAGES_   ",
            "infoEmpty": "No hay datos disponibles",
            "infoFiltered": "(se ha filtrado la cantidad maxima de datos)",
            "processing": "Procesando...",
            "search": "Buscar:",
            "select":{
                rows: "  %d filas seleccionadas"
            },

            "paginate": {
                "first": "Primera",
                "last": "Ultima",
                "next": "Siguiente",
                "previous": "Anterior"
            },
        }
        });
    $('#data2').DataTable({
            responsive: true,
            autoWidth: false,
            "language": {
            "lengthMenu": "_MENU_ Filas por pagina",
            "zeroRecords": "No tenemos datos - Lo sentimos",
            "info": "Pagina _PAGE_ de _PAGES_   ",
            "infoEmpty": "No hay datos disponibles",
            "infoFiltered": "(se ha filtrado la cantidad maxima de datos)",
            "processing": "Procesando...",
            "search": "Buscar:",
            "select":{
                rows: "  %d filas seleccionadas"
            },

            "paginate": {
                "first": "Primera",
                "last": "Ultima",
                "next": "Siguiente",
                "previous": "Anterior"
            },
        }
        });

    $(function () {
    $('#data2 tbody').on('click','btn_modal', function () {
        var datos = data2.rows( { selected: True}).data();
        console.log(datos);
    })
})
} );

// $(function () {
//    $('form').on('submit', function (e){
//       e.preventDefault();
//
//       var parameters = new FormData(this);
//       submit_with_ajax(window.location.pathname,'notificacion', 'estas seguro?', parameters, function () {
//          location.href = '{{list_url}}';
//       });
//
//    });
// });

Highcharts.chart('container', {
    chart: {
        type: 'column'
    },
    title: {
        text: 'Uso servicio de comedor por mes'
    },
    subtitle: {
    },
    xAxis: {
        categories: [
            'Ene',
            'Feb',
            'Mar',
            'Abr',
            'May',
            'Jun',
            'Jul',
            'Ago',
            'Sep',
            'Oct',
            'Nov',
            'Dic'
        ],
        crosshair: true
    },
    yAxis: {
        min: 0,
        title: {
            text: 'porcentaje en (KG)'
        }
    },
    tooltip: {
        headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
        pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
            '<td style="padding:0"><b>{point.y:.1f} </b></td></tr>',
        footerFormat: '</table>',
        shared: true,
        useHTML: true
    },
    plotOptions: {
        column: {
            pointPadding: 0.2,
            borderWidth: 0
        }
    },
    series: [{
        name: 'Desperdicios',
        data: [22.6, 19.8, 17.5, 21.4, 32.0, 18.5, 19.0, 19.3, 18.2, 19.5, 21.6, 16.3],
        color: 'tomato'
    }, {
        name: 'Produccion',
        data: [88.9, 76.8, 88.3, 89.4, 78.0, 89.3, 88.0, 78.6, 87.4, 76.2, 89.3, 87.2],
        color: '#93C572'

    }]
});

Highcharts.chart('contGraph', {
    chart: {
        type: 'column'
    },
    title: {
        text: 'Uso servicio de comedor por mes'
    },
    subtitle: {
    },
    xAxis: {
        categories: [
            'Ene',
            'Feb',
            'Mar',
            'Abr',
            'May',
            'Jun',
            'Jul',
            'Ago',
            'Sep',
            'Oct',
            'Nov',
            'Dic'
        ],
        crosshair: true
    },
    yAxis: {
        min: 0,
        title: {
            text: 'porcentaje en (KG)'
        }
    },
    tooltip: {
        headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
        pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
            '<td style="padding:0"><b>{point.y:.1f} </b></td></tr>',
        footerFormat: '</table>',
        shared: true,
        useHTML: true
    },
    plotOptions: {
        column: {
            pointPadding: 0.2,
            borderWidth: 0
        }
    },
    series: [{
        name: 'Asistencias',
        data: [1890, 1920, 1722, 1963, 1899, 1895, 1655, 1959, 1759, 1923, 2001, 1889],
        color: '#48D1CC'
    }, {
        name: 'Retardos',
        data: [88, 76, 88, 89, 78, 89, 88, 78, 87, 76, 89, 87],
        color: '#ffa500'

    }]

});

function seleccion() {
    var  x = document.getElementById("MySeleccion").value;
    var ttest = document.getElementById("djPrueba").innerText;
    var hoolder = 0;
    hoolder = parseInt(ttest);

    if (x == 1){

        document.getElementById("text1").innerHTML = 'arroz: '
        document.getElementById("text2").innerHTML = 'pollo: '
        document.getElementById("text3").innerHTML = 'papa: '
        document.getElementById("inputItem4").hidden = false;
        document.getElementById("text4").innerHTML = 'lenteja: '
        document.getElementById("text5").innerHTML = 'sandia: '

        const button = document.getElementById("btn_aceptar")
        button.disabled = false;

        //Visualizar los objetos

        if (hoolder > 0 && hoolder < 50) {

            document.getElementById("cnt_prod").innerHTML = 'Cantidad a Preparar (Baja)';

            document.getElementById("info_item1").innerHTML = 'arroz';
            document.getElementById("desc_item1").innerHTML = '22 Kg.';

            document.getElementById("info_item2").innerHTML = 'pollo';
            document.getElementById("desc_item2").innerHTML = '30 Kg.';

            document.getElementById("info_item3").innerHTML = 'papa';
            document.getElementById("desc_item3").innerHTML = '15 Kg.';

            document.getElementById("info_item4").innerHTML = 'lenteja';
            document.getElementById("desc_item4").innerHTML = '10 Kg.';

            document.getElementById("info_item5").innerHTML = 'sandia';
            document.getElementById("desc_item5").innerHTML = '12 Kg';

            //MOSTRAR OBJETOS OCULTOS
            document.getElementById("tar_ind_1").hidden = false;
            document.getElementById("tar_ind_2").hidden = false;
            document.getElementById("tar_ind_3").hidden = false;
            document.getElementById("tar_ind_4").hidden = false;
            document.getElementById("tar_ind_5").hidden = false;
    }
        if (hoolder > 49 && hoolder < 100) {

            document.getElementById("cnt_prod").innerHTML = 'Cantidad a Preparar (Alta)';

            document.getElementById("info_item1").innerHTML = 'arroz';
            document.getElementById("desc_item1").innerHTML = '33 Kg.';

            document.getElementById("info_item2").innerHTML = 'pollo';
            document.getElementById("desc_item2").innerHTML = '42.5 Kg.';

            document.getElementById("info_item3").innerHTML = 'papa';
            document.getElementById("desc_item3").innerHTML = '23.3 Kg.';

            document.getElementById("info_item4").innerHTML = 'lenteja';
            document.getElementById("desc_item4").innerHTML = '19.8 Kg.';

            document.getElementById("info_item5").innerHTML = 'sandia';
            document.getElementById("desc_item5").innerHTML = '16 Kg';

            //MOSTRAR OBJETOS OCULTOS
            document.getElementById("tar_ind_1").hidden = false;
            document.getElementById("tar_ind_2").hidden = false;
            document.getElementById("tar_ind_3").hidden = false;
            document.getElementById("tar_ind_4").hidden = false;
            document.getElementById("tar_ind_5").hidden = false;
    }
    }
    if (x == 2){
        document.getElementById("text1").innerHTML = 'pasta'
        document.getElementById("text2").innerHTML = 'cerdo'
        document.getElementById("text3").innerHTML = 'queso'
        document.getElementById("inputItem4").hidden = true;
        document.getElementById("text5").innerHTML = 'mango'

        const button = document.getElementById("btn_aceptar")
        button.disabled = false;

        if (hoolder > 0 && hoolder < 50) {

            document.getElementById("cnt_prod").innerHTML = '(Cantidad a Preparar (Baja))';

            document.getElementById("info_item1").innerHTML = 'pasta';
            document.getElementById("desc_item1").innerHTML = '44.5 Kg.';

            document.getElementById("info_item2").innerHTML = 'cerdo';
            document.getElementById("desc_item2").innerHTML = '35.7 Kg.';

            document.getElementById("info_item3").innerHTML = 'queso';
            document.getElementById("desc_item3").innerHTML = '25.1 Kg.';

            document.getElementById("info_item5").innerHTML = 'mango';
            document.getElementById("desc_item5").innerHTML = '25.4 Kg';

            //MOSTRAR OBJETOS OCULTOS
            document.getElementById("tar_ind_1").hidden = false;
            document.getElementById("tar_ind_2").hidden = false;
            document.getElementById("tar_ind_3").hidden = false;
            document.getElementById("tar_ind_4").hidden = true;
            document.getElementById("tar_ind_5").hidden = false;
    }
        if (hoolder > 49 && hoolder < 100) {

            document.getElementById("cnt_prod").innerHTML = '(Cantidad a Preparar (Alta))';

            document.getElementById("info_item1").innerHTML = 'pasta';
            document.getElementById("desc_item1").innerHTML = '54 Kg.';

            document.getElementById("info_item2").innerHTML = 'cerdo';
            document.getElementById("desc_item2").innerHTML = '48.5 Kg.';

            document.getElementById("info_item3").innerHTML = 'queso';
            document.getElementById("desc_item3").innerHTML = '35.3 Kg.';

            document.getElementById("info_item5").innerHTML = 'mango';
            document.getElementById("desc_item5").innerHTML = '20 Kg';

            //MOSTRAR OBJETOS OCULTOS
            document.getElementById("tar_ind_1").hidden = false;
            document.getElementById("tar_ind_2").hidden = false;
            document.getElementById("tar_ind_3").hidden = false;
            document.getElementById("tar_ind_4").hidden = true;
            document.getElementById("tar_ind_5").hidden = false;
    }
    }

}




