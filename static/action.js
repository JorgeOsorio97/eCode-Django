
$('#pedrito').submit((event)=>{
    event.preventDefault();
    console.log('evento submit');
    window.open(`/generatePDF/?id_transaccion=D100799991201774000`,"_self")
    // $.post({    
    //     url: 'http://127.0.0.1:8000/POST_buscar/',
    //     data: {
    //         'tipo':$('#tipo').val(),
    //         'fecha':$('#fecha').val(),
    //         'hora':$('#hora').val(),
    //         'estado':$('#estado').val(),
    //         'municipio':$('#municipio').val(),
    //         'banco':$('#banco').val(),
    //         'u4':$('#u4').val()      
    //     },
    //     dataType: 'json',
    //     success :function(data){
    //         console.log(data);
    //         if(data.success == true){
    //             //window.open(`/generatePDF/?id_transaccion=${data.id_transaccion}`,"_self")
    //         }
    //     }
    //   });
});


// function getCookie(name) {
//     var cookieValue = null;
//     if (document.cookie && document.cookie !== '') {
//         var cookies = document.cookie.split(';');
//         for (var i = 0; i < cookies.length; i++) {
//             var cookie = jQuery.trim(cookies[i]);
//             // Does this cookie string begin with the name we want?
//             if (cookie.substring(0, name.length + 1) === (name + '=')) {
//                 cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//                 break;
//             }
//         }
//     }
//     return cookieValue;
// }
// var csrftoken = getCookie('csrftoken');


new Morris.Line({
    // ID of the element in which to draw the chart.
    element: 'myfirstchart',
    // Chart data records -- each entry in this array corresponds to a point on
    // the chart.
    data : [
        {"period":"2018-09-01","monto ($)":425.568},
        {"period":"2018-09-02","monto ($)":415.152}, 
        {"period":"2018-09-03","monto ($)":405.923}, 
        {"period":"2018-09-04","monto ($)":423.383}, 
        {"period":"2018-09-05","monto ($)":392.795}, 
        {"period":"2018-09-06","monto ($)":416.248}, 
        {"period":"2018-09-07","monto ($)":432.023}, 
        {"period":"2018-09-08","monto ($)":447.427}, 
        {"period":"2018-09-09","monto ($)":455.587}, 
        {"period":"2018-09-10","monto ($)":424.510}, 
        {"period":"2018-09-11","monto ($)":420.081}, 
        {"period":"2018-09-12","monto ($)":387.949}, 
        {"period":"2018-09-13","monto ($)":394.307}, 
        {"period":"2018-09-14","monto ($)":430.888}, 
        {"period":"2018-09-15","monto ($)":418.945}, 
        {"period":"2018-09-16","monto ($)":419.488}, 
        {"period":"2018-09-17","monto ($)":403.101}, 
        {"period":"2018-09-18","monto ($)":414.887}, 
        {"period":"2018-09-19","monto ($)":380.920}, 
        {"period":"2018-09-20","monto ($)":412.981}, 
        {"period":"2018-09-21","monto ($)":403.595}, 
        {"period":"2018-09-22","monto ($)":398.595}, 
        {"period":"2018-09-23","monto ($)":400.714}, 
        {"period":"2018-09-24","monto ($)":422.413}, 
        {"period":"2018-09-25","monto ($)":420.791}, 
        {"period":"2018-09-26","monto ($)":441.268}, 
        {"period":"2018-09-27","monto ($)":384.516}, 
        {"period":"2018-09-28","monto ($)":420.645}, 
        {"period":"2018-09-29","monto ($)":411.650}
        ],
    // The name of the data record attribute that contains x-values.
    xkey: 'period',
    // A list of names of data record attributes that contain y-values.
    ykeys: ['monto ($)'],
    // Labels for the ykeys -- will be displayed when you hover over the
    // chart.
    labels: ['Miles de pesos ($) por día']
  });