$("#submitLocation").on("click", function(e){
      e.preventDefault();
      $.ajax({
        data: {
          location: $("#location_id").val(),
        },
        type: "POST",
        url: "/dub-locations/",
      }).done(function (data) {
        if (data.output) {
          $("#location_form").submit();
          console.log(data.output);
        } else {
          alert("This Name is already used, please choose other one.");
        }
      });
    });
         $("#submitSales").on("click", function(e){
      e.preventDefault();
      $.ajax({
        data: {
          sales_id: $("#sales_id").val(),
        },
        type: "POST",
        url: "/dub-sales/",
      }).done(function (data) {
        if (data.output) {
          $("#sales_form").submit();
          console.log(data.output);
        } else {
          alert("This Name is already used, please choose other one.");
        }
      });
    });
$("#submitProduct").on("click", function (e) {
  e.preventDefault();
  $.ajax({
    data: {
      productId: $("#productId").val(),
      part_id: $("#part_id").val(),
      area: $("#area").val(),
    },
    type: "POST",
    url: "/dub-products/",
  }).done(function (data) {
    if (data.output) {
      $("#product_form").submit();
      console.log(data.output);
    } else {
      alert("A product with the same Product ID, Part ID, and Area already exists.");
    }
  });
});
$("#submitPerson").on("click", function (e) {
  e.preventDefault();
  $.ajax({
    data: {
      operationperson_id: $("#operationperson_id").val(),
      operationperson_phn: $("#operationperson_phn").val(),
    },
    type: "POST",
    url: "/dub-person/",
  }).done(function (data) {
    if (data.output) {
      $("#operationperson_form").submit();
      console.log(data.output);
    } else {
      alert("A product with the same Product ID, Part ID, and Area already exists.");
    }
  });
});



$("#product_form").submit(function (e) {
  var requiredFields = ["#productId", "#part_id", "#area"];
  var emptyFields = [];
  requiredFields.forEach(function(field) {
    if (!$(field).val()) {
      emptyFields.push(field);
    }
  });
  if (emptyFields.length > 0) {
    e.preventDefault();
    alert("Please fill all fields: " + emptyFields.join(", "));
  }
});
$("#vendor_form").submit(function (e) {
  var requiredFields = ["#vendor_id", "#vendor_phn", "#vendor_address"];
  var emptyFields = [];
  requiredFields.forEach(function(field) {
    if (!$(field).val()) {
      emptyFields.push(field);
    }
  });
  if (emptyFields.length > 0) {
    e.preventDefault();
    alert("Please fill all fields: " + emptyFields.join(", "));
  }
});
$("#operationperson_form").submit(function (e) {
  var requiredFields = ["#operationperson_id", "#operationperson_phn"];
  var emptyFields = [];
  requiredFields.forEach(function(field) {
    if (!$(field).val()) {
      emptyFields.push(field);
    }
  });
  if (emptyFields.length > 0) {
    e.preventDefault();
    alert("Please fill all fields: " + emptyFields.join(", "));
  }
});

$("#inward_from").submit(function (e) {
  var requiredFields = ["#productId", "#part_id", "#cost", "#quantity", "#vendor_id", "#vendor_address", "#vendor_phn", "#operationperson_id", "#operationperson_phn", "#location_id", "#location_area"];
  var emptyFields = [];
  requiredFields.forEach(function(field) {
    if (!$(field).val()) {
      emptyFields.push(field);
    }
  });
  if (emptyFields.length > 0) {
    e.preventDefault();
    alert("Please fill all fields: " + emptyFields.join(", "));
  }
});
$("#outward_from").submit(function (e) {
  var requiredFields = ["#productId", "#part_id","#quantity"];
  var emptyFields = [];
  requiredFields.forEach(function(field) {
    if (!$(field).val()) {
      emptyFields.push(field);
    }
  });
  if (emptyFields.length > 0) {
    e.preventDefault();
    alert("Please fill all fields: " + emptyFields.join(", "));
  }
});


      $("#submitVendor").on("click", function (e) {
      e.preventDefault();
      $.ajax({
        data: {
          vendor_id: $("#vendor_id").val(),
        },
        type: "POST",
        url: "/dub-vendors/",
      }).done(function (data) {
        if (data.output) {
          $("#vendor_form").submit();
          console.log(data.output);
        } else {
          alert("This Name is already used, please choose other one.");
        }
      });
    });
$(document).ready(function() {
  $('#location').change(function() {
    var location_id = $(this).val();
    $.ajax({
      url: '/get_remaining_area',
      data: {'location_id': location_id},
      dataType: 'json',
      success: function(data) {
        console.log(data);  // add this line to check the data returned by the server
        $('#remaining_area').val(data.remaining_area);
      }
    });
  });
});
$(document).ready(function() {
  $('#location').change(function() {
    var location_id = $(this).val();
    $.ajax({
      url: '/get_remaining_area',
      data: {'location_id': location_id},
      dataType: 'json',
      success: function(data) {
        console.log(data);  // add this line to check the data returned by the server
        $('#remaining_area').val(data.remaining_area);
      }
    });
  });
});

    $("#submitPerson").on("click", function (e) {
      e.preventDefault();
      $.ajax({
        data: {
          operationperson_id: $("#operationperson_id").val(),
        },
        type: "POST",
        url: "/dub-person/",
      }).done(function (data) {
        if (data.output) {
          $("#operationperson_form").submit();
          console.log(data.output);
        } else {
          alert("This Name is already used, please choose other one.");
        }
      });
    });