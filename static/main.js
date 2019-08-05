$(document).ready(function () {
    $("#loginform").hide();
    $("#regform").hide();
    $("#login").click(function(){
        $("#loginform").slideDown("slow");
    });
    $("#register").click(function(){
        $("#regform").slideDown("slow");
    });
    $("#register").click(function(){
        $("#register").hide();
        $("#login").hide();
    });
    $("#login").click(function(){
        $("#register").hide();
        $("#login").hide();
    });
    $("#oops").click(function(){
        $("#loginform").hide();
        $("#regform").slideDown("slow");
    });
    $.ajax({
        type:"GET",
        url:"https://app.ticketmaster.com/discovery/v2/events.json?size=1&apikey=c67uIW7Qedz4nlhrGmV9PwnRM42zl5au",
        async:true,
        dataType: "json",
        success: function(json) {
                    console.log(json);
                    // Parse the response.
                    // Do other things.
                 },
        error: function(xhr, status, err) {
                    // This time, we do not end up here!
                 }
      });
    // });
});