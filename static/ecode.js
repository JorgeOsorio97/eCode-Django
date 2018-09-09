$('#enviar').click((event)=>{
    event.preventDefault();
    console.log('enviando ecode');
    
    $.post({    
        url: 'http://127.0.0.1:8000/POST_ecode2tran/',
        data: {
            'ecode':$('#ecode').val(),     
        },
        dataType: 'json',
        success :function(data){
            console.log(data);
            if(data.success == true){
                window.open(`generatePDF/?id_transaccion=${data.id_transaccion}`)
            }
        }
      });
})