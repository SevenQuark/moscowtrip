$(document).ready(function(){
    $('#timelineTabs a').click(function (e) {
      e.preventDefault();
      $(this).tab('show');
    })
});
