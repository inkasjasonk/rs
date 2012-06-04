$(document).ready(function(event    ){
    $('#raw').tablesorter();
    $("[type=submit],[type=image]").bind("click", function(e){
        $(this).parent().validate();
    });
});

