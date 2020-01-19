/**
 * Created by Andy on 2016/11/20.
 */
$(document).ready(function () {

    $("html").append('<div class="modal fade" id="msgbox0" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true"></div>');
    $("#msgbox0").load("../byyfy/msgbox.html");
    $("#header0").load("../byyfy/header.html");
    $("#footer0").load("../byyfy/footer.html");

    $('li.dropdown').mouseover(function () {
        $(this).addClass('open');
    }).mouseout(function () {
        $(this).removeClass('open');
    });

});

function getUrlParams(name) {
    var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)", "i");
    var r = window.location.search.substr(1).match(reg);
    if (r != null) return unescape(r[2]);
    return null;
}


/*
 function getUrlParams(targate1) {
 var data1 = [25,50,70,30,200,300,70 ];

 /!*  loop while true


 end loop*!/
 var r = window.location.search.substr(1).match(reg);
 if (r != null) return unescape(r[2]);
 return null;
 }
 */
