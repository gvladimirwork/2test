$(document).ready(function() {
  $("#id_q").keyup(function() {
    //if ($("#id_q").val()) {
    var input_string = $("#id_q").val();
    $.ajax({
      url : "/search/",
      type : "POST",
      dataType: "json",
      data : {
          client_response : input_string,
          csrfmiddlewaretoken: '{{ csrf_token }}'
          },
          success : function(json) {
            alert();
                      if (JSON.stringify(json).length > 2) {
                        $("#res").empty();  
                        $('#resTmpl').tmpl(json).appendTo("#res");
                      } else {
                        $("#res").empty();
                        $("#res").append('<p>No results found.</p>');
                      }

          },
          error : function(xhr,errmsg,err) {
            alert(xhr.status + ": " + xhr.responseText);
          }
    });
    //} else {
    //          $("#res").empty();
    //}
    return false;
  });
});
