$(function () {

    $(document).on("click", "#enviar", function () {

        var imagem = new FormData($('#formulario')[0]);

        $.ajax({
            url: 'http://localhost:5000/salvar',
            method: 'POST',
            data: imagem, 
            contentType: false,
            cache: false,
            processData: false,
            success: function () {
                alert("Enviou a imagem direitinho!");
            },
            error: function () {
                alert("Não enviou a imagem");
            },
        });
    })
})