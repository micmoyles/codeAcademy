var main = function () {
	$('.btn-updateBook').click(function(event) {
	$.getJSON('book.json',function(jd) {
	$('.buyBook').text(jd.Buy);
	$('.sellBook').text(jd.Sell);
});
});
};

var err = function () {
    $.getJSON("book.json", function(d) {
        alert("success");
    }).fail( function(d, textStatus, error) {
        console.error("getJSON failed, status: " + textStatus + ", error: "+error)
    });
}
var autoreload = function () {
	$.getJSON('book.json',function(jd) {
	$('.buyBook').text(jd.Buy);
	$('.sellBook').text(jd.Sell);
});
};
var main2 = function () {
	$.ajaxSetup({cache: false});
	setInterval(function(){autoreload()},1000);
};
//$(document).ready(setInterval(function(){autoreload()},1000));
$(document).ready(main2);
