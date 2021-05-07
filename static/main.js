function Signup() {
  $("#signup").modal("show");
}

$(".add_cart").click(function () {
  var item_id = $(this).attr("item_id");
  //console.log('hiii',item_id)
  $.ajax({
    type: "POST",
    url: "/add_to_cart/",
    data: { csrfmiddlewaretoken: $(".csrf_value").val(), item_id: item_id },
    dataType: "json",
  }).done(function (response) {
    if (response.is_added) {
      console.log(response);
      $("#class_button_" + item_id).attr("class", "btn btn-primary");
      $("#add" + item_id).html("added to Cart");
    } else {
      $("#class_button_" + item_id).attr("class", "btn btn-danger");
      $("#add" + item_id).html("add to Cart");
    }
  });
});

//============user search=============

$("#search").on("submit", function (e) {
  e.preventDefault();
  var query = $("#query").val();
  if (query) {
    $.ajax({
      type: "GET",
      url: "/search/result/",
      dataType: "json",
      data: { query: query, csrf: $(".csrf_value").val() },
    }).done(function (response) {
      $("#inner").html(response.rendered_html);
    });
  }
});
