$('#outwards_from').on('submit', function(event) {
  event.preventDefault(); // prevent the default form submission

  // get the form data
  var formData = $(this).serialize();

  // send an AJAX request to check the quantity
  $.post('/check_quantity_mov/', formData, function(response) {
    if (response === 'true') {
      // if the quantity is valid, submit the form
      $('#outwards_from')[0].submit();
    } else {
      // if the quantity is invalid, display an alert
      alert('insufficient quantity');
    }
  });
});
