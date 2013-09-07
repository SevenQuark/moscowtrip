$(document).ready(function(){
    $('#timelineTabs a').click(function (e) {
      e.preventDefault();
      $(this).tab('show');
    });
    $('.tree-toggle').click(function () {
        var child =  $(this).parent().children('ul.tree')
        if(child.is(":hidden")){
             $(this).addClass('active');
        }else{
             $(this).removeClass('active');
        }
	    child.toggle(200);
    });

    $('#id_date_to').datepicker({format: 'mm.dd.yyyy'});
    $('#id_date_from').datepicker({format: 'mm.dd.yyyy'});
});
