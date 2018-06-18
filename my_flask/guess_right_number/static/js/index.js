$( document ).ready(function() {
    $(".my_button").click(function(){
    alert('sasasasasas')
          $.post("/",
        {
            number: $(".my_number").val(),
        },
        function(data, status){
            $(".result").html(
            '<p>' +data.message+ '</p>'
            );
            $(".result").css('background-color','red');

        });
    })
});