$(document).ready(function(){
    $('#timelineTabs a').click(function (e) {
      e.preventDefault();
      $(this).tab('show');
    })

    $('#id_date_to').datepicker({format: 'mm.dd.yyyy'});
    $('#id_date_from').datepicker({format: 'mm.dd.yyyy'});
});
