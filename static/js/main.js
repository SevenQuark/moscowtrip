$(document).ready(function(){
    if($('#id_date_to').length >0){
        $('#id_date_to').datepicker({format: 'mm.dd.yyyy'});
        $('#id_date_from').datepicker({format: 'mm.dd.yyyy'});
    }
    $('.mt-star').rating({
        callback: function(value, link){ }
    });
});
