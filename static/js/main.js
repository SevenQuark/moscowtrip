$(document).ready(function(){
    $('#timelineTabs a').click(function (e) {
      e.preventDefault();
      $(this).tab('show');
    })

    $('#id_date_to').datepicker()
    $('#id_date_from').datepicker()
});
