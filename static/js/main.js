$(document).ready(function(){
    $('#timelineTabs a').click(function (e) {
      e.preventDefault();
      $(this).tab('show');
    })

    $('#id_date_to').datepicker({format: 'dd.mm.yyyy'});
    $('#id_date_from').datepicker({format: 'dd.mm.yyyy'});
});
