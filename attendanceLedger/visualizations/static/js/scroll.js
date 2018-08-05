$(document).ready(function() {
  var table = $('#fixed-header').DataTable();

  new $.fn.dataTable.FixedHeader( table );
} );
