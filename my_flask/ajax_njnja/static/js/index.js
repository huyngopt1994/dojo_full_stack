$( document ).ready(function() {
    $(".my_button").click(function(){
          $.post("/",
        {
            color: $(this).val(),
        },
        function(data, status){
            $(".render_infor").html(
            '<p>' +data.message+ '</p>'+
            '<img src="/static/Ninjas/' + data.image+'">'
            )

        });
    })
});