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
    // $("#error").hide();
    // $("#showError").click(function(){
    //     $("#error").show();
    // });
});