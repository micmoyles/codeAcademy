
var err = function () {
    $.getJSON("book.json", function(d) {
        alert("success");
    }).fail( function(d, textStatus, error) {
        console.error("getJSON failed, status: " + textStatus + ", error: "+error)
    });
}
var autoreload = function () {
	$.getJSON('book.json',function(jd) {
	$('.buylevel1').text(jd.Buy_1);
	$('.selllevel1').text(jd.Sell_1);
	$('.buylevel2').text(jd.Buy_2);
	$('.selllevel2').text(jd.Sell_2);
	$('.buylevel3').text(jd.Buy_3);
	$('.selllevel3').text(jd.Sell_3);
});
};
var main = function () {
	$.ajaxSetup({cache: false});
	setInterval(function(){autoreload()},1000);
};
//$(document).ready(setInterval(function(){autoreload()},1000));
$(document).ready(main);
