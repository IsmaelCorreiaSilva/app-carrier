$(document).ready(function(){
    $('#id_phone').mask('(00) 00000-0000');
    $('#id_zip_code').mask('00.000-000');
});

$('#id_zip_code').blur(function(){
    const cep = $('#id_zip_code').val().replace('-', '').replace('.','');+

        fetch("https://viacep.com.br/ws/"+cep+"/json/")
        .then(response => {
          if (!response.ok) {
            throw new Error("Erro na requisição: " + response.status);
          }
          return response.json();
        })
        .then(data => {
            $('#id_street').val(data.logradouro);
            $('#id_district').val(data.bairro);
            $('#id_city').val(data.localidade);
            $('#id_state').val(data.estado);
        })
        .catch(error => {
          console.error("Erro:", error);
        });
});