$(document).ready(function(){
    if($('#id_date_to').length >0){
        $('#id_date_to').datepicker({format: 'mm.dd.yyyy'});
        $('#id_date_from').datepicker({format: 'mm.dd.yyyy'});
    }
    $('.mt-star').rating({
        callback: function(value, link){ }
    });

    $('.toggle-sidebar').click(function(){
        var bar = $('#fluidSidebar');
        if(bar.is(':hidden')){
            bar.show();
            bar.animate({
                right:0
            });
        }else{
            bar.animate({
                right:'-300px'
            },function(){bar.hide();});
        }
        return false;
    })
});
